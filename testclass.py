# import pytest

#class TestClass:
import pytest
import yaml


def func(x):
    return x+1

# 参数化
@pytest.mark.parametrize(('a','b'),yaml.safe_load(open('./data.yaml')))
def test_answer(a,b):
    assert func(a)==b

def test_answer1():
    assert func(4)==5

@pytest.fixture() #装饰器
def login():
    print('登录操作')
    username='jerry'
    return username

class TestDome():
    def test_a(self,login):
        print(f'a username={login}')

    def test_b(self):
        print('b')

if __name__=='__main__':
    pytest.main(['testclass.py::TestDome::test_a'])