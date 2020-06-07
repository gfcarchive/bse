# -*- coding: utf-8 -*-

import traceback
import mockup_coinbase as mc
from bse import cli, path
from click.testing import CliRunner


accounts = """[
    {
        "bankCode": "",
        "bic": "",
        "currency": "EUR",
        "iban": "",
        "name": "Coinbase",
        "number": "Main",
        "owner": "",
        "portfolio": true,
        "subAccount": "",
        "type": "Portfolio"
    }
]
"""


def test_coinbase_accounts(mocker) -> None:
    mocker.patch("bse.lua._globals.bse_time", return_value=1_590_067_388)
    mocker.patch("bse.lua._connection.Connection._request", side_effect=mc.mock_request)
    netrc = path.join(path.here(__file__), "..", "test.netrc")

    runner = CliRunner()
    result = runner.invoke(cli.main, f"--netrc {netrc} accounts coinbase")
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0
    assert result.output == accounts
