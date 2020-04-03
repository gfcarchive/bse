# -*- coding: utf-8 -*-

import attr
import json
from bse import logger
from typing import Any, Dict, Optional


@attr.s
class JSON(object):

    _jsontext: Optional[str] = attr.ib(default="")
    _json: Optional[Any] = attr.ib(default=None)
    _log: logger.Logger = attr.ib()

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(self.__class__.__name__)

    def dictionary(self) -> Dict[str, Any]:
        self._log.debug(f"[JSON(...):dictionary()] {self._jsontext}")
        if self._json:
            return self._json
        if not self._jsontext:
            self._jsontext = "{}"
        self._json = json.loads(self._jsontext)
        return self._json

    def set(self, j: Any) -> "JSON":
        self._json = j
        self._jsontext = json.dumps(j)
        self._log.debug(f"[JSON():set(...)] {self._jsontext}")
        return self

    def json(self) -> str:
        self._log.debug(f"[JSON():json()] {self._jsontext}")
        return self._jsontext or ""
