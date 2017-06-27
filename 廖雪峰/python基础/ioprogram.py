#!/usr/bin/env python
#encoding:utf-8

try:
    f = open('/Users/lst-bytedance/code/hello.py', 'r')
    s = f.read()
    print s
finally:
    if f:
        f.close()

with open('/Users/lst-bytedance/code/hello.py', 'r') as f:
    s = f.read()
    print s

with open('/Users/lst-bytedance/code/hello.py', 'r') as f:
    for line in f.readlines():
        print line

# 打开非ASCI码的文件要用'rb'模式。
with open('/Users/lst-bytedance/Desktop/git.jpg', 'rb') as f:
    print f.read()

# 写文件。'a+'不会覆盖，'w'和'w+'会覆盖。
with open('/Users/lst-bytedance/code/hello.py', 'a+') as f:
    f.write('print \'Hello, world!\'\n')

with open('/Users/lst-bytedance/code/hello.py', 'r') as f:
    s = f.read()
    print s

'''在Python中，文件读写是通过open()函数打开的文件对象完成的。使用with语句操作文件IO是个好习惯。'''

import os

print os.name, os.uname()
print os.environ
print os.getenv('PATH')
print os.path.abspath('.')
print os.path.join('/Users/lst-bytedance', 'testdir')
dir_s = os.path.join('/Users/lst-bytedance', 'testdir')
os.mkdir(os.path.join('/Users/lst-bytedance', 'testdir'))
os.rmdir(dir_s)
print os.path.split(dir_s)
print os.path.splitext('/Users/lst-bytedance/code/hello.py')
print os.listdir('/Users/lst-bytedance/')

# 编写一个search(s)的函数，能在当前目录以及当前目录的所有子目录下查找文件名包含指定字符串的文件，并打印出完整路径：
def search(s, dir_name = os.path.abspath('/Users/lst-bytedance/PycharmProjects')):
     for file in os.listdir(dir_name):
         path = os.path.join(dir_name, file)
         if os.path.isdir(path):
             search(s, path)
         else:
             if s in file:
                 print path

search('hello', '/Users/lst-bytedance/PycharmProjects')
print
search('hello')


'''Python的os模块封装了操作系统的目录和文件操作，要注意这些函数有的在os模块中，有的在os.path模块中。'''

import json

# dump/load 要结合文件来操作， dumps和loads不需要结合文件。
f = open('dump.txt', 'w')
d = dict(name = 'Bob', age = 18, score = 99)
s = json.dumps(d) # 如果不想要每个key前都有一个'u',就是用该方法，把dict转换为str。
s2 = json.dump(d, f)
print s, s2
d1 = json.loads(s)
d3 = json.loads(s, encoding='utf-8')
f.close()
f = open('dump.txt', 'r')
d2 = json.load(f)

print type(d), type(s), type(d2), type(s2)
print d, d1, s, d2, s2
print d3
print str(d)
f.close()

for key in d.keys():
    print type(key), key
for key in d1.keys():
    print type(key), key

# 序列化对象，直接用json 转换class对象不会成功，需要使用自定义的方法来进行转换
class Student(object):
    def __init__(self, name, age, score):
        self.name = name
        self.age = age
        self.score = score

def student2dict(stu):
    return {
        'name' : stu.name,
        'age' : stu.age,
        'score' : stu.score
    }

s = Student('Tom', 33, 66.9)
print json.dumps(s, default=student2dict)

print json.dumps(s, default= lambda obj : obj.__dict__)

# 反序列化json为对象：
def dict2student(d):
    return Student(d['name'], d['age'], d['score'])

str_json = '{"name":"tom", "age": 18, "score": 77.7}'
stu = json.loads(str_json, object_hook=dict2student)
print type(s), s, type(stu), stu

'''Python语言特定的序列化模块是pickle，但如果要把序列化搞得更通用、更符合Web标准，就可以使用json模块。

json模块的dumps()和loads()函数是定义得非常好的接口的典范。当我们使用时，只需要传入一个必须的参数。但是，
当默认的序列化或反序列机制不满足我们的要求时，我们又可以传入更多的参数来定制序列化或反序列化的规则，
既做到了接口简单易用，又做到了充分的扩展性和灵活性。'''