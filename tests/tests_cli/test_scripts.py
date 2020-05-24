# -*- coding: utf-8 -*-

import traceback
from bse import cli
from click.testing import CliRunner


_scripts = """[
    {
        "slug": "coinbase",
        "description": "Fetch balances from Coinbase API and list them as securities"
    }
]
"""


def test_scripts() -> None:
    """Test the scripts command"""
    runner = CliRunner()
    result = runner.invoke(cli.main, "scripts")
    assert result.output == _scripts
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0


_scripts_help = f"""Usage: bse scripts [OPTIONS]

  Show the scripts discovered by the BSE tool

Options:
  --help  Show this message and exit.
"""


def test_scripts_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, "scripts --help")
    assert result.output == _scripts_help
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0
