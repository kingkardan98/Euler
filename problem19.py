import datetime

years = range(1901, 2001)
months = range(1, 13)

sundayCounter = 0

for year in years:
    for month in months:
        weekday = datetime.datetime(year, month, 1).weekday()
        if weekday == 6:
            sundayCounter += 1

print(sundayCounter)