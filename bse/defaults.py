# -*- coding: utf-8 -*-

from bse import path as _p

NETRC = _p.expanduser("~/.netrc")

LOG = _p.join(_p.here(__file__), "..", "bse.log")

# Environment variables

ENV_NETRC = "BSE_NETRC"

# Dict keys to mask when debugging

MASK_KEYS = ("CB-ACCESS-SIGN", "CB-ACCESS-KEY")
