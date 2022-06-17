# -*- coding: utf-8 -*-
# @Author    : XieLiLi
# @Time      : 2022/6/12 0012 12:43
# @Function  :
from datetime import datetime
from typing import List
from func.calculator import Calculator
import pytest
import yaml

#测试用例中文转码
def pytest_collection_modifyitems(
    session: "Session", config: "Config", items: List["Item"]
) -> None:
    #print(items)
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item._nodeid.encode('utf-8').decode('unicode-escape')


#动态生成日志名字
@pytest.fixture(scope="session", autouse=True)
def manage_log(request):
    """set log file name as logs/<日期_时间>.log"""
    #先获取当前时间
    now = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
    #在字符串拼接文件名字及路径
    log_name = 'output/log/' + now + '.logs'

    request.config.pluginmanager.get_plugin("logging-plugin") \
        .set_log_path(log_name)


#获得计算器对象
@pytest.fixture(scope="class")
def get_clac():
    clac = Calculator()
    yield clac
    print("测试结束")

@pytest.fixture(autouse=True)
def clac_fix():
    print("开始计算")
    yield
    print("结束计算")