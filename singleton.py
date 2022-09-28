#!/usr/bin/env python
# -*- coding:utf-8 -*-
"""
实现单例模式
"""


# 使用__new__方法实现
class Singleton(object):
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, '_instance'):
            orig = super(Singleton, cls)
        return cls._instance

