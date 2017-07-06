#encoding:utf-8

print 'I\'m Ok!'
print r"I'm Ok !"
print('\\\t\\')
print(r'\\\t\\')

print (r'''hello
    lstad
    asdfsadf''')

age = 19
if age > 18:
    print('adult')
else:
    print('teenager')

PI = 3.1415926
print(PI)

print(7/4)
print(7//4)
print(7%4)
print 7/float(3)

n = 123
f = 456.789
s1 = 'Hello, world'
s2 = 'Hello, \'Adam\''
s3 = r'Hello, "Bart"'
s4 = r'''Hello,
Lisa!'''

print(n,f,s1,s2,s3,s4)

# str1 = '中文'.encode('gb2312')
# str2 = '中文'.encode('utf-8')
str1 = '中文'
str2 = '中文'
print(str1, str2)

#height = input('请输入身高：')
height = 22
#weight = input('请输入体重：')
weight = 22
bmi = float(weight) / (float(height) ** 2)

if bmi < 18.5:
    print('过轻。')
elif bmi >= 18.5 and bmi <= 25:
    print('正常。')
elif bmi >25 and bmi <=28:
    print('过重。')
elif bmi > 28 and bmi <=32:
    print('肥胖。')
else:
    print('严重肥胖。')

res = 'yes' if bmi < 18.5 else 'no'
print res

L = ['bart', 'Lisa', 'Adam']
(a, b, c) = L# 多个变量同时赋值。
print a, b, c
for name in L:
    print('hello, ' + name + '!')
L.pop(1) # 删除第二个元素
L.remove('bart') # 移除值为bart的元素
print(L) #
print L * 3, '每个元素重复三次'
L = '100'
l = []
if l:
    print "l !---> empty"
else:
    print "l ---> empty"
l.append(L)
print l

d = {"mike":95, "tom":88, "jim":77}
print(d), "tems返回类型", type(d.items())
for key, value in d.items():
    print key, value
t = (1, 2, 3)#不变对象
t2 = (1, 2, [1, 2])#不变对象，但是里边的list内容可变，hash不唯一
d[t] = 1
#d[t2] = 2 # 不可以把 t2当做key放入字典内，因为t2的hash不唯一。
print(d)

d2 = dict(mike2=95, tom2=88, jim2=77)
print(d2)

d.update(d2) # 把d2字典数据，加入到d内。
print d

#set的原理和dict一样，所以，同样不可以放入可变对象，因为无法判断两个可变对象是否相等，也就无法保证set内部“不会有重复元素”。
s = set({1, 2, 2, 3, 3, 4})
print(s)
s.add(5)
s.add(5)
print(s)
s.add(t)
print(s)
#s.add(t2)
print(s)
print list(s)

s = set((1, 3, 4))
print s

s = set([1, 3, 5])
print s
