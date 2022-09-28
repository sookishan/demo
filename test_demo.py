#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest


# 没有传ids的,默认用参数值
@pytest.mark.parametrize("x, y", [(0, 1), (2, 3), (4, 5)])
def test_demo01(x, y):
    pass


# 传入了ids的,使用ids中的名称
@pytest.mark.parametrize("x, y", [(0, 1), (2, 3), (4, 5)], ids=("第一次", "第二次", "第三次"))
def test_demo02(x, y):
    pass









