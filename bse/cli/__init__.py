# -*- coding: utf-8 -*-

from ._engine import cmd_accounts, account_detail_cmds
from ._config import cmd_config
from ._main import main
from ._slugs import cmd_slugs

main.add_command(cmd_accounts)
main.add_command(cmd_config)
main.add_command(cmd_slugs)

for cmd in account_detail_cmds:
    main.add_command(cmd)
