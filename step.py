#!/usr/bin/env python
# -*- coding:utf-8 -*-
import importlib
import inspect
from context_base import ContextBase


class Step(ContextBase):
    def __init__(self, step: dict):
        self._step = step
        self._params = None
        self._object_name = ""
        self._package_name = ""
        self._method_name = ""

    def run(self):
        for key, value in self._step.items():
            class_method = str(key).split(".")
            if len(class_method) >= 2:
                self._package_name = '.'.join(class_method[0:-2])
                self._object_name = class_method[-2]
                self._method_name = class_method[-1]
            # print()
            elif len(class_method) == 1:
                self._method_name = class_method[0]
            self._params = value
        class_object = self.object_get()
        method_object = self.method_get(class_object)
        return self.method_run(method_object)

    def object_get(self):
        if self._object_name in [[], '']:
            return self
        else:
            param_dict = self.get_param_dict()
            if self._object_name in param_dict and self._package_name == '':
                return param_dict[self._object_name]
            else:
                # sys.path.append()
                # mtf.core.testcase.TestCase()
                if self._package_name == '':
                    # random.random()
                    self._package_name = self._object_name
                else:
                    self._package_name = '.'.join([self._package_name, self._object_name])
                self._object_name = ''
                # 动态导入某个包
                name_list = self._package_name.split('.')

                def find(index):
                    package_name = '.'.join(name_list[0:index+1])
                    package_target = importlib.import_module(package_name)
                    importlib.invalidate_caches()
                    globals()[package_name] = package_target
                    if len(name_list) == index + 1:
                        return  package_target
                    else:
                        object_name = name_list[index+1]
                        if hasattr(package_target, object_name):
                            object_target = getattr(package_target,object_name)
                            if inspect.ismodule(object_target):
                                return find(index+1)
                            else:
                                return object_target
                        else:
                            return find(index+1)
                package_target = find(0)
                return package_target

    def get_param_dict(self):
        """
         依次查找locals param data() glabals
        :return:
        """
        param_dict = globals()
        param_dict.update(locals())
        return param_dict

    def method_get(self, class_object):
        """
        找方法
        :param class_object:
        :return:
        """
        # 方法获取
        if hasattr(class_object, self._method_name):
            return getattr(class_object, self._method_name)
        # 支持print等内置函数
        elif self._method_name in globals()['__builtins']:
            return globals()['__builtins__'][self._method_name]

    def save(self, var_name):
        return self._return(var_name)

    def _return(self, var_name=None):
        res = self.get_context().return_value()
        if var_name is not None:
            globals()[var_name] = res
        return res

    def update_param(self, data, param_dict):
        """
        获取参数并进行模板替换，支持多参数列表与命名参数
        :param data:
        :param param_dict:
        :return:
        """
        def recursion(d):
            if isinstance(d, list):
                return [recursion(l) for l in d]
            elif isinstance(d, dict):
                return {k: recursion(v) for k, in d.items()}
            elif isinstance(d, str):
                if d.startswith('$(' and d.endswith(')')):
                    return eval(d[2:-1], param_dict)
                else:
                    return d
        return recursion(data)
