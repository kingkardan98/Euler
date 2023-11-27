months = {
    "Jan": 31,
    "Feb": 28,
    "FebLeap": 29,
    "Mar": 31,
    "Apr": 30,
    "May": 31,
    "Jun": 30,
    "Jul": 31,
    "Aug": 31,
    "Sep": 30,
    "Oct": 31,
    "Nov": 30,
    "Dec": 31
}

days = {
    "Mon": 1,
    "Tue": 2,
    "Wed": 3,
    "Thu": 4,
    "Fri": 5,
    "Sat": 6,
    "Sun": 7
}

years = range(1900, 2001)

def isLeapYear(year):
    isDivisibleByFour = year % 4 == 0
    isCentury = year % 100 == 0
    isDivisibleBy400 = year % 400 == 0

    if isDivisibleByFour and (not isCentury) and isDivisibleBy400:
        return True
    return False

def countDays(year):
    if isLeapYear(year):
        return 366
    return 365

totalDays = 0
yearDict = dict()
for year in years:
    yearDict[year] = countDays(year)
    totalDays += yearDict[year]