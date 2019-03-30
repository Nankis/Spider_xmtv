# -*- coding: utf-8 -*-
__author__ = 'Ginseng'
import re

"""
<div class="video-info">([\s\S]*?)</div>  取<div class="video-info"></div>内的所有内容

概括字符集
\d   表示所有数字   等价[0-9]
\D   表示非数字字符    等价[^0-9]
\w   匹配数字,字母和下划线  类似但不等价于[A-Za-z0-9_]
\W   匹配任何非单词字符,  等价于 [^A-Za-z0-9_]   ===>匹配 空格& \r \n 等等
\s   匹配任何不可见字符(空白字符)，包括空格、制表符、换页符等等。等价于[ \f\n\r\t\v]
\S   匹配任何可见字符。等价于[^ \f\n\r\t\v]
.    匹配换行符\n职位的其他所有字符

数量词

一.  
a = 'python 1111java2345php'
r = re.findall('[a-z]{3,6}',a)
{3,6}匹配前面的3-6 
默认贪婪模式, 贪婪模式取界线的最大值, 非贪婪模式取界线的最小值

二 .
# * 星号对前面的字符匹配 匹配0次或无限多次
# + 加号对前面的字符匹配 匹配1次或无限多次
# ? 问号对前面的字符匹配 匹配0次或1次   注意与{}中的贪婪模式区别  ?前面是范围则是非贪婪模式   ?前面不是范围则是匹配0次或1次

三.
边界匹配
^和$

四.
组  () 一个括号代表一组 # 注意区别[], [] 是或关系 () 是且关系

"""

# a = 'C0C++7Java8C#8Python9Javascript'
# r = re.findall('acc', a)  # 第一个参数是正则表达式,第二个是要匹配的字符  结果会返回列表

# a = 'abc,acc,adc,aec,afc,ahc'
# r = re.findall('a[cf]c', a)  # 匹配出a*c中间为c或者f的字符 1.普通字符用来作为定界,出现在[]里的字符是或的关系
# r = re.findall('a[^cf]c', a)  # 匹配出中间不是c或者f的字符
# r = re.findall('a[c-f]c', a)  # 匹配出中间是c-f的任意1个字符 等价于a[cdef]c


# a = 'pythonp 1111java2345php'
# 默认贪婪模式即,以能匹配到6次就优先匹配到6次 比如 jav已经满足了3次了,但是贪婪模式会继续匹配
# r = re.findall('[a-z]{3,6}', a)  # 匹配3-6次,贪婪模式尽可能匹配6次
# print(r)
#
# a2 = 'pythonp 1111java2345php'
# r2 = re.findall('[a-z]{3,6}?', a2)  # 末尾加?非贪婪模式 即等价于 [a-z]{3}
# print(r2)


# * 星号对前面的字符匹配 匹配0次或无限多次
# + 加号对前面的字符匹配 匹配1次或无限多次
# ? 问号对前面的字符匹配 匹配0次或1次
a3 = 'pytho0python1pythonn2'
# r3 = re.findall('python*', a3)  # 第一个pytho中*前面的n出现了0次 符合  第三个pythonn中*前面的n出现了2次  符合
r3 = re.findall('python+', a3)  # 第一个pytho中+前面的n出现了0次 不符合  第三个pythonn中+前面的n出现了2次  符合
# 关于*号和+号的理解,如'python+'中,应该先匹配pytho  然后再考虑n+或者n*
# print(r3)

a4 = 'pytho0python1pythonn2'
# 第三个pythonn中先匹配pytho   然后再匹配n?由于出现了一次n满足条件所以直接去掉后面多余的n  问号匹配通常可以用来去重
r4 = re.findall('python?', a4)
# print(r4)


qq = '100000001'
r5 = re.findall('\d{4,8}', qq)  # 检测4~8的QQ号
# print(r5)

a6 = '100000001'
r6 = re.findall('001$', a6)  # ^和$为边界占位符 ^从左往右依次匹配,$从末尾往左匹配.本例子就是匹配从右往左数是100的
# print(r6)

