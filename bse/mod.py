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
    _luart: lupa.LuaRuntime = attr.ib()

    @_log.default
    def _initlog(self) -> logger.Logger:
        return logger.new(LuaMod.__class__.__name__)

    @_luart.default
    def _initluart(self) -> lupa.LuaRuntime:
        return lupa.LuaRuntime(unpack_returned_tuples=True)

    def _initglobals(self) -> None:
        g = self._luart.globals()
        if path.exists(self._script):
            g.extensionName = path.fname(self._script)
        else:
            g.extensionName = "string"
        g["bse_log"] = self._log

    def _runprologue(self) -> None:
        self._luart.execute(lua.prologue())

    def _initattrs(self) -> None:
        wb = lua.WebBanking(self._luart)
        wb.validate()
        d = wb.scope()

        # lupa converts 1.0 into 1. REMINDER: lua only has float numbers
        self.version = float(d["version"])

        self.url = d["url"]
        self.description = d["description"]
        self.name = d["services"][1]
        self.slug = d["extensionName"]

    def _runscript(self) -> None:
        if path.exists(self._script):
            self._luart.execute(path.readfile(self._script))
        else:
            self._luart.execute(self._script)

    def __attrs_post_init__(self) -> None:
        self._initglobals()
        self._runprologue()
        self._runscript()
        self._initattrs()


def load() -> None:
    pass
