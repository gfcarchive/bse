# -*- coding: utf-8 -*-

import traceback
from bse import cli
from click.testing import CliRunner


_balance_without_slug = f"""Usage: bse balance [OPTIONS] SLUG
Try 'bse balance --help' for help.

Error: Missing argument 'SLUG'.
"""


def test_balance_without_slug() -> None:
    """Test the balance command"""
    runner = CliRunner()
    result = runner.invoke(cli.main, "balance")
    assert result.output == _balance_without_slug
    traceback.print_exception(*result.exc_info)
    assert result.exit_code > 0


_balance_help = f"""Usage: bse balance [OPTIONS] SLUG

  Retrieves the balance in multiple currencies for a given slug.

Options:
  --help  Show this message and exit.
"""


def test_balance_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, "balance --help")
    assert result.output == _balance_help
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0
