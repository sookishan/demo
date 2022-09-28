#!/usr/bin/env python
# -*- coding:utf-8 -*-
from context_base import ContextBase


class TestCase(ContextBase):
    def __int__(self, steps, context):
        self.steps = steps
        self._context = context

    def run_steps(self):
        self.get_context().run_steps(self.steps)
