#!/usr/bin/env python
# -*- coding:utf-8 -*-
from threading import lock


# Building：单例类，饿汉模式
class Building:
    # python的类变量会被多个类、实例共享
    __id = 0
    __instance = None  # 类属性

    # cls指当前类
    def __new__(cls):
        cls.__id += 1
        print(f"创建弟{cls._id}个对象，分配空间(指定地址)")  # 1.创建对象时，new方法会先被调用
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)  # 2.为对象分配空间：父类的__new__，参数接受一个类名，会返回类的实例
        return cls.__instance  # 3.返回对象的引用，必须得有这个返回，不然self找不到对象（即没有实例化）

    def __init__(self):  # 初始化方法；对这个实例化对象再次加工
        print(f"开始盖第{self.__id}座楼")
        print(f"地址是：{id(self)}")


# LBuilding：单例类，懒汉模式
class LBuilding:
    # python的类变量会被多个类、实例共享
    _id = 0
    _instance = None

    # cls指当前类
    def __new__(cls):
        cls._id += 1
        print(f"创建弟{cls._id}个对象，分配空间(指定地址)")  # 1.创建对象时，new方法会先被调用
        if cls._instance is None:
            cls._instance = super().__new__(cls)  # 2.为对象分配空间：父类的__new__，参数接受一个类名，会返回类的实例
        return cls._instance  # 3.返回对象的引用，必须得有这个返回，不然self找不到对象（即没有实例化）

    def __init__(self):  # 初始化方法；对这个实例化对象再次加工
        print(f"开始盖第{self._id}座楼")
        print(f"地址是：{id(self)}")


if __name__ == "__main__":
    build1 = LBuilding()
    build2 = LBuilding()

