# -*- coding: utf-8 -*-

import click
from bse import config, logger
from bse.engine import Engine
from bse.transform import Jsonable
from bse.mod import ModType
from typing import Dict


@click.group(name="coinbase")
@click.pass_context
def grp_coinbase(ctx: click.Context) -> None:
    """Access Coinbase account and transaction data"""
    pass


@grp_coinbase.command(name="accounts")
@click.pass_obj
def cmd_accounts(obj: Dict[str, str]) -> int:
    """Retrieves the list of accounts"""
    try:
        conf = config.new(obj)
        with Engine(ModType.Coinbase, conf) as e:
            click.echo(Jsonable.dump(e.accounts()))
        return 0
    except Exception as e:
        log = logger.new("Coinbase accounts")
        log.exception(e)
        raise e
