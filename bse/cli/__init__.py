# -*- coding: utf-8 -*-

from ._accounts import cmd_accounts
from ._balance import cmd_balance
from ._config import cmd_config
from ._main import main
from ._securities import cmd_securities
from ._slugs import cmd_slugs
from ._transfers import cmd_transfers

main.add_command(cmd_accounts)
main.add_command(cmd_balance)
main.add_command(cmd_config)
main.add_command(cmd_securities)
main.add_command(cmd_slugs)
main.add_command(cmd_transfers)
