def is_leap(year):
    leap = False
    
    x = year
    if x&4 == 0:
        if x&100 != 0 or x&400 == 0:
            leap = True
    else:
        leap = False
    return leap

year = int(input())