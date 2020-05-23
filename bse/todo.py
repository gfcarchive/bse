# -*- coding: utf-8 -*-

import attr
from bse import defaults


@attr.s
class TODO(object):
    filename: str = attr.ib()
    context: str = attr.ib()
    msg: str = attr.ib()


TODOs = (
    TODO(
        defaults.__name__,
        "LOG",
        "Initialize log file location depending on runtime: testing, installed, etc",
    ),
)
