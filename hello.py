#encoding:utf-8

def my_range():
    for i in range(10):
        a = i
        print(a)

test_int = 1

if not test_int:
    print "yes"
else:
    print "no"

import json

s = '{"extend_sum_gate":10, "extend_rate":0.9}'
print json.loads(s).items()
s = '99,22,33'
s = 'aaa,nnn'
dic = {}

def is_json(myjson):
    try:
        json.loads(myjson)
    except ValueError:
        return False
    return True

if is_json(s):
    print type(dic), dic
else:
    print "error"

import datetime

print datetime.datetime.now()

l = ['a', 'b', 'c']

s = 'a'

s ==
