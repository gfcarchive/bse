# -*- coding: utf-8 -*-

import click
from ._exceptions import jsonexception
from bse import config
from bse.engine import Engine
from bse.transform import Jsonable
from typing import Any, Callable, Dict


@click.command(name="accounts")
@click.argument("slug", type=click.STRING)
@click.pass_obj
@jsonexception
def cmd_accounts(obj: Dict[str, str], slug: str) -> int:
    """Retrieves the list of accounts for a given slug."""
    conf = config.new(obj)
    with Engine(slug, conf) as e:
        click.echo(Jsonable.dump(e.accounts()))
    return 0


_cmddef = (
    ("balance", "Retrieves the balance in multiple currencies for a given slug."),
    ("securities", "Retrieves the list of securities for a given slug."),
    ("transfers", "Retrieves the list of transfers for a given slug."),
)

account_detail_cmds: Any = []


def _newcmd(cmd: str, doc: str) -> Callable[..., Any]:
    @click.command(name=cmd)
    @click.argument("slug", type=click.STRING)
    @click.pass_obj
    @jsonexception
    def cmdf(obj: Dict[str, str], slug: str) -> int:

        conf = config.new(obj)
        with Engine(slug, conf) as e:
            ret = []
            for account in e.accounts():
                f = getattr(e, cmd)
                tmpret = f(account)
                if isinstance(tmpret, list):
                    ret.extend(tmpret)
                else:
                    ret.append(f(account))
            click.echo(Jsonable.dump(ret))
        return 0

    cmdf.help = doc
    return cmdf


for (cmd, doc) in _cmddef:
    account_detail_cmds.append(_newcmd(cmd, doc))
