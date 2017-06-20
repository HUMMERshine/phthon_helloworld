#encoding:utf-8

from datetime import datetime
from hello import my_range


now = datetime.now()

print ("%s", now)
print ("%s/%s/%s %s:%s:%s" % (now.hour, now.minute, now.second, now.month, now.day, now.year))

#调用hello.py的my_range函数
my_range()