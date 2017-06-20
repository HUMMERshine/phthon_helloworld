import math

n1 = 255
n2 = 1000
print(hex(n1))
print(hex(n2))
'''调用Python的函数，需要根据函数定义，传入正确的参数。如果函数调用出错，一定要学会看错误信息，所以英文很重要！'''

#函数赋值给一个变量
a = abs
print(a(-1))

def my_abs(x):
    if x >= 0:
        return x
    else:
        return -x

def nop():
    pass

#类型检查
def my_abs2(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    elif x >= 0:
        return x
    else:
        return -x

#my_abs2('a')
#my_abs('a')


#函数可以返回多个值，其实返回的是一个tuple类型。
def move(x, y, step, angle=0):
    nx = x + step * math.cos(angle)
    ny = y + step * math.sin(angle)
    return nx, ny

x, y = move(100, 100, 60, math.pi / 6)
print(x, y)
r = move(100, 100, 60, math.pi / 6)
print(r)

'''定义函数时，需要确定函数名和参数个数；

如果有必要，可以先对参数的数据类型做检查；

函数体内部可以用return随时返回函数结果；

函数执行完毕也没有return语句时，自动return None。

函数可以同时返回多个值，但其实就是一个tuple。'''

#调用默认参数，来进行运算
def power(x, n = 2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s

print(power(5, 3))
print(power(8))

#默认参数是list类型，要注意：
def add_end(L = []):
    L.append("hello")
    return L

print(add_end())
print(add_end())#第二次打印了两次hello，因为默认参数list在定义时，就计算出了L，L已经存在了。

#定义默认参数要牢记一点：默认参数必须指向不变对象！
def add_end2(L = None):
    if L is None:
        L = []#每次都创建新的list，
    L.append("hello")
    return L

print(add_end2())
print(add_end2())

#可变参数,函数内部就收到的是一个tuple
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

print(calc(1,2,3,4))
num = [1,2,3,4]
print(calc(*num))#参数前面加*，表示吧list或tuple的内容作为可变参数传递给函数。

#关键字参数，传递0个或者多个dict类型的参数
def person(name, age, **kw):
    print('name:', name, 'age:', age, 'other:', kw)

person('Michael', 30)
person('Bob', 35, city = 'Beijing')
extra = {'city': 'Beijing', 'job':'Engineer'}
person('Jack', 24, city = extra['city'], job = extra['job'])
person('Jack', 24, **extra)#参数前加**引用字典类型变量。
#**extra表示把extra这个dict的所有key-value用关键字参数传入到函数的**kw参数，kw将获得一个dict，
# 注意kw获得的dict是extra的一份拷贝，对kw的改动不会影响到函数外的extra。

def person2(name, age, **kw):
    if 'city' in kw:
        pass
    if 'job' in kw:
        pass
    print('name:', name, 'age:', age, 'other:', kw)

#命名关键字参数：
def person3(name, age, *, city, job):
    print(name, age, city, job)

#用*分割参数，*后的参数必须出现在参数里：
person3('tom', 33, city='beijing', job = 'Engineer')
#person3('tom', 33)#缺少后两个参数不对。

#如果函数定义中已经有了一个可变参数，后面跟着的命名关键字参数就不再需要一个特殊分隔符*了：
def person4(name, age, *args, city, job):
    print(name, age, args, city, job)

#person4('tom', 33, 'Beijing', 'Engineer')
#如果有默认参数值，可以省略该参数。
def person5(name, age, *, city = 'Beijing', job):
    print(name, age, city, job)

person5('Tom', 44, job = 'Engineer')

#使用命名关键字参数时，要特别注意，如果没有可变参数，就必须加一个*作为特殊分隔符。如果缺少*，Python解释器将无法识别位置参数和命名关键字参数：


#在Python中定义函数，可以用必选参数、默认参数、可变参数、关键字参数和命名关键字参数，这5种参数都可以组合使用。
#但是请注意，参数定义的顺序必须是：必选参数、默认参数、可变参数、命名关键字参数和关键字参数。
def f1(a, b, c = 0, *args, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'args =', args, 'kw =', kw)

def f2(a, b, c=0, *, d, **kw):
    print('a =', a, 'b =', b, 'c =', c, 'd =', d, 'kw =', kw)

f1(1,2)
f2(1,2,d=99,ext=None)

args = (1, 2, 3, 4)
kw = {'d':99, 'x':'#'}
f1(*args, **kw)
#对于任意函数，都可以通过类似func(*args, **kw)的形式调用它，无论它的参数是如何定义的

'''Python的函数具有非常灵活的参数形态，既可以实现简单的调用，又可以传入非常复杂的参数。

默认参数一定要用不可变对象，如果是可变对象，程序运行时会有逻辑错误！

要注意定义可变参数和关键字参数的语法：

*args是可变参数，args接收的是一个tuple；

**kw是关键字参数，kw接收的是一个dict。

以及调用函数时如何传入可变参数和关键字参数的语法：

可变参数既可以直接传入：func(1, 2, 3)，又可以先组装list或tuple，再通过*args传入：func(*(1, 2, 3))；

关键字参数既可以直接传入：func(a=1, b=2)，又可以先组装dict，再通过**kw传入：func(**{'a': 1, 'b': 2})。

使用*args和**kw是Python的习惯写法，当然也可以用其他参数名，但最好使用习惯用法。

命名的关键字参数是为了限制调用者可以传入的参数名，同时可以提供默认值。

定义命名的关键字参数在没有可变参数的情况下不要忘了写分隔符*，否则定义的将是位置参数。'''

def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)

print(fact(100))

#汉诺塔：
def move(n, a, b, c):
    if n == 1:
        print('move', a, '-->', c)
    else:
        move(n-1, a, c, b)
        move(1, a, b, c)
        move(n-1, b, a, c)

move(4, 'A', 'B', 'C')
