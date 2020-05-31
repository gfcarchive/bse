# -*- coding: utf-8 -*-

import traceback
from bse import cli
from click.testing import CliRunner


_securities_without_slug = f"""Usage: bse securities [OPTIONS] SLUG
Try 'bse securities --help' for help.

Error: Missing argument 'SLUG'.
"""


def test_securities_without_slug() -> None:
    """Test the securities command"""
    runner = CliRunner()
    result = runner.invoke(cli.main, "securities")
    assert result.output == _securities_without_slug
    traceback.print_exception(*result.exc_info)
    assert result.exit_code > 0
