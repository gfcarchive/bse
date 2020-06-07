# -*- coding: utf-8 -*-

import attr
import json
from ._pylua import py2lua, lua2py
from bse import logger
from lupa import LuaRuntime  # type: ignore
from typing import Any, Dict, Optional


@attr.s
class JSON(object):

    luart: LuaRuntime = attr.ib()
    jsontext: Optional[str] = attr.ib(default="")
    _json: Optional[Any] = attr.ib(default=None)
    _log: logger.Logger = attr.ib()

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(self.__class__.__name__)

    def dictionary(self) -> Dict[str, Any]:
        if not self._json:
            if not self.jsontext:
                self.jsontext = "{}"
            self._json = json.loads(self.jsontext)

        self._log.debug(self._json, extra={"context": "[JSON(...):dictionary()]"})
        return py2lua(self.luart, self._json)

    def set(self, j: Any) -> "JSON":
        self._json = lua2py(j)
        self.jsontext = json.dumps(self._json)
        self._log.debug(f"[JSON():set(...)] {self.jsontext}")
        return self

    def json(self) -> str:
        self._log.debug(f"[JSON():json()] {self.jsontext}")
        return self.jsontext or ""
