# -*- coding: utf-8 -*-

from bse import defaults, cli
from click.testing import CliRunner


_root_help = f"""Usage: bse [OPTIONS] COMMAND [ARGS]...

Options:
  --netrc PATH  Path to the .netrc file.  [environment variable: BSE_NETRC]
                [default: {defaults.NETRC}]

  --help        Show this message and exit.

Commands:
  coinbase  Access Coinbase account and transaction data
  config    Get configuration options
  scripts   Show the scripts discovered by the BSE tool
"""


def test_root_help() -> None:
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert help_result.output == _root_help
