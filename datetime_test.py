from datetime import datetime

now = datetime.now()

print("%s" % now)
print("%s/%s/%s %s:%s:%s" % (now.hour, now.minute, now.second, now.month, now.day, now.year))