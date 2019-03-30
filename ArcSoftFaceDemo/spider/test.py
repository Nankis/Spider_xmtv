# -*- coding: utf-8 -*-
__author__ = 'Ginseng'
import re

# a = '\n                 路西法         '
# rg = '[\w]*?'
# r = re.findall(rg, a)
# r2 = re.sub(' ', '', a)
# print(r)
# print(r2)


# '</i>([\s\S]*?)</span>'
a = '<i class="ricon ricon-eye"></i>17.7万'
rg = 'i>([\d\w\s\S]*)'
r = re.findall(rg, a)
# print(r)
a2 = '17.7万'
a3 = '1777'

# a2_rg = '[\d\s\S]*万$'
# a2r = re.findall(a2_rg, a2)
# a3r = re.findall(a2_rg, a3)
# print(a2r)
# print(a3r)


# def getnum(value):
#     v = value.group()
#     # re.sub('万', '', v)  # 17.7   17 7000
#     v = v.replace('万', '')
#     v = float(v) * 10000
#     return str(v)
#
#
# r2 = re.sub(a2_rg, getnum, a2)
# print(r2)


# a = '5.5万'
# b = '666'
# if '万' in a:
#     a = a.replace('万', '')
#     a = float(a) * 10000
#
# print(a)
a = "['317']"
rg = "['"

a = a.replace("['", '')
a = a.replace("']", '')
print(a)
print(r)
