# -*- coding: utf-8 -*-

import traceback
from bse import cli
from click.testing import CliRunner


_accounts_without_slug = f"""Usage: bse accounts [OPTIONS] SLUG
Try 'bse accounts --help' for help.

Error: Missing argument 'SLUG'.
"""


def test_accounts_without_slug() -> None:
    """Test the accounts command"""
    runner = CliRunner()
    result = runner.invoke(cli.main, "accounts")
    assert result.output == _accounts_without_slug
    traceback.print_exception(*result.exc_info)
    assert result.exit_code > 0
