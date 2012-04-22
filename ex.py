__author__ = 'Siglud'
# -*- coding: utf-8 -*-
 
def find_greatest_common_divisor(x, y):
    '''查找最大公约数函数
 
    根据计算机程序设计艺术中第一节的算法来求最大公约数'''
    temp = x > y and x%y or y%x
    print("x= %d  y=%d  temp= %d") %(x, y, temp) # added by Tom Xue

    if temp == 0:
        return x > y and y or x
    else:
        if (x > y):
            return find_greatest_common_divisor(y,temp)#此处一定要有Return,否则还会执行一轮
        else:
            return find_greatest_common_divisor(x,temp)
 
x = input("请输入x的值:")
y = input("请输入y的值:")
 
print(find_greatest_common_divisor(int(x),int(y)))
