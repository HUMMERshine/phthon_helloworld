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
    print type(s), s
else:
    print "error"

print is_json('111'), "----"
print json.loads(u'111'), type(json.loads(u'111'))

import datetime

print datetime.datetime.now()

l = ['a', 'b', 'c']

s = 'a'


d = {'a': 1, 'b': {}}

d.update({})
print d['b']
if d['b']:
    print 'ok'

if 'a' in d:
    print "in"
else:
    print 'not in'

dict1 = {'aaa' : 1, 'bbb' : 2}
dict2 = {'aaa' : 2, 'bbb' : 3}

def compare_dict(info, be, af):
    for key in be:
        if not af[key]:
            print "删除"
            if not info['delete']:
                info['delete'] = []
            info['delete'].append(key)
        elif be[key] != af[key]:
            if isinstance(be[key], dict):
                compare_dict(info, be[key], af[key])
                is_add(info, be[key], af[key])
            else:
                print "修改"
                if not info['edit']:
                    info['edit'] = []
                info['edit'].append((key, be[key], af[key]))

def is_add(info, be, af):
    for key in af:
        if not be[key]:
            print "新增"
            if not info['add']:
                info['add'] = []
            info['add'].append(key)

now = datetime.datetime.now()

print ("%s", now)
print ("%s/%s/%s %s:%s:%s" % (now.year, now.month, now.day, now.hour, now.minute, now.second))

s = 'abc,abc,abc,'
s = s[:-1]
print type(s), s

s = u"{\"abc\":123}"
print type(json.loads(s))
s = "123"
print type('s'), json.loads(s),is_json(s)
s = 's'
# print type('s'), json.loads(s),is_json(s)
print type("你好")
s = s + "你好"
print type('s')

print json.loads("123")

a = u'Bl\xe1Bl\xe1Logia'
print str(s)