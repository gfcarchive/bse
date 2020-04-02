# -*- coding: utf-8 -*-

from ._core import LuaRuntime, LuaError
from bse import __version__
from schema import Schema, SchemaError, SchemaMissingKeyError, And, Or  # type: ignore
from typing import Dict, Optional, Union


def environment(luart: LuaRuntime) -> Dict[str, str]:
    g = luart.globals()
    version = _version(g.version)
    name = _name(g.services, g.extensionName)
    env = {
        "version": version,
        "url": g.url,
        "description": g.description,
        "name": name,
        "extensionName": g.extensionName,
    }
    _validate(env)
    return env


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
    return f"{v:.1f}"


def _validate(env: Dict[str, str]) -> None:
    schema = Schema(
        {
            "version": And(str, len),
            "url": Or(None, And(str, len)),
            "description": And(str, len),
            "name": And(str, len),
            "extensionName": And(str, len),
        }
    )
    try:
        schema.validate(env)
    except SchemaError as e:
        if isinstance(e, SchemaMissingKeyError):
            e.autos = [f"WebBanking: {a}" for a in e.autos]
        raise LuaError(e)
