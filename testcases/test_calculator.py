# -*- coding: utf-8 -*-
# @Author    : XieLiLi
# @Time      : 2022/6/12 0012 12:37
# @Function  :
import logging
import allure
import pytest
import yaml


def get_datas(type_name, level):
    """  get datas from the calc_data.yaml
    :param type_name:   "add"  "div"
    :param level:       "P0"  "P1_1"  "P1_2"  "P2"
    :return:    {'add_P0_datas': [], 'add_P0_ids': []}
    """
    with open('../datas/calc_data.yaml', encoding='utf-8') as f:
        result = yaml.safe_load(f)
        calc_datas = result.get(type_name).get(level).get('datas')
        calc_ids = result.get(type_name).get(level).get('ids')
        # print(calc_datas)
        # print(calc_ids)
    return {f'{type_name}_{level}_datas': calc_datas, f'{type_name}_{level}_ids': calc_ids}

@allure.feature("计算器测试用例")
class TestCalculator():

    #获取加法测试用例数据

    add_P0_datas = get_datas('add', 'P0').get("add_P0_datas")
    add_P0_ids = get_datas('add', 'P0').get("add_P0_ids")

    add_P1_1_datas = get_datas('add', 'P1_1').get("add_P1_1_datas")
    add_P1_1_ids = get_datas('add', 'P1_1').get("add_P1_1_ids")

    add_P1_2_datas = get_datas('add', 'P1_2').get("add_P1_2_datas")
    add_P1_2_ids = get_datas('add', 'P1_2').get("add_P1_2_ids")

    add_P2_datas = get_datas('add', 'P2').get("add_P2_datas")
    add_P2_ids = get_datas('add', 'P2').get("add_P2_ids")

    #获取除法测试用例数据
    div_P0_datas = get_datas('div', 'P0').get("div_P0_datas")
    div_P0_ids = get_datas('div', 'P0').get("div_P0_ids")

    div_P1_1_datas = get_datas('div', 'P1_1').get("div_P1_1_datas")
    div_P1_1_ids = get_datas('div', 'P1_1').get("div_P1_1_ids")

    div_P1_2_datas = get_datas('div', 'P1_2').get("div_P1_2_datas")
    div_P1_2_ids = get_datas('div', 'P1_2').get("div_P1_2_ids")

    div_P2_datas = get_datas('div', 'P2').get("div_P2_datas")
    div_P2_ids = get_datas('div', 'P2').get("div_P2_ids")



    #加法测试用例
    @allure.story("加法 - P0冒烟测试")
    @pytest.mark.P0
    @pytest.mark.parametrize("num1, num2, expected", add_P0_datas, ids=add_P0_ids)
    def test_add_P0(self, get_clac, num1, num2, expected):
        logging.info(f"参数： {num1}, {num2}  预期结果： {expected}")
        with allure.step("步骤1： 两个数相加"):
            result = get_clac.add(num1, num2)
            logging.info(f"实际结果： {result}")
        with allure.step("步骤2： 验证结果"):
            assert result == expected


    @allure.story("加法 - P1_1边界值测试")
    @pytest.mark.P1_1
    @pytest.mark.parametrize("num1, num2, expected", add_P1_1_datas, ids=add_P1_1_ids)
    def test_add_P1_1(self, get_clac, num1, num2, expected):
        logging.info(f"参数： {num1}, {num2}  预期结果： {expected}")
        with allure.step("步骤1： 两个数相加"):
            result = get_clac.add(num1, num2)
            logging.info(f"实际结果： {result}")
        with allure.step("步骤2： 验证结果"):
            assert result == expected


    @allure.story("加法 - P1_2特殊字符测试")
    @pytest.mark.P1_2
    @pytest.mark.parametrize("num1, num2, errortype", add_P1_2_datas, ids=add_P1_2_ids)
    def test_add_P1_2(self, get_clac, num1, num2, errortype):
        logging.info(f"参数： {num1}, {num2}  预期异常： {errortype}")
        with pytest.raises(eval(errortype)) as e:
            with allure.step("步骤1：两个数相加"):
                result = get_clac.add(num1, num2)
        logging.info(f"实际异常： {e.typename}")


    @allure.story("加法 - P2空值和空格测试")
    @pytest.mark.P2
    @pytest.mark.parametrize("num1, num2, errortype", add_P2_datas, ids=add_P2_ids)
    def test_add_P2(self, get_clac, num1, num2, errortype):
        logging.info(f"参数： {num1}, {num2}  预期异常： {errortype}")
        with pytest.raises(eval(errortype)) as e:
            with allure.step("步骤1：两个数相加"):
                result = get_clac.add(num1, num2)
        logging.info(f"实际异常： {e.typename}")



    #除法测试用例
    @allure.story("除法 - P0冒烟测试")
    @pytest.mark.P0
    @pytest.mark.parametrize("num1, num2, expected", div_P0_datas, ids=div_P0_ids)
    def test_div_P0(self, get_clac, num1, num2, expected):
        logging.info(f"参数： {num1}, {num2}  预期结果： {expected}")
        try:
            with allure.step("步骤1： 两个数相除"):
                result = get_clac.div(num1, num2)
                logging.info(f"实际结果： {result}")
            with allure.step("步骤2： 验证结果"):
                assert result == expected
        except ZeroDivisionError as e:
            logging.info(f"实际异常： {e}")

            #其实这块这个异常我不确定是不是应该做特殊处理，因为源代码的确没有控制不能输入0啊



    @allure.story("除法 - P1_1边界测试")
    @pytest.mark.P1_1
    @pytest.mark.parametrize("num1, num2, expected", div_P1_1_datas, ids=div_P1_1_ids)
    def test_div_P1_1(self, get_clac, num1, num2, expected):
        logging.info(f"参数： {num1}, {num2}  预期结果： {expected}")
        with allure.step("步骤1： 两个数相除"):
            result = get_clac.div(num1, num2)
            logging.info(f"实际结果： {result}")
        with allure.step("步骤2： 验证结果"):
            assert result == expected



    @allure.story("除法 - P1_2特殊字符测试")
    @pytest.mark.P1_2
    @pytest.mark.parametrize("num1, num2, errortype", div_P1_2_datas, ids=div_P1_2_ids)
    def test_div_P1_2(self, get_clac, num1, num2, errortype):
        logging.info(f"参数： {num1}, {num2}  预期异常： {errortype}")
        with pytest.raises(eval(errortype)) as e:
            with allure.step("步骤1：两个数相除"):
                result = get_clac.div(num1, num2)
        logging.info(f"实际异常： {e.typename}")



    @allure.story("除法 - P2空值和空格测试")
    @pytest.mark.P2
    @pytest.mark.parametrize("num1, num2, errortype", div_P2_datas, ids=div_P2_ids)
    def test_div_P2(self, get_clac, num1, num2, errortype):
        logging.info(f"参数： {num1}, {num2}  预期异常： {errortype}")
        with pytest.raises(eval(errortype)) as e:
            with allure.step("步骤1：两个数相除"):
                result = get_clac.div(num1, num2)
        logging.info(f"实际异常： {e.typename}")

