from calendar import month
import bs4
from bs4 import BeautifulSoup
import requests
import re
from month1 import month1
from stock import *
from datetime import datetime
from pytz import timezone


def main():
    
    while(True):
        now = datetime.now()
        tz = timezone('EST')
        current_time = datetime.now(tz)
        comma = ','

        getMonth1 = month1(current_time.month)
        getName = getMonth1.numToMonth()
        
        print("Main Menu")
        print(f'Current Time = {getName} {current_time.day}{comma}{current_time.year}')
        print(f"Current Time = {current_time.hour + 1}:{current_time.minute}:{current_time.second}")
        #user_option = input(" ")
        user_input = input('Enter in a ticker: ')

        user_stock = stock(user_input)
        
        get_stock = user_stock.get_ticker()
        
        url = f'https://finance.yahoo.com/quote/{get_stock}/'

        response = requests.get(url)

        soup = BeautifulSoup(response.text, "lxml")

        if current_time.hour >= 9.5 and current_time.hour < 16:
            current_price = soup.find_all('div', {'class':'My(6px) Pos(r) smartphone_Mt(6px) W(100%)'})[0].find('fin-streamer').text

            print(f'This is the price of the current stock: {current_price}')
        else:
            extended_hours = soup.find('fin-streamer', {'class': "C($primaryColor) Fz(24px) Fw(b)"}).text
            
            print(f'This is the price of the stock in extended trading hours: {extended_hours}');

main()


