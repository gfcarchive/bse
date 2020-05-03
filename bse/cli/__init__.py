# -*- coding: utf-8 -*-

from ._main import main
from ._config import cmd_config
from ._coinbase import grp_coinbase

main.add_command(grp_coinbase)
main.add_command(cmd_config)
