# -*- coding: utf-8 -*-

import attr
from enum import Enum
from typing import Optional


@attr.s
class Credential(object):
    username: Optional[str] = attr.ib()
    password: Optional[str] = attr.ib()


class AccountType(Enum):
    Girokonto = "Girokonto"
    Sparkonto = "Sparkonto"
    FixedTermDeposit = "FixedTermDeposit"
    Loan = "Loan"
    CreditCard = "CreditCard"
    Portfolio = "Portfolio"
    Other = "Other"


@attr.s
class Account(object):

    name: str = attr.ib()
    owner: str = attr.ib()
    accountNumber: str = attr.ib()
    subAccount: str = attr.ib()
    portfolio: bool = attr.ib()
    bankCode: str = attr.ib()
    currency: str = attr.ib()
    iban: str = attr.ib()
    bic: str = attr.ib()
    type: AccountType = attr.ib()
