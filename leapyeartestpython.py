#leap year test by ceb@

print("############################")
print("leap year test")
print("############################")

year = input("Type a year:")
year = int(year)
leap_year = False

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

#by ceb@
