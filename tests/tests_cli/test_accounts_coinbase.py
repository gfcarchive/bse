# -*- coding: utf-8 -*-

import io
import requests
import traceback
from bse import cli, path
from click.testing import CliRunner
from typing import Dict


_mocked_user = """
{
    "data": {
        "id": "11111111-1111-1111-1111-111111111111",
        "name": "Name Surname",
        "resource": "user",
        "resource_path": "/v2/user",
        "native_currency": "EUR"
    }
}
"""


def _mocked_coinbase_request(
    method: str, url: str, post_content: Dict[str, str], headers: Dict[str, str]
) -> requests.Response:
    if url == "https://api.coinbase.com/v2/user":
        assert method == "GET"
        assert not post_content
        assert headers.get("CB-VERSION") == "2017-06-01"
        assert headers.get("CB-ACCESS-KEY") == "thisistheapikey"
        assert headers.get("CB-ACCESS-TIMESTAMP") == "1590067388"
        assert (
            headers.get("CB-ACCESS-SIGN")
            == "07f8d9a6e6764dd8aca4cc3ec089754898c674b5fb677ae427cf82231325c245"
        )
        resp = requests.Response()
        resp.status_code = 200
        resp.headers = {"content-type": "application/json"}
        resp.encoding = "utf-8"
        resp.raw = io.BytesIO(_mocked_user.encode())
        return resp
    return None


_coinbase_accounts = """[
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
    mocker.patch(
        "bse.lua._connection.Connection._request", side_effect=_mocked_coinbase_request
    )
    netrc = path.join(path.here(__file__), "..", "test.netrc")

    runner = CliRunner()
    result = runner.invoke(cli.main, f"--netrc {netrc} accounts coinbase")
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0
    assert result.output == _coinbase_accounts
