# -*- coding: utf-8 -*-

from ._accounts import cmd_accounts
from ._main import main
from ._config import cmd_config
from ._slugs import cmd_slugs

main.add_command(cmd_accounts)
main.add_command(cmd_config)
main.add_command(cmd_slugs)
