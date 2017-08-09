#encoding:utf-8

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
        list = filter(_not_divisible(n), list) # 构造新序列,第一个参数实际代表def（x）:x % n > 0

# for n in primes():
#     if n < 1000:
#         print(n)
#     else:
#         break

for x in _odd_iter():
    if x > 1000:
        break;
    else:
        print x

it = _odd_iter()
print next(it)
print next(it)
print next(it)