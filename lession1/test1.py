


l = [1,2,3,True,2]

print l

print l.count(2)

print len(l)

print type('ag')

for m in [0, len(l)-1]:
    print l[m]


d = {'a':1, 'b':2}
print type(d['a'])

class dd():
    '''description of dd'''
    def __init__(self):
        pass
    def say(self):
        pass
    
    def __str__(self):
        return 'my name is dd'

d = dd()

def foo(d):
    print d
    print type(d)
    print dir(d)
    print help(d)

foo(d)

#传参
def foo1():
    print 'no args'

def foo1(s):
    print 'one args'

def foo1(s, s2):
    print s, s2

def foo1(s, s2 = None):
    print s, s2

# 动态参数 kw 位置参数列表； kws 默认参数列表
def foo1(*kw, **kws):
    print kw
    print kws

foo1(1,2,3,4, s = 1, s2 = 3)

# 查看内建函数
print dir(__builtins__)

print 'test'