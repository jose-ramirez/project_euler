#You are given the following information, but you may prefer
#to do some research for yourself.
#
#1 Jan 1900 was a Monday.
#Thirty days has September, April, June and November.
#All the rest have thirty-one, Saving February alone,
#Which has twenty-eight, rain or shine.
#And on leap years, twenty-nine.
#A leap year occurs on any year evenly divisible by 4,
#but not on a century unless it is divisible by 400.
#
#How many Sundays fell on the first of the
#month during the twentieth century (1 Jan 1901 to 31 Dec
#2000)?

def is_leap(year):
	a = (year % 4 == 0 and year % 100 != 0)
	b = year % 400 == 0
	return a or b

def p19():
    total = 0
    start = 1 #jan 1st, 1900 is monday:
    common = [3, 0, 3, 2, 3, 2, 3, 3, 2, 3, 2]
    leap = [3, 1, 3, 2, 3, 2, 3, 3, 2, 3, 2]
    for year in range(1901, 2001):
        #get first day of the year, 0 is sunday:
        a = 2 if is_leap(year - 1) else 1
        y = leap if is_leap(year) else common
        start = (start + a) % 7
        tmp = start
        #get first days of year's months:
        f = []
        for d in y:
        	tmp += d
        	tmp %= 7
        	f.append(tmp)
        #count sundays:
        g = [x for x in f if x == 0]
        #add the count to the total, adding the first day
        # if it was sunday:
        t = len(g) if start != 0 else len(g) + 1
        total += t
    return total

print(p19())