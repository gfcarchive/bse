# -*- coding: utf-8 -*-

import pytest  # type: ignore
from bse import mod
from bse import path
from schema import SchemaError  # type: ignore


@pytest.mark.parametrize("script", [path.join("samples", "lua_webbanking_ok.lua")])
def test_webbanking_ok(script: str) -> None:
    script = path.join(path.here(__file__), script)
    m = mod.LuaMod(script)
    assert m.version == 1.0
    assert m.url == "https://www.mysite.com"
    assert m.description == "Service Description"
    assert m.name == "Service Name"
    assert m.slug == "lua_webbanking_ok"


@pytest.mark.parametrize(
    "script",
    [
        path.join("samples", "lua_webbanking_no_description.lua"),
        path.join("samples", "lua_webbanking_no_url.lua"),
        path.join("samples", "lua_webbanking_no_version.lua"),
        path.join("samples", "lua_webbanking_no_services.lua"),
    ],
)
def test_missing_global(script: str) -> None:
    script = path.join(path.here(__file__), script)
    with pytest.raises(SchemaError):
        mod.LuaMod(script)
