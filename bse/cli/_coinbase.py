# -*- coding: utf-8 -*-

import click
from bse import config, logger
from bse.engine import Engine
from bse.transform import Jsonable
from typing import Dict


@click.group(name="coinbase")
@click.pass_context
def grp_coinbase(ctx: click.Context) -> None:
    """Access Coinbase account and transaction data"""
    pass


@grp_coinbase.command(name="accounts")
@click.pass_obj
@logger.logexceptions
def cmd_accounts(obj: Dict[str, str]) -> int:
    """Retrieves the list of accounts"""
    conf = config.new(obj)
    with Engine("coinbase", conf) as e:
        click.echo(Jsonable.dump(e.accounts()))
    return 0
