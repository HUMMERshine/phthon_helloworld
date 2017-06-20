def add(x, y, f):
    return f(x) + f(y)

print(add(-4, 7, abs))

L = [abs(x) for x in [-1, 1, 2, -3]]
print(L)

#map和reduce函数
#map接受一个函数，和一个Iterable作为参数。返回一个iterator。
def f(x):
    return x * x

r = map(f, [1, 2, 3, 4, 5, 6, 7, 8, 9])
print(r)
print(next(r))#r是一个iterator
print(list(r))
#reduce函数接受一个函数f和一个序列作为输入，这个函数f必须接受两个参数。
# reduce(f, [x1, x2, x3, x4]) = f(f(f(x1, x2), x3), x4)
from functools import reduce
def fn(x, y):
    return x * 10 + y

print(reduce(fn, [1, 3, 5, 7, 9]))

def char2num(s):
    return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[s]

#转换字符串到int类型变量
def str2int(s):
    return reduce(fn, map(char2num, s))

print(str2int('024689'))

#练习：
def normalisze(name):
    return name[0].upper() + name[1:].lower()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalisze, L1))
print(L2)

def prod(L):
    return reduce(lambda x, y: x * y, L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))

def str2float(s):
    indexs = s.find('.')
    powers = len(s)-indexs-1
    if indexs ==-1:
        indexs = len(s) +1
        powers = 0
    def str2num(ss):
        return {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}[ss]
    num = map(str2num,s[:indexs]+s[indexs+1:])
    return reduce(lambda x,y:x*10+y,num)/(10**powers)
print('str2float(\'12.3456\') =', str2float('12.3456'))

'''end'''

#filter()函数，过滤一个序列，接受一个函数和一个序列
def not_empty(s):
    return s and s.strip()

print(list(filter(not_empty, ['A', '', 'B', None, 'C', '  '])))

#求素数：
def _odd_iter():
    n = 1
    while True:
        n = n + 2
        yield n

def _not_divisible(n):
    return lambda x: x % n > 0#x代表it内的每个元素，lamdba的含义，其实_not_divisible(n)它代表的是函数def(x):x % n > 0;

def primes():
    yield 2
    it = _odd_iter() # 初始序列
    while True:
        n = next(it) # 返回序列的第一个数
        yield n
        it = filter(_not_divisible(n), it) # 构造新序列,第一个参数实际代表def（x）:x % n > 0

for n in primes():
    if n < 1000:
        print(n)
    else:
        break

#sorted排序,第二个参数key函数，可以对每个元素进行处理
L = [36, 5, -12, 9, -21]
print(sorted(L))
print(sorted(L, key=abs))
print(sorted(L, key=abs, reverse=True))

S = ['bob', 'about', 'Zoo', 'Credit']
print(sorted(S))
print(sorted(S, key=str.lower))
print(sorted(S, key=str.lower, reverse=True))

#练习
L = [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)

def by_score(t):
    return t[1]
L2 = sorted(L, key=by_score)
print(L2)
'''end'''

def lazy_sum(*args):
    def sum():
        ax = 0
        for x in args:
            ax = ax + x
        return ax
    return sum

#f = lazy_sum(1, 2, 3, 4, 5)
f = lazy_sum(*[1, 2, 3, 4, 5])
print(f())

#闭包，返回函数
def count():
    fs = []
    for i in range(1, 4):
        def f():
            return i * i
        fs.append(f)
    return fs

f1, f2, f3 = count()
print(f1(), f2(), f3())

def count2():
    fs = []
    def f(j):
        def g():
            return j * j
        return g
    for i in range(1, 4):
        fs.append(f(i))
    return fs
f1, f2, f3 = count2()
print(f1(), f2(), f3())

'''一个函数可以返回一个计算结果，也可以返回一个函数。

返回一个函数时，牢记该函数并未执行，返回函数中不要引用任何可能会变化的变量。'''

#匿名函数
f = lambda x : x * x
print(f(5))

def build(x, y):
    return lambda : x * x + y * y
print(build(2, 3))
print(build(2, 3)())


'''Python对匿名函数的支持有限，只有一些简单的情况下可以使用匿名函数。'''

import functools

def log(text):
    def decorator(func):
        #下面的注解是改变now的name属性。
        #@functools.wraps(func)
        def wrapper(*args, **kw):
            print('%s %s():' % (text, func.__name__))
            return func(*args, **kw)
        return wrapper
    return decorator

@log('lst')
def now():
    print('2017-6-4')

now()
print(now.__name__)


