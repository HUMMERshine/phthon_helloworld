#!/usr/bin/env python
# -*- coding: utf-8 -*-

' a test module '

#从Python 2.7到Python 3.x就有不兼容的一些改动，比如2.x里的字符串用'xxx'表示str，
# Unicode字符串用u'xxx'表示unicode，而在3.x中，所有字符串都被视为unicode，因此，写u'xxx'和'xxx'是完全一致的，
# 而在2.x中以'xxx'表示的str就必须写成b'xxx'，以此表示“二进制字符串”。

from __future__ import unicode_literals #注释该行，看下面四行代码区别
import sys

print '\'xxx\' is unicode?', isinstance('xxx', unicode)
print 'u\'xxx\' is unicode?', isinstance(u'xxx', unicode)
print '\'xxx\' is str?', isinstance('xxx', str)
print 'b\'xxx\' is str?', isinstance(b'xxx', str)



__author__ = 'lishutao'

def test():
    args = sys.argv
    if len(args)==1:
        print 'Hello, world!'
    elif len(args)==2:
        print 'Hello, %s!' % args[1]
    else:
        print 'Too many arguments!'

if __name__=='__main__':
    test()
    l = sys.path
    for item in l:
        print item

