import os

if os.path.exists("/Users/lishutao/b.txt"):
    data = open("/Users/lishutao/b.txt")
    for each_line in data:
        try:
            (first, second) = each_line.split(';', 1)
            print(first, end='')
            print(' said:', end='')
            print(second, end='')
        except:
            pass
else:
    print('The data file is missing')

"""
data.close()

data = open("/Users/lishutao/b.txt")
for each_line in data:
    print(each_line, end='')

data.close()
"""