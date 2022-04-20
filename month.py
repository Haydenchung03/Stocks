
class month:
    
    def __init__(self, month):
        self.month = month
    
    def numToMonth(self):
        month1 = {
        1 : 'January',
        2 : 'Februrary',
        3 : 'March',
        4 : 'April',
        5 : 'May',
        6 : 'June',
        7 : 'July',
        8 : 'August',
        9 : 'May',
        10 : 'June',
        11 : 'July',
        12 : 'August',
        }
        if self.month in month1:
            print(self.month)