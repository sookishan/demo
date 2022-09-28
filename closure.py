#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
闭包函数的实例：
outer是外部函数，a和b都是外部函数的临时变量
"""


# def outer(a):
#     b = 10
#
#     # inner是内函数
#     def inner():
#         # 在内函数中 用到了外函数的临时变量
#         print(a+b)
#     return inner

def outer(x):
    print(f'外部变量x等于{x}')
    print(id(x))

    def inner(y):
        print(f'内部变量y等于{y}')
        print(id(y))
        nonlocal x
        x += y
        print(f'相加等于{x}')
        return x
    return inner


def outer2(a):
    print(f'外部变量x等于{a}')
    print(id(a))

    def inner(b):
        print(f'内部变量y等于{b}')
        print(id(b))
        c = 10
        print(id(c))
        b += c
        print(f'相加等于{b}')
        return b
    return inner


if __name__ == '__main__':
    demo = outer2(5)
    # demo(3)
    print(f"变量函数地址：{id(demo)}")
    print(f"对象实例化地址：{id(demo(3))}")
    print(f"对象实例化地址：{id(demo(7))}")
    # demo(7)

    # demo2 = outer(7)
    # demo2()


