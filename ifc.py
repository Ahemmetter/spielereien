# -*- coding: utf-8 -*-

import datetime as dt

# date_greg = dt.date.today()                     # get current date in Gregorian calendar
x = int(raw_input("Year: "))
y = int(raw_input("Month: "))
z = int(raw_input("Day: "))

date_greg = dt.datetime(x, y, z)

day_greg = int(date_greg.strftime("%d"))
month_greg = int(date_greg.strftime("%m"))
year_greg = int(date_greg.strftime("%Y"))

doy_greg = date_greg.timetuple().tm_yday - 1
year = year_greg + 10000

suits = [u"\u2660", u"\u2665", u"\u2666", u"\u2663", u"\u2605"]
weekdays = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

def ifc():
    if (year % 4 == 0) and not (year % 100 == 0) or (year % 400 == 0):
        if doy_greg < 168:
            month = doy_greg / 28 + 1
            day = doy_greg % 28 + 1
            season = doy_greg / 13
        elif doy_greg == 168:
            month = 6
            day = 29
            season = "Leap Day"
        elif doy_greg == 365:
            month = 13
            day = 29
            season = "Year Day"
        else:
            doy_greg_new = doy_greg - 169
            month = doy_greg_new / 28 + 7
            day = doy_greg_new % 28 + 1
            season = doy_greg_new / 13
    else:
        if doy_greg == 364:
            month = 13
            day = 29
            season = "Year Day"
        else:
            month = doy_greg / 28 + 1
            day = doy_greg % 28 + 1
            season = doy_greg / 13

    if day == 29:
        week = 4
    else:
        week = (day - 1) / 7

    card = (month - 1) / 13

    if day == 29:
        card = 13

    if day != 29:
        weekday = (day - 1) % 7

    # return day, month, season
    print "Gregorian: " + weekdays[(date_greg.weekday() + 1) % 7] + ", the " + str(day_greg) + "." + str(month_greg) + "." + str(year_greg)
    print "IFC: " + weekdays[weekday] + ", the " + str(day) + "." + str(month) + "." + str(year)# + ", " + suits[card]

ifc()
