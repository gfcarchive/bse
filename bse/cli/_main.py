# -*- coding: utf-8 -*-

import click
from bse import defaults
from bse import logger, todo


@click.group(name="bse")
@click.option(
    "--netrc",
    envvar=defaults.ENV_NETRC,
    default=defaults.NETRC,
    type=click.Path(exists=True, readable=True, allow_dash=False),
    show_default=True,
    help=f"Path to the .netrc file.  [environment variable: {defaults.ENV_NETRC}]",
)
@click.pass_context
def main(ctx: click.Context, netrc: str) -> None:
    ctx.obj = {defaults.ENV_NETRC: netrc}
    for t in todo.TODOs:
        logger.new(t.filename).warning(f"[{t.context}] {t.msg}")
