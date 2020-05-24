# -*- coding: utf-8 -*-

import pytest  # type: ignore
from bse import module, path
from glob import glob


@pytest.mark.parametrize(
    "script", glob(path.join(path.here(__file__), "luatests", "test*.lua"))
)
def test_lua_tests(script: str) -> None:
    script = path.join(path.here(__file__), script)
    module.LuaMod(script)
