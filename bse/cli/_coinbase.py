# -*- coding: utf-8 -*-

import click
from ._root import cmd_root
from typing import Dict


@cmd_root.group(name='coinbase')
@click.pass_context
def cmd_coinbase(ctx: click.Context) -> None:
    """Access Coinbase account and transaction data"""


@cmd_coinbase.command(name="accounts")
@click.pass_obj
def cmd_accounts(obj: Dict[str, str]) -> int:
    pass
