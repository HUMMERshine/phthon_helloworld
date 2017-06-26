#!/usr/bin/env python
#ecoding:utf-8

# 正常情况下，当我们定义了一个class，创建了一个class的实例后，我们可以给该实例绑定任何属性和方法，
# 这就是动态语言的灵活性。先定义class：


class Student(object):
    pass

s = Student()
s.name = "lishutao"

def set_age(self, age):
    self.age = age

# 给实例绑定一个方法
from types import MethodType

s.set_age = MethodType(set_age, s, Student)
s.set_age(25)

print s.age

# 给类绑定方法。
def set_score(self, score):
    self.score = score

Student.set_score = MethodType(set_score, None, Student)
s2 = Student()
s2.set_score(100)
print s2.score

class Student2(object):
    #Python允许在定义class的时候，定义一个特殊的__slots__变量，来限制该class能添加的属性：
    __slots__ = ('name', 'age')

# 使用__slots__要注意，__slots__定义的属性仅对当前类起作用，对继承的子类是不起作用的：
ss = Student2()
ss.name = 'Michael'
ss.age = 19
#ss.score = 97

print ss

'''除非在子类中也定义__slots__，这样，子类允许定义的属性就是自身的__slots__加上父类的__slots__。'''

# @property,@birth.setter:get和set方法。
class Student3(object):

    @property
    def birth(self):
        return self._birth

    @birth.setter
    def birth(self, value):
        self._birth = value

    # age是一个只读变量，不能赋值
    @property
    def age(self):
        return 100 - self._birth

s3 = Student3()
s3.birth = 99
#s3.age = 89 #只读变量。
print s3.birth
print s3.age

# @内的函数变量需要加一个下划线:_。
'''@property广泛应用在类的定义中，可以让调用者写出简短的代码，同时保证对参数进行必要的检查，这样，程序运行时就减少了出错的可能性。'''

class Student4(object):
    def __init__(self, name):
        self.__name = name
    #重载，__str__()方法。
    def __str__(self):
        return 'Student object (name : %s)' % self.__name

s4 = Student4("lishutao")
print s4.__repr__() #开发者可以看
print s4

# 如果一个类想被用于for ... in循环，类似list或tuple那样，就必须实现一个__iter__()方法，该方法返回一个迭代对象，然后，
# Python的for循环就会不断调用该迭代对象的next()方法拿到循环的下一个值，直到遇到StopIteration错误时退出循环。

class Fib(object):
    def __init__(self):
        self.a, self.b = 0, 1 # 初始化两个计数器a，b

    def __iter__(self):
        return self # 实例本身就是迭代对象，故返回自己

    def next(self):
        self.a, self.b = self.b, self.a + self.b # 计算下一个值
        if self.a > 100000: # 退出循环的条件
            raise StopIteration();
        return self.a # 返回下一个值

fib = Fib()
for x in fib:
    print x

# 要表现得像list那样按照下标取出元素，需要实现__getitem__()方法：
class Fib2(Fib):
    def __getitem__(self, n):
        a, b = 1, 1
        for x in range(n):
            a, b = b, a + b
        return a

fib = Fib2()
print fib[3]
print fib[10]
# print fib[10:19] 需要对传递的参数做判断。
# 原因是__getitem__()传入的参数可能是一个int，也可能是一个切片对象slice，所以要做判断：
class Fib3(Fib):
    def __getitem__(self, n):
        if isinstance(n, int):
            a, b = 1, 1
            for x in range(n):
                a, b = b, a + b
            return a
        if isinstance(n, slice):
            start = n.start
            stop = n.stop
            a, b = 1, 1
            L = []
            for x in range(stop):
                if x >= start:
                    L.append(a)
                a, b = b, a + b
            return L

fib = Fib3()
print fib[10:19]


