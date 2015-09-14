# this algorithm works in SOME cases but not ALL
# can you identify in which cases this algorithm fails?

daysOfMonths = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def isLeapYear(year):   # https://en.wikipedia.org/wiki/Leap_year#Algorithm
    if year % 4 != 0:
        return 365
    elif year % 100 != 0:
        return 366
    elif year % 400 != 0:
        return 365
    else:
        return 366

def daysBetweenDates(y1, m1, d1, y2, m2, d2):
    days = daysOfMonths[m1 - 1] - d1
    m1 += 1

    while m1 < m2:
        if m1 == 2 and isLeapYear(y1) == 366:
            days += 29
        else:
            days += daysOfMonths[m1]
        m1 += 1
    days += d2
    while y1 < y2:
        days += isLeapYear(y1)
        y1 += 1
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
