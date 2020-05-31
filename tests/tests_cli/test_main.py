# -*- coding: utf-8 -*-

from bse import defaults, cli
from click.testing import CliRunner


_root_help = f"""Usage: bse [OPTIONS] COMMAND [ARGS]...

Options:
  --netrc PATH  Path to the .netrc file.  [environment variable: BSE_NETRC]
                [default: {defaults.NETRC}]

  --help        Show this message and exit.

Commands:
  accounts    Retrieves the list of accounts for a given slug.
  balance     Retrieves the balance in multiple currencies for a given slug.
  config      Get configuration options.
  securities  Retrieves the list of securities for a given slug.
  slugs       Shows the slugs loaded in bse.
  transfers   Retrieves the list of transfers for a given slug.
"""


def test_root_help() -> None:
    runner = CliRunner()
    help_result = runner.invoke(cli.main, ["--help"])
    assert help_result.exit_code == 0
    assert help_result.output == _root_help
