# -*- coding: utf-8 -*-

import click
from bse import logger, register
from bse.transform import Jsonable
from typing import Dict


@click.command(name="scripts")
@click.pass_obj
@logger.logexceptions
def cmd_scripts(obj: Dict[str, str]) -> int:
    """Show the scripts discovered by the BSE tool"""
    r = register.Register()
    scripts = [
        {"slug": slug, "description": r.load(slug).description} for slug in r.slugs()
    ]
    click.echo(Jsonable.dump(scripts))
    return 0
