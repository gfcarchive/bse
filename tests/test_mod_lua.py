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
            == "401779A9F6545849E11EC969949549AE41DD8DBDD4F133E21145A1EF6C1551E1A5302E8AAC7FF9CF955D98000C6E532FD9F193B"
            + "39FA17695A2E650EC132F3140"
        )
        assert (
            g.test_sha256
            == "119E3F0D28CF6A92D29399D5787F90308B6B87670D8C2386EC42CB36E293B5C4"
        )
        assert g.test_sha1 == "1E0A5DA7CF8D083E5D170DB4E5CD03DC5B22D3FA"
        assert g.test_md5 == "27703945B9BCEACB09546D2E103AD360"
        #
        assert (
            g.test_hmac512
            == (
                "1613e1de8845bf9d652ac7023b1b499fa975c5102c25557ea3d2bca8213aa20caa823aaed9a8f5cb5e3e2c1a8cbdf55b86892"
                + "319b5d356d70e05dc1fb0fbb813"
            ).upper()
        )
        assert (
            g.test_hmac384
            == "87cae1d0fe8fef5c3c2c0cfb9ca06d99b8a6267084308c41c73b2c2aa638b94f7c43c3ba62aeffb2cf909ccc987df13b".upper()
        )
        assert (
            g.test_hmac256
            == "6e4e506a08fff48f42d4754ddebfbdaa61619ecbc3828eb2b4dda99f94875396".upper()
        )
        #
        assert len(str(g.test_time)) == 13  # length for timestamp with milliseconds


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
