# -*- coding: utf-8 -*-

import traceback
import mockup_coinbase as mc
from bse import cli, path
from click.testing import CliRunner


def test_coinbase_transfers(mocker) -> None:
    mocker.patch("bse.lua._globals.bse_time", return_value=1_590_067_388)
    mocker.patch("bse.lua._connection.Connection._request", side_effect=mc.mock_request)
    netrc = path.join(path.here(__file__), "..", "test.netrc")

    runner = CliRunner()
    result = runner.invoke(cli.main, f"--netrc {netrc} transfers coinbase")
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 1
    assert result.exception.__class__ == NotImplementedError
    # assert result.output == mc.transfers
