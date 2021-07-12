

# coding=utf-8
# authou:shichao

import pytest 
from selenium import webdriver
import time

driver = webdriver.Chrome()


@pytest.fixture(scope="module", autouse=True)
def setup_class():
    print("\n>>>scope=”module“类型为module针对全局文件有效, autouse=True，状态为开启，自动调用方式，执行setup；例如：打开浏览器，并且打开百度首页")
    driver.maximize_window()
    time.sleep(1)
    URL = "https://www.baidu.com/"
    driver.get(URL)

    # 用yield关键字呼唤teardown操作
    yield
    print("\n>>>scope=”module“类型为module针对全局文件有效, autouse=True，状态为开启，自动调用方式，执行teardown;例如：最后关闭浏览器")
    driver.quit()


@pytest.fixture(scope="function", autouse=False)
def setup_funtion():
    print("\n>>>scope=”function“类型为function只针对函数有效, autouse=False，为关闭状态，手动调用方式；例如做：点击首页操作等")
    time.sleep(2)


def testcase001():
    print("\n>>>执行测试用例1")
    driver.find_element_by_id("kw").send_keys(u"软件测试")
    driver.find_element_by_xpath('//*[@id="su"]').click()


def testcase002(setup_funtion):
    print("\n>>>执行测试用例2")


if __name__ == '__main__':
    pytest.main(["-s", "test_fix_yield.py"])