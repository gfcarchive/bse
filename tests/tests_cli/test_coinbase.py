# -*- coding: utf-8 -*-

from bse import cli
from click.testing import CliRunner


_coinbase_help = f"""Usage: bse coinbase [OPTIONS] COMMAND [ARGS]...

  Access Coinbase account and transaction data

Options:
  --help  Show this message and exit.

Commands:
  accounts
"""


def test_coinbase_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, "coinbase --help")
    assert result.exit_code == 0
    assert result.output == _coinbase_help
