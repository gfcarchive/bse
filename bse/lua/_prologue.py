# -*- coding: utf-8 -*-

from bse import path


def prologue() -> None:
    script = path.join(path.here(__file__), "_prologue.lua")
    return path.readfile(script)
