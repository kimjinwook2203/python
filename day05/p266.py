import time;
import datetime;


t=time.time()#1970.1.1~현재까지의 초
print(t)
localtime = time.localtime()
print(time.localtime())
print(localtime.tm_year)
print(localtime.tm_mon)
print(localtime.tm_mday)

localtime2 = datetime.datetime.now()


print(localtime2)
print(localtime2.year)