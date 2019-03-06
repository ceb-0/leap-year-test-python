#leap year test by ceb@

print("############################")
print("leap year test")
print("by ceb@")
print("############################")

def leapyeartest():
    leap_year = False
    year = input("Type a year: \n")
    year = int(year)
    if year%400 == 0:
        leap_year = True
    elif year%100 == 0:
        leap_year = False
    elif year%4 == 0:
        leap_year = True
    else:
        leap_year = False
    if leap_year == True:
        print("This year is a leap year!")
    else:
        print("This year is not a leap year!")

def want_to_start():
    start = False
    ask_start = 1
    ask_start = input("Want you start ? Yes = 1 | No = 0 \n")
    if type(ask_start) == int or float:
        ask_start = float(ask_start)
        if float(ask_start) == 1:
            start = True
        elif float(ask_start) == 0:
            start = False
    else:
        print("ERROR-1")
        want_to_start()
    if start == True:
        leapyeartest()
    elif start == False:
        want_to_start()
    else:
        print("ERROR-2")
    want_to_start()

want_to_start()



#by ceb@
