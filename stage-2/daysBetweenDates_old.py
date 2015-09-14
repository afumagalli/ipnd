daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):	# https://en.wikipedia.org/wiki/Leap_year#Algorithm
	if year % 4 != 0:
		return False
	elif year % 100 != 0:
		return True
	elif year % 400 != 0:
		return False
	else:
		return True

def endYear(y1, m1, d1):
	days = 0
	month = m1 + 1

	days += daysOfMonths[m1 - 1] - d1
	while (month < 13):
		days += daysOfMonths[month - 1]
		month += 1
	return days

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
	days = 0
	year = y1 + 1
	month = 1

	if y1 != y2:
		days += endYear(y1, m1, d1)

	if y1 == y2:
		days += daysOfMonths[m1 - 1] - d1
		month = m1 + 1

	while year < y2:
		if isLeapYear(year):
			days += 366
		else:
			days += 365
		year += 1

	while month < m2:
		if month == 2 and isLeapYear(y2):
			days += 29
		else:
			days += daysOfMonths[month - 1]
		month += 1

	days += d2
	return days

def test():
    test_cases = [((2012,1,1,2012,2,28), 58),
                  ((2012,1,1,2012,3,1), 60),
                  ((2011,6,30,2012,6,30), 366),
                  ((2011,1,1,2012,8,8), 585 ),
                  ((1900,1,1,1999,12,31), 36523)]
    
    for (args, answer) in test_cases:
        result = daysBetweenDates(*args)
        if result != answer:
            print "Test with data:", args, "failed"
            print result
        else:
            print "Test case passed!"

test()