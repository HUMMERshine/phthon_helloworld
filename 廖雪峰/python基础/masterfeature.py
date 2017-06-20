#encoding:utf-8

L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

#三种方式打印前三个数据。
print([L[0], L[1], L[2]])

r = []
n = 3
for i in range(n):
    r.append(L[i])
print(r)

print(L[0:3])

#记住倒数第一个元素的索引是-1
print(L[-1])

L = list(range(100))
print(L)
print(L[-20:-10:3])
print(L[:])

T = (1,2,3,4,5,6,7)
print(T[:3])

strs = "ABCDEFG"
print(strs[:3])
print(strs[::2])

#字典的迭代。
d = {'a': 1, 'b': 2, 'c': 3}

for value in d.values():
    print(value)
for value in d.items():
    print(value)
for value in d:
    print(value, d[value])
#for循环内可以有多个变量
for k, v in d.items():
    print(k , '=', v)

#判断对象可迭代:
from collections import Iterable
print(isinstance('abc', Iterable))
print(isinstance([1, 2, 3], Iterable))
print(isinstance(123, Iterable))

#获取下标
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)

for x, y in [(1,2), (2, 3), (3, 4)]:
    print(x, y)

#列表生成式：
L = []
for x in range(1, 11):
    L.append(x * x)
print(L)

print([x * x for x in range(1, 11)])

print([x * x for x in range(1, 11) if x > 5])

#双重循环，形成全排列
print([m +n for m in 'ABC' for n in 'ABC'])

#列出当前目录下的所有文件和目录
import os
print([d for d in os.listdir('.')])

d = {'x': 'A', 'y': 'B', 'z': 'C' }
print([k + '=' + 'v' for k, v in d.items()])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

L1 = ['Hello', 'World', 18, 'Apple', None]
print([s.lower() for s in L1 if isinstance(s, str)])

'''运用列表生成式，可以快速生成list，可以通过一个list推导出另一个list，而代码却十分简洁。'''
#生成器，是一种算法。使用（）表示：
g = (x * x for x in range(10))

print(g)

print(next(g))
print(next(g))
print(next(g))

for n in g:
    print(n)

#杨辉三角：函数式生成器
def triangles():
    L = []
    while True:
        L.append(1)
        i = len(L) - 2
        while i > 0:
            L[i] = L[i] + L[i-1]
            i = i - 1
        yield L

def triangles2():
    L = [1]
    while True:
        yield L
        L.append(0)#把0加入到L尾部
        L = [L[i - 1] + L[i] for i in range(len(L))]#当i==0时，L[i-1] 是L[-1]也就是0

n = 0
for t in triangles2():
    print(t)
    n = n + 1
    if n == 10:
        break

#生成器都是Iterator对象，但list、dict、str虽然是Iterable，却不是Iterator。
#把list、dict、str等Iterable变成Iterator可以使用iter()函数：
from collections import Iterator

print(isinstance([], Iterable))
print(isinstance(iter([]), Iterator))

it = iter([1, 2, 3, 4, 5])
it2 = iter((1, 2, 3, 4, 5))
print(type([]))
print(type(it))
print(type(it2))

while True:
    try:
        x = next(it)
        print(x)
    except StopIteration:
        print("end")
        break
'''凡是可作用于for循环的对象都是Iterable类型；

凡是可作用于next()函数的对象都是Iterator类型，它们表示一个惰性计算的序列；

集合数据类型如list、dict、str等是Iterable但不是Iterator，不过可以通过iter()函数获得一个Iterator对象。

Python的for循环本质上就是通过不断调用next()函数实现的，例如：'''


