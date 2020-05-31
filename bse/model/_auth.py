# -*- coding: utf-8 -*-

import attr
from typing import Optional


@attr.s
class Credential(object):
    username: Optional[str] = attr.ib()
    password: Optional[str] = attr.ib()
