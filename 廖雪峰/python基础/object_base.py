#!/usl/bin/env python
#encoding:utf-8

class Student (object):
    def __init__(self, name, score):
        self.__name = name
        self.__score = score

    def print_score(self):
        print ('%s: %s') % (self.__name, self.__score)

    def get_grade(self):
        if self.__score >= 90:
            return 'A'
        elif self.__score >= 60:
            return 'B'
        else:
            return 'C'

bart = Student("lishutao", 99)
print bart
print Student
#print bart.__name  #外部无法访问__下划线变量,双下划线
bart.print_score()
print bart.get_grade()
bart.age = 19
print Student.__dict__
print bart.__dict__


class Animal(object):
    def run(self):
        print "Animal is running..."

class Dog(Animal):
    def run(self):
        print "Dog is running..."

class Cat(Animal):
    def run(self):
        print "Cat is running..."

#多态
dog = Dog()
cat = Cat()

dog.run()
cat.run()

print isinstance(dog, Dog)
print isinstance(dog, Animal)
print isinstance(dog, Cat)

'''继承可以把父类的所有功能都直接拿过来，这样就不必重零做起，子类只需要新增自己特有的方法，也可以把父类不适合的方法覆盖重写；

有了继承，才能有多态。在调用类实例方法的时候，尽量把变量视作父类类型，这样，所有子类类型都可以正常被接收；

旧的方式定义Python类允许不从object类继承，但这种编程方式已经严重不推荐使用。任何时候，如果没有合适的类可以继承，就继承自object类。'''

print type(123)
print type(None)
print type(abs)
print type(dog)

print isinstance('abc', str)
print isinstance(u'abc', unicode)
print isinstance('abc', unicode)

print dir('ABC')

print hasattr(bart, 'age')
print getattr(bart, 'age')