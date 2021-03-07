import calendar

yy = int(input("what year is it: "))
mm = int(input("what month you want: "))
dd = int(input("what date is it to know what dayis it: "))

print(calendar.month(yy,mm,dd))

