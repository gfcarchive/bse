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
