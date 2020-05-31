# -*- coding: utf-8 -*-

import click
from bse import config, logger
from bse.engine import Engine
from bse.transform import Jsonable
from typing import Dict


@click.command(name="transfers")
@click.argument("slug", type=click.STRING)
@click.pass_obj
@logger.logexceptions
def cmd_transfers(obj: Dict[str, str], slug: str) -> int:
    """Retrieves the list of transfers for a given slug."""
    conf = config.new(obj)
    with Engine(slug, conf) as e:
        transfers = []
        for account in e.accounts():
            transfers.append(e.transfers(account))
        click.echo(Jsonable.dump(transfers))
    return 0
