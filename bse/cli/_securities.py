# -*- coding: utf-8 -*-

import click
from bse import config, logger
from bse.engine import Engine
from bse.transform import Jsonable
from typing import Dict


@click.command(name="securities")
@click.argument("slug", type=click.STRING)
@click.pass_obj
@logger.logexceptions
def cmd_securities(obj: Dict[str, str], slug: str) -> int:
    """Retrieves the list of securities for a given slug."""
    conf = config.new(obj)
    with Engine(slug, conf) as e:
        securities = []
        for account in e.accounts():
            securities.append(e.securities(account))
        click.echo(Jsonable.dump(securities))
    return 0
