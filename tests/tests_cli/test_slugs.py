# -*- coding: utf-8 -*-

import traceback
from bse import cli
from click.testing import CliRunner


_slugs = """[
    {
        "slug": "coinbase",
        "description": "Fetch balances from Coinbase API and list them as securities"
    }
]
"""


def test_slugs() -> None:
    """Test the slugs command"""
    runner = CliRunner()
    result = runner.invoke(cli.main, "slugs")
    assert result.output == _slugs
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0


_slugs_help = f"""Usage: bse slugs [OPTIONS]

  Shows the slugs loaded in bse. A slug is the identifier used for a script

Options:
  --help  Show this message and exit.
"""


def test_slugs_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, "slugs --help")
    assert result.output == _slugs_help
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0
