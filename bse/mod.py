# -*- coding: utf-8 -*-
import attr
import lupa  # type: ignore
from bse import path
from bse import logger
from bse import lua


@attr.s
class Mod(object):
    version: float = attr.ib(init=False)
    url: str = attr.ib(init=False)
    description: str = attr.ib(init=False)
    name: str = attr.ib(init=False)
    slug: str = attr.ib(init=False)


@attr.s
class LuaMod(Mod):

    _script: str = attr.ib()  # _script could be either a file path, or a text to execute
    _log: logger.Logger = attr.ib()

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(LuaMod.__class__.__name__)

    def _initglobals(self, luart: lupa.LuaRuntime) -> None:
        g = luart.globals()
        if path.exists(self._script):
            g.extensionName = path.fname(self._script)
        else:
            g.extensionName = "string"

    def _runprologue(self, luart: lupa.LuaRuntime) -> None:
        prologue = path.join(path.here(__file__), "_prologue.lua")
        luart.execute(path.readfile(prologue))

    def _initattrs(self, luart: lupa.LuaRuntime) -> None:
        wb = lua.WebBanking(luart)
        wb.validate()
        d = wb.scope()

        # lupa converts 1.0 into 1. REMINDER: lua only has float numbers
        self.version = float(d["version"])

        self.url = d["url"]
        self.description = d["description"]
        self.name = d["services"][1]
        self.slug = d["extensionName"]

    def _runscript(self, luart: lupa.LuaRuntime) -> None:
        if path.exists(self._script):
            luart.execute(path.readfile(self._script))
        else:
            luart.execute(self._script)

    def __attrs_post_init__(self) -> None:
        luart = lupa.LuaRuntime(unpack_returned_tuples=True)
        self._initglobals(luart)

        self._runprologue(luart)

        self._runscript(luart)

        self._initattrs(luart)


def load() -> None:
    pass
