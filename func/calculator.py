# -*- coding: utf-8 -*-
# @Author    : XieLiLi
# @Time      : 2022/6/12 0012 12:35
# @Function  : 被测函数

class Calculator:

    def add(self, a, b):

        if a > 99 or a < -99 or b >99 or b < -99:
            print("请输入范围为[-99, 99]的整数或浮点数")
            return "参数大小超出范围"

        return a + b

    def div(self, a, b):

        if a > 99 or a < -99 or b > 99 or b < -99:
            print("请输入范围为[-99, 99]的整数或浮点数")
            return "参数大小超出范围"

        return a / b