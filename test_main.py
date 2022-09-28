#!/usr/bin/env python
# -*- coding:utf-8 -*-
import pytest
from context import Context


class TestMain:
    context = Context()
    context.load("./tmp.yml")

    @pytest.mark.parametrize("testcase", context.store.testcase.values(), ids=context.store.testcase.key())
    def test_main(self, testcase):
        self.context.run_steps_by_testcase(testcase)
