# -*- coding: utf-8 -*-

import pytest  # type: ignore
from bse import logger


def test_logging_decorator() -> None:
    @logger.logexceptions
    def f() -> int:
        return 1

    assert f() == 1


def test_error_in_logging_decorator() -> None:
    @logger.logexceptions
    def f() -> int:
        raise Exception("this is an error")

    with pytest.raises(Exception):
        f()
