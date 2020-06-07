# -*- coding: utf-8 -*-

import io
import requests
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

_mocked_accounts = """
{
    "pagination": {
        "limit": 25
    },
    "data": [
        {
            "id": "11111111-1111-1111-1111-111111111111",
            "name": "My Wallet",
            "primary": true,
            "type": "wallet",
            "currency": {
                "code": "BTC",
                "name": "Bitcoin",
                "exponent": 8,
                "type": "crypto",
                "asset_id": "22222222-2222-2222-2222-222222222222",
                "slug": "bitcoin"
            },
            "balance": {
                "amount": "0.00000000",
                "currency": "BTC"
            },
            "created_at": "2014-04-13T08:47:30Z",
            "updated_at": "2016-01-05T12:32:08Z",
            "resource": "account",
            "resource_path": "/v2/accounts/11111111-1111-1111-1111-111111111111",
            "allow_deposits": true,
            "allow_withdrawals": true,
            "native_balance": {
                "amount": "0.00",
                "currency": "EUR"
            }
        }
    ]
}
"""

_mocked_fx_btc = """
{
    "data": {
        "currency": "BTC",
        "rates": {
            "EUR": "8567.555"
        }
    }
}

"""


def _check_input(
    method: str, post_content: Dict[str, str], headers: Dict[str, str], signature: str
) -> None:
    assert method == "GET"
    assert not post_content
    if signature:
        assert headers.get("CB-VERSION") == "2017-06-01"
        assert headers.get("CB-ACCESS-KEY") == "thisistheapikey"
        assert headers.get("CB-ACCESS-TIMESTAMP") == "1590067388"
        assert headers.get("CB-ACCESS-SIGN") == signature


def _response(content: str) -> requests.Response:
    resp = requests.Response()
    resp.status_code = 200
    resp.headers = {"content-type": "application/json"}
    resp.encoding = "utf-8"
    resp.raw = io.BytesIO(content.encode())
    return resp


def mock_request(
    method: str, url: str, post_content: Dict[str, str], headers: Dict[str, str]
) -> requests.Response:
    if url == "https://api.coinbase.com/v2/user":
        _check_input(
            "GET",
            post_content,
            headers,
            "07f8d9a6e6764dd8aca4cc3ec089754898c674b5fb677ae427cf82231325c245",
        )
        return _response(_mocked_user)
    if url == "https://api.coinbase.com/v2/accounts":
        _check_input(
            "GET",
            post_content,
            headers,
            "e877ea1985a2e41d50b35a85786f8d17630a6ea97909e1ce9b1a4312d8c059bb",
        )
        return _response(_mocked_accounts)
    if url == "https://api.coinbase.com/v2/exchange-rates?currency=BTC":
        _check_input("GET", post_content, headers, None)
        return _response(_mocked_fx_btc)

    assert False, f"URL {url} could not be mocked"
