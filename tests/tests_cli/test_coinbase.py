# -*- coding: utf-8 -*-

import tempfile
import traceback
from bse import cli, path
from click.testing import CliRunner


_coinbase_help = f"""Usage: bse coinbase [OPTIONS] COMMAND [ARGS]...

  Access Coinbase account and transaction data

Options:
  --help  Show this message and exit.

Commands:
  accounts  Retrieves the list of accounts
"""


def test_coinbase_help() -> None:
    with tempfile.NamedTemporaryFile() as f:
        runner = CliRunner()
        result = runner.invoke(cli.main, f"--netrc {f.name} coinbase --help")
        traceback.print_exception(*result.exc_info)
        assert result.exit_code == 0
        assert result.output == _coinbase_help


def test_coinbase_acounts() -> None:
    netrc = path.join(path.here(__file__), "..", "test.netrc")
    runner = CliRunner()
    result = runner.invoke(cli.main, f"--netrc {netrc} coinbase accounts")
    assert isinstance(result.exception, NotImplementedError)
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 1
    # assert result.output == ""
