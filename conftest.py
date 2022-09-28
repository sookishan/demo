#!/usr/bin/env python
# -*- coding:utf-8 -*-
# 通过钩子函数,pytest在收集完所有测试项后调用这个钩子,items就是所有的用例合集
def pytest_collection_modifyitems(session, config, items):
    for item in items:
        item.name = item.name.encode("utf-8").decode("unicode_escape")
        # print(item.nodeid)
        item._nodeid = item.nodeid.encode("utf-8").decode("unicode_escape")


# 具体作用可参考:https://docs.pytest.org/en/latest/reference/reference.html#_pytest.hookspec.pytest_addhooks
def pytest_addoption(parser):
    parser.addoption(
        "--stringinput",
        action="append",
        default=[],
        help="list of stringinputs to pass to test functions",
    )


# 具体参考:https://docs.pytest.org/en/latest/how-to/parametrize.html#pytest-generate-tests
def pytest_generate_tests(metafunc):
    if "stringinput" in metafunc.fixturenames:
        metafunc.parametrize("stringinput", metafunc.config.getoption("stringinput"))

