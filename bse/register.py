# -*- coding: utf-8 -*-

import attr
from bse import defaults, module, path
from glob import glob
from typing import Dict, List


class RegisterError(Exception):
    pass


@attr.s
class Register(object):

    _r: Dict[str, module.Mod] = attr.ib(factory=dict)

    def __attrs_post_init__(self) -> None:
        for _p in defaults.SCRIPT_PATHS:
            for script in glob(path.join(_p, "*.lua")):
                m = module.LuaMod(script)
                self._r[m.slug] = m

    def load(self, slug: str) -> module.Mod:
        s = self._r.get(slug)
        if s:
            return s
        raise RegisterError(
            f"Script '{slug}' not found. Slugs available are {self._r.keys()}"
        )

    def slugs(self) -> List[str]:
        return list(self._r.keys())
