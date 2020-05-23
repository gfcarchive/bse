# -*- coding: utf-8 -*-

import pytest  # type: ignore
from bse import mod, path, __version__
from glob import glob
from unittest import mock


@pytest.mark.parametrize("script", [path.join("samples", "lua_webbanking_ok.lua")])
def test_mod_init(script: str) -> None:
    script = path.join(path.here(__file__), script)
    m = mod.LuaMod(script)
    assert m.version == "1.0"
    assert m.url == "https://www.mysite.com"
    assert m.description == "Service Description"
    assert m.name == "Service Name"
    assert m.slug == "lua_webbanking_ok"


@pytest.mark.parametrize(
    "script", [path.join("samples", "lua_webbanking_no_description.lua")]
)
def test_missing_global(script: str) -> None:
    script = path.join(path.here(__file__), script)
    with pytest.raises(mod.ModError):
        mod.LuaMod(script)


@pytest.mark.parametrize("script", [path.join("samples", "lua_webbanking_min.lua")])
def test_default_global(script: str) -> None:
    script = path.join(path.here(__file__), script)
    m = mod.LuaMod(script)
    assert m.version == __version__
    assert m.url is None
    assert m.name == m.slug


@pytest.mark.parametrize("script", [path.join("samples", "lua_MM.lua")])
def test_mm(script: str) -> None:
    script = path.join(path.here(__file__), script)
    with mock.patch("time.sleep") as mockts:
        m = mod.LuaMod(script)
        g = m._luart.globals()
        #
        mockts.assert_called_once_with(1)
        #
        assert g.test_product_name == "BSE"
        assert g.test_product_version == __version__
        #
        assert g.test_localizetext == "This is a Test"
        #
        assert g.test_localizenumber1 == "1"
        assert g.test_localizenumber2 == "1.1"
        assert g.test_localizenumber3 == "1.23"
        #
        assert g.test_localizedate1 == "Mar 31, 2020, 3:24:28 PM"
        assert g.test_localizedate2 == "2020.03.31 AD at 15:24:28 UTC"
        #
        assert g.test_localizeamount1 == "1"
        assert g.test_localizeamount2 == "1.1"
        assert g.test_localizeamount3 == "1.1"
        assert g.test_localizeamount4 == "€1.10"
        assert g.test_localizeamount5 == "€1.10"
        #
        assert g.test_urlencode1 == "this%20is%20a%20test"
        assert g.test_urlencode2 == "this%20is%20a%20test"
        #
        assert g.test_urldecode1 == "this is a test"
        #
        assert g.test_encoded_str1 == "74657374"
        assert g.test_decoded_str1 == "test"
        assert g.test_base64_encode1 == "dGVzdA=="
        assert g.test_base64_decode1 == "74657374"
        #
        assert (
            g.test_sha512
            == "401779a9f6545849e11ec969949549ae41dd8dbdd4f133e21145a1ef6c1551e1a5302e8aac7ff9cf955d98000c6e532fd9f"
            + "193b39fa17695a2e650ec132f3140"
        )
        assert (
            g.test_sha256
            == "119e3f0d28cf6a92d29399d5787f90308b6b87670d8c2386ec42cb36e293b5c4"
        )
        assert g.test_sha1 == "1e0a5da7cf8d083e5d170db4e5cd03dc5b22d3fa"
        assert g.test_md5 == "27703945b9bceacb09546d2e103ad360"
        #
        assert g.test_hmac512 == (
            "1613e1de8845bf9d652ac7023b1b499fa975c5102c25557ea3d2bca8213aa20caa823aaed9a8f5cb5e3e2c1a8cbdf55b868923"
            + "19b5d356d70e05dc1fb0fbb813"
        )
        assert g.test_hmac384 == (
            "87cae1d0fe8fef5c3c2c0cfb9ca06d99b8a6267084308c41c73b2c2aa638b94f7c43c3ba62aeffb2cf909ccc987df13b"
        )
        assert (
            g.test_hmac256
            == "6e4e506a08fff48f42d4754ddebfbdaa61619ecbc3828eb2b4dda99f94875396"
        )
        #
        assert len(str(g.test_time)) == 10  # length for timestamp


@pytest.mark.parametrize(
    "script",
    [
        path.join("samples", "lua_MM_localized_date_error.lua"),
        path.join("samples", "lua_MM_localized_number_error.lua"),
        path.join("samples", "lua_MM_localized_amount_error.lua"),
    ],
)
def test_mm_error(script: str) -> None:
    script = path.join(path.here(__file__), script)
    with pytest.raises(mod.ModError):
        mod.LuaMod(script)


@pytest.mark.parametrize(
    "script", glob(path.join(path.here(__file__), "luatests", "test*.lua"))
)
def test_lua_tests(script: str) -> None:
    script = path.join(path.here(__file__), script)
    mod.LuaMod(script)
