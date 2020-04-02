# -*- coding: utf-8 -*-

import attr
import json
from typing import Any, Dict, Optional


@attr.s
class JSON(object):

    _json: Optional[str] = attr.ib(default="")

    def dictionary(self) -> Dict[str, Any]:
        if not self._json:
            self._json = "{}"
        return json.loads(self._json)
