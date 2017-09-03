
# 列表推导式（list comprehension)

# , 可以让print打印多个表达式
print 'age', 23

x = 12, y = 23
x,y = y,x 
print x, y

# 把某件事从另一个文件中导入
 from somemodule import somefunction

from somemodule import *

#如果两个模块都有open函数，就需要像下面这样使用函数

module1.open(...)
module2.open(...)

# 或，在语句末尾增加一个as子句，在该as子句后给出的名字，将
# 成为整个模块的别名
import math as foobar
foobar.sqrt(4)

# 同样可以为函数提供别名
from math import sqrt as foobar
foobar(9)

#序列解包（sequence unpacking），可选代解包
x,y,z = 1,2,3
print x, y, z

x,y = y,x
print x, y

scoundrel = {'name':'robin', 'girlfriend':'marion'}
key, value = scoundrel.popitem()
print key, value

# 需要注意的是，所解包的序列中的元素数量必须和放置在赋值符号=左边的变量数量
# 完全一致，否则python会赋值时引发异常

# 一些迭代工具

# 1， 并行迭代
names = ['amen', 'bech', 'agei', 'demo']
ages = [12,34,12,15]

#zip函数可以用来进行并行迭代；可以把两个序列‘压缩’在一起；
zip(names, ages)
for name, age in zip(names, ages):
    print name, 'is', age, 'years old'

# zip函数可以作用于任意多的序列。关于它很重要的一点是zip可以应付不等长的序列
# 当最短的序列‘用完’的时候就会停止
zip(range(5), xrange(10000000))

# 2, 编号迭代

for index, string in enumerate(strings):
    if 'xxx' in string:
        strings[index] = '[censored]'

# 3,翻转和排序迭代




