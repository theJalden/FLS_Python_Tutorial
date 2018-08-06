import csv
import matplotlib.pyplot as plt

import datetime

month2num = {"Jan":1, "Feb":2, "Mar":3,
             "Apr":4, "May":5, "Jun":6,
             "Jul":7, "Aug":8, "Sep":9,
             "Oct":10, "Nov":11, "Dec": 12}

# String /* Mon YYYY */ => datetime
# Returns a date-time object given a string
# with the indicated month and year
def makeDateTime(date_str):
    mon_str, yr_str = date_str.split()
    return datetime.datetime(int(yr_str), month2num[mon_str], 1)



ff = open('lfpr.csv')

ff_reader = csv.reader(ff)
    
for ii, xx in enumerate(ff_reader):
    if ii==0:
        jj = [nn for nn in range(len(xx))]
        print(makeDateTime(xx[123]))
    
        dates = jj[1:-5]
    elif ii ==1:
        values = [ float(vv) for vv in xx[1:-5]]

fig, ax = plt.subplots()

plt.plot(dates,values)

plt.show()
