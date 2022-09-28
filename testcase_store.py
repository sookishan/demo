#!/usr/bin/env python
# -*- coding:utf-8 -*-
import yaml

from step import Step


class TestCaseStore:
    def __init__(self):
        self.test_params = {}
        self.testcase = {}

    def load(self, path):
        with open(path) as f:
            methods = yaml.load(f)
        for mothod_name, steps in methods.items():
            step_method = []
            for step in steps:
                step_method.append(Step(step))
            if method_name.startswith("test_"):
                self.test_params[method_name] = step_method
        self.testcase_gen()

    def testcase_gen(self):
        """根据params生成多个testcase"""
        self.testcase = self.test_params
