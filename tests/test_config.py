# -*- coding: utf-8 -*-

from bse import config, defaults, path
import pytest  # type: ignore


def test_missing_netrc() -> None:
    netrc = path.join(path.here(__file__), "this_file_does_not_exist")
    cfg = config.new({defaults.ENV_NETRC: netrc})
    with pytest.raises(FileNotFoundError):
        cfg.readrc("machine")


def test_missing_machine() -> None:
    netrc = path.join(path.here(__file__), "test.netrc")
    cfg = config.new({defaults.ENV_NETRC: netrc})
    with pytest.raises(KeyError):
        cfg.readrc("machine_does_not_exist")


def test_login() -> None:
    netrc = path.join(path.here(__file__), "test.netrc")
    cfg = config.new({defaults.ENV_NETRC: netrc})
    cred = cfg.readrc("api.coinbase.com")
    assert cred.login == "thisistheapikey"
