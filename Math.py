# coding=utf-8
# !/usr/bin/env python

print ("-----------------输出0~100的偶数------------------")
# 定义初始值
start = 1
while True:
    if start == 51:
        break
    print  start * 2
    start += 1
print ("-----------------输出0~100的奇数------------------")
# 定义初始值
start = 1
while True:
    if start == 100:
        break
    # %运算是取余数
    if start % 2 == 1:
        print start
    start += 1
