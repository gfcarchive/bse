# -*- coding: utf-8 -*-

import attr
from ._core import LuaRuntime, LuaError
from ._scope import Scope
from schema import Schema, SchemaError, SchemaMissingKeyError, And, Or  # type: ignore
from typing import Any, Dict


@attr.s
class WebBanking(Scope):

    luart: LuaRuntime = attr.ib()

    def scope(self) -> Dict[str, Any]:
        g = self.luart.globals()
        return {
            "version": g.version,
            "url": g.url,
            "description": g.description,
            "services": g.services,
            "extensionName": g.extensionName,
        }

    def validate(self) -> None:
        schema = Schema(
            {
                "version": Or(int, float),
                "url": And(str, len),
                "description": And(str, len),
                "services": lambda x: x,
                "extensionName": And(str, len),
            }
        )
        try:
            schema.validate(self.scope())
        except SchemaError as e:
            if isinstance(e, SchemaMissingKeyError):
                e.autos = [f"WebBanking: {a}" for a in e.autos]
            raise LuaError(e)
