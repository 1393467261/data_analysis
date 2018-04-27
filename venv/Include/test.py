#coding:utf-8
from pandas import Series
import csv
import random
import datetime

fn = 'data.csv'

with open(fn, 'w') as fp:
    wr = csv.writer(fp)
    wr.writerow(['date', 'count'])
    startDate = datetime.date(2017, 1, 1)

    for i in range(365):
        amount = 300 + i*5 + random.randrange(100)
        wr.writerow([str(startDate), amount])
        startDate = startDate + datetime.timedelta(days=1)

def __main__():
    print("你好，世界")
__main__()