#encoding:utf-8

import logging

logging.basicConfig(level=logging.INFO)

# logging的好处，它允许你指定记录信息的级别，有debug，info，warning，error等几个级别，当我们指定level=INFO时，
# logging.debug就不起作用了。同理，指定level=WARNING后，debug和info就不起作用了。
# 这样一来，你可以放心地输出不同级别的信息，也不用删除，最后统一控制输出哪个级别的信息。

def foo(s):
    return 10 / int(s)

def bar(s):
    return foo(s) * 2

def main():
    try:
        bar('0')
    except StandardError, e:
        logging.info(e)
        print e
        logging.exception(e)
        print "hello"

main()
print 'END'

class myError(StandardError):
    pass

def fo(s):
    n = int(s)
    if n == 0:
        raise myError('invalidvalue %s' % s)
    return 10 % n

#捕获自定义的错误
try:
    fo(0)
except StandardError, e:
    print e

'''Python内置的try...except...finally用来处理错误十分方便。出错时，会分析错误信息并定位错误发生的代码位置才是最关键的。

程序也可以主动抛出错误，让调用者来处理相应的错误。但是，应该在文档中写清楚可能会抛出哪些错误，以及错误产生的原因。'''

