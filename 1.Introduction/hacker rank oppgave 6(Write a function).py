'''
def is_leap(year):
    leap = False
    
    leap = year
    
    if (leap % 4) ==0:
        return True
        if (leap % 100) == 0: 
            return False
            if (leap % 400) == 0:
                return True
        
            return False
is_leap(year = int(input("Write your year here:")))
'''


def is_leap(year):
    leap = False
    
    
    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False


year = int(input("Write your year here:")))


