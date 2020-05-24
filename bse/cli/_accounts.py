# -*- coding: utf-8 -*-

import click
from bse import config, logger
from bse.engine import Engine
from bse.transform import Jsonable
from typing import Dict


@click.command(name="accounts")
@click.argument("slug", type=click.STRING)
@click.pass_obj
@logger.logexceptions
def cmd_accounts(obj: Dict[str, str], slug: str) -> int:
    """Retrieves the list of accounts for a given slug."""
    conf = config.new(obj)
    with Engine(slug, conf) as e:
        click.echo(Jsonable.dump(e.accounts()))
    return 0
