# -*- coding: utf-8 -*-

import traceback
import mockup_coinbase as mc
from bse import cli, path
from click.testing import CliRunner


_out = """[
    {
        "amount": "0.00",
        "currency": null,
        "exchange_rate": null,
        "isin": null,
        "market": "Coinbase",
        "name": "Bitcoin",
        "number": null,
        "original_amount": null,
        "original_currency": null,
        "price": null,
        "price_currency": null,
        "purchase_price": null,
        "purchase_price_currency": null,
        "quantity": null,
        "trade_timestamp": null
    }
]
"""


def test_coinbase_securities(mocker) -> None:
    mocker.patch("bse.lua._globals.bse_time", return_value=1_590_067_388)
    mocker.patch("bse.lua._connection.Connection._request", side_effect=mc.mock_request)
    netrc = path.join(path.here(__file__), "..", "test.netrc")
    # netrc = defaults.NETRC

    runner = CliRunner()
    result = runner.invoke(cli.main, f"--netrc {netrc} securities coinbase")
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0
    assert result.output == _out
