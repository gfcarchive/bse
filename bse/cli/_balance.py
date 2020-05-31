# -*- coding: utf-8 -*-

import click
from bse import config, logger
from bse.engine import Engine
from bse.transform import Jsonable
from typing import Dict


@click.command(name="balance")
@click.argument("slug", type=click.STRING)
@click.pass_obj
@logger.logexceptions
def cmd_balance(obj: Dict[str, str], slug: str) -> int:
    """Retrieves the balance in multiple currencies for a given slug."""
    conf = config.new(obj)
    with Engine(slug, conf) as e:
        balances = []
        for account in e.accounts():
            balances.append(e.balance(account))
        click.echo(Jsonable.dump(balances))
    return 0
