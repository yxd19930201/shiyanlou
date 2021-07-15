import pytest
import yaml

class TestDome:
    @pytest.mark.parametrize("env",yaml.safe_load(open("./env.yml")))
    def test_dome(self,env):
        if "test" in env:
            print("测试环境ID",env["test"])
        elif "dev" in env:
            print("开发环境ID",env["dev"])