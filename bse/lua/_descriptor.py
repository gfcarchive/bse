# -*- coding: utf-8 -*-

import attr
from ._core import LuaRuntime, LuaError
from bse import __version__
from typing import Dict, Optional, Union


def _valueval(instance: "Descriptor", attribute: attr.Attribute, value: str) -> None:
    if attribute.name == "url":

        def val(x: str) -> int:
            return x is None or (isinstance(value, str) and len(value))

    else:

        def val(x: str) -> int:
            return isinstance(value, str) and len(value)

    if not val(value):
        raise LuaError(f"WebBanking: {attribute} has invalid value {value}")


@attr.s
class Descriptor(object):
    version: str = attr.ib(validator=_valueval)
    description: str = attr.ib(validator=_valueval)
    name: str = attr.ib(validator=_valueval)
    protocol: str = attr.ib(validator=_valueval)
    url: str = attr.ib(default=None, validator=_valueval)


def descriptor(luart: LuaRuntime) -> Descriptor:
    g = luart.globals()
    version = _version(g.version)
    name = _name(g.services, g.extensionName)
    return Descriptor(
        version=version,
        url=g.url,
        description=g.description,
        name=name,
        protocol=g.ProtocolWebBanking,
    )


def _name(v: Optional[Dict[int, str]], default: str) -> str:
    if not v:
        return default
    if len(v) > 1:
        raise ValueError("Only 1 service declaration allowed")
    return v[1]


def _version(v: Optional[Union[int, float, str]]) -> str:
    if not v:
        return __version__
    if isinstance(v, float):
        return str(v)
    if isinstance(v, int):
        return f"{v:.1f}"
    return v
