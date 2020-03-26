#!/usr/bin/python
# -*- coding: UTF-8 -*-
# 装饰器的应用

__author__ = 'sphenginx'

def funA(fn):
    print("C语言中文网")
    fn() # 执行传入的fn参数
    print("http://c.biancheng.net")
    return "装饰器函数的返回值"

@funA
def funB():
    print("学习 Python")

if __name__ == '__main__':
	print(funB)

