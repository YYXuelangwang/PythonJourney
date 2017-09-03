
# repr 会创建一个字符串，它会以合法的python表达式的形式来表示值

print repr('this is my ma ')
print repr(1000L)

print str('hello this is my classmate')
print str(10000L)

# ` （反引号，而不是单引号）的使用如下,打印一个包含数字的字符串
temp = 34
# print 'the temperature is ' + temp  error（不能直接将字符串和数字相加）
print 'the temperature is ' + `temp`

x,y = 12, 23
x, y = y,x
print x, y

# input 会假设用户输入的是合法的python表达式（或多或少有些与repr函数相反的意思），
# raw_input 会把所有的输入当做原始数据（raw data)，然后将其放入字符串中

name = input('what is your name') #如果用户输入 jack 会导致程序报错，如果用户输入 "jack",程序正常运行
print 'Hello ' + name +'!'

name = raw_input('what is your name') #这里不会有上面的问题，不管用户怎么输入都不会报错
print 'hello' + name + '!'

# 1，长字符串, 使用三个引号 '''或者"""

print ''' this is a very long sting,
it continues here.abs
and  ite's not over yet
'hello workd'  \   
still here.'''

# 上面的一个反斜线\, 导致换行符本身就“转义"了，也就忽略了换行



