#encoding:utf-8

import os, signal

print 'Process %s start...' % os.getpid()
pid = os.fork() # fork()方法返回两次结果，
if pid==0:
    print 'I am child process (%s) and my parent is %s.' % (os.getpid(), os.getppid())
    os.kill(os.getpid(),signal.SIGKILL) # 杀死子进程，否则下面的代码都会运行两次
else:
    print 'I (%s) just created a child process (%s).' % (os.getpid(), pid)



# 创建子进程，并等待子进程结束。
from multiprocessing import Process
import os

# 子进程要执行的代码
def run_proc(name):
    print 'Run child process %s (%s)...' % (name, os.getpid())

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Process(target=run_proc, args=('test',))
    print 'Process will start.'
    p.start() #创建子进程时，只需要传入一个执行函数和函数的参数，创建一个Process实例，用start()方法启动，
                # 这样创建进程比fork()还要简单。 join()方法可以等待子进程结束后再继续往下运行，通常用于进程间的同步。
    p.join()
    print 'Process %s end.' % os.getpid()

# 启动大量多进程，进程池。
from multiprocessing import Pool
import time, random

def long_time_task(name):
    print 'Run task %s (%s)...' % (name, os.getpid())
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print 'Task %s runs %0.2f seconds.' % (name, (end - start))

if __name__=='__main__':
    print 'Parent process %s.' % os.getpid()
    p = Pool()
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print 'Waiting for all subprocesses done...'
    p.close()
    p.join()
    print 'All subprocesses done.'

# 进程间通信：
from multiprocessing import Queue

# 写数据进程执行的代码:
def write(q):
    for value in ['A', 'B', 'C']:
        print 'Put %s to queue...' % value
        q.put(value)
        time.sleep(random.random())

# 读数据进程执行的代码:
def read(q):
    while True:
        value = q.get(True)# TRUE，使这个进程阻塞在这里。
        print 'Get %s from queue.' % value

if __name__=='__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    pw = Process(target=write, args=(q,))
    pr = Process(target=read, args=(q,))
    # 启动子进程pw，写入:
    # pw.start()
    # 启动子进程pr，读取:
    pr.start()
    # 等待pw结束:
    pw.join()
    # pr进程里是死循环，无法等待其结束，只能强行终止:
    pr.terminate()

'''在Unix/Linux下，可以使用fork()调用实现多进程。

要实现跨平台的多进程，可以使用multiprocessing模块。

进程间通信是通过Queue、Pipes等实现的。'''