a7 = 'PythonPythonPythonPythonPython'
r7 = re.findall('(Python){3}', a7)
# print(r7)

a8 = 'PythonC#\nJavaPHP'
# r8 = re.findall('c#', a8, re.I)  # 第三个参数:re.I 忽略大小写匹配 ,多个模式之间用|衔接,注意,此处|不是或关系,是且的关系
r8 = re.findall('c#.{2}', a8, re.I | re.S)  # .代表\n外的任意字符  re.S 代表可以匹配所有字符,包括\n


# print(r8)


def convert(value):
    """
    函数模式匹配可以进行动态匹配,然后返回不同的匹配结果
    :param value:
    :return:
    """
    matched = value.group()  # 对象可以通过.group方法取到值
    # 如果是通过search或者match匹配的,则可以给group()传入组号,获取对应组的值
    # 此时接收到的value是一个对象
    # print(value)
    return "!!" + matched + "!!"


a9 = 'PythonC#JavaC#PHPC#'
# r9 = re.sub('C#', 'GO', a9, 0)  # 将C# 替换成GO 第四个参数是替换个数,默认是0  0代表所有的C#都会被替换
r9 = re.sub('C#', 'GO', a9, 2)  # 2代表从左到右依次替换,只替换2次---即替换的最大次数

# print("str内置函数的替换:\n", a9.replace("C#", "GO"))  # 注意字符串不可改变,要用新的变量来接收替换后的结果
# print(r9)

# re.sub的第二个参数可以接收函数,注意,该函数必须要可以接收参数,因为当sub匹配到结果时,会把匹配的值传到该函数,
# 而返回的值也是由函数调用后得的 而且此时的函数只要写函数名既可,不是调用函数.
r9_ = re.sub('C#', convert, a9)


# print(r9_)

def getnum(value):
    """
    动态匹配,动态返回
    :param value:
    :return:
    """
    num = value.group()
    num = int(num)
    if num <= 5:
        num = 0
    else:
        num = 1
    return "-" + str(num)


a10 = 'A8C3721D86'
r10 = re.sub('\d', getnum, a10)
# print(r10)


a11 = 'A8C3721D86'
# 从字符串的首字母开匹配,如果匹配不到数字就直接返回  因为a11的开头不是数字,所以没有匹配到结果
r11 = re.match('\d', a11)  # 可通过group()方法拿到匹配到的值,可以给group()传入组号,获取对应组的值,通过span()拿到匹配的位置
# print(r11)

# search从左往右查找字符串,一旦查找到满足匹配的结果,则返回目标所在的位置
# 如span=(1,2) 代表位置1之后(不包括1)才是匹配的结果,直到2(包括2)
r11_ = re.search('\d', a11)  # 可通过group()方法拿到匹配到的值,可以给group()传入组号,获取对应组的值,通过span()拿到匹配的位置
# print(r11_, "匹配到的下标:", r11_.span())

# 查找并且以列表格式返回所有符合结果
r11__ = re.findall('\d', a11)
# print(r11__)


a12 = 'life is short,i use python'  # 获取life和python之间的所有字符
a12a = 'life is short,i use python,i love python'  # 获取life和python之间的所有字符,同时获取末尾两个python之间的所有字符
r12 = re.search('life(.*)python', a12)
# print(r12.group(1))  # 组号为0则是所有的组的结果,因此想要获得对应组号应该从1开始数

r12_ = re.findall('life(.*)python', a12)
# print(r12_)

# 多组匹配
# r12r = re.findall('life(.*)python(.*)python', a12a)
# print(r12r)

r12r = re.search('life(.*)python(.*)python', a12a)
# print(r12r.group(0))  #
# print(r12r.group(1))  # 第一组匹配结果
# print(r12r.group(2))  # 第二组匹配结果
# print(r12r.group(0, 1, 2))  # 通过元祖返回所有结果
# print(r12r.groups())  # 只返回匹配到所有组的结果 等价于 r12r.group(1,2)
