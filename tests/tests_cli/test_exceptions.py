# -*- coding: utf-8 -*-

import pytest  # type: ignore
from bse.cli._exceptions import jsonexception


def test_logging_decorator() -> None:
    @jsonexception
    def f() -> int:
        return 0

    assert f() == 0


def _check_echo(s: str) -> None:
    assert (
        s
        == """{
    "message": "this is an error",
    "type": "Exception"
}"""
    )


def test_uncaught_error(mocker) -> None:
    mocker.patch("click.echo", side_effect=_check_echo)

    @jsonexception
    def f() -> int:
        raise Exception("this is an error")

    with pytest.raises(Exception):
        f()
