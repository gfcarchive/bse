# -*- coding: utf-8 -*-
import os.path


# directly imported from os.path
exists = os.path.exists
join = os.path.join


# created specifically for bse
def here(file_: str) -> str:
    """
    Given __file__ it returns the absolute path to the file directory
    """
    return os.path.abspath(os.path.dirname(file_))


def fname(fpath: str) -> str:
    """
    Given a file like /opt/text.txt; it returns text
    """
    return os.path.basename(fpath).split(os.path.extsep)[0]


def readfile(fpath: str) -> str:
    with open(fpath, "r") as f:
        return f.read()
