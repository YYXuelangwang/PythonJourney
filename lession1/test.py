

# encoding  : utf-8

#__author__ = 'macy'

# 格式是缩进和空格：
def foo():
    print 'hello world'
    if (True):
        print 'hello macy'

# python是解释性语言且具有强类型转换的能力，所以python中变量不需要声明
# 变量名与变量类型；而是直接给变量赋值即可
# 另外python是大小写区分的，变量a和变量A不是一回事
s = 1
print type(s)
ss = '1'
s = None
print type(s)
s = True
s = False
s = 10L
print type(s)

# False: {}, False, [], (), None, 0, ''

def foo1():
    a = 10
    if (a>10):
        print 'hello 10+'
    elif 5<a<10:
        print 'hello 5+'
    else:
        print 'hello low'

l = [1,23]
for i in l:
    print i

for i in range(100):
    print i

a = 0
while a < 5:
    print a
    a = a + 1

def foo2(x, y):
    print x, y
    return x+y

print foo2(1,2)

#python 中的匿名函数
ss = lambda x, y: x+y
print ss(2,3)

#定义一个python的类
class Foo(object):
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def do(self):
        print self.name
        print self.age


