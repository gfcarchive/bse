# -*- coding: utf-8 -*-
"""Console script for bse."""
import sys
import click
from bse import config as bse_config, defaults
from typing import Dict


@click.group()
@click.option('--netrc',
              envvar=defaults.ENV_NETRC,
              default=defaults.NETRC,
              type=click.Path(exists=True, readable=True, allow_dash=False),
              show_default=True,
              help=f"Path to the .netrc file.  [environment variable: {defaults.ENV_NETRC}]",
              )
@click.pass_context
def bse(ctx: click.Context, netrc: str) -> None:
    ctx.obj = {defaults.ENV_NETRC: netrc}


@bse.command()
@click.pass_obj
def config(obj: Dict[str, str]) -> int:
    """Get configuration options"""
    conf = bse_config.new(obj)
    click.echo(conf.json())
    return 0


if __name__ == "__main__":
    sys.exit(bse())  # pragma: no cover
