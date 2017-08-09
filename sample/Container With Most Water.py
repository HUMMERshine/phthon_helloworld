#encoding:utf-8

height = range(1, 15001)
print len(height)

def method1(height):
    pro = 0
    for i in range(0, len(height)):
        for j in range(i + 1, len(height)):
            if j > i:
                temp = (j - i) * (height[j] - height[i])
                pro = max(pro, temp)
    print "<<<", pro

method1(height)
