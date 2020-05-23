# -*- coding: utf-8 -*-

import attr
from bse.transform import Jsonable
from enum import Enum
from typing import Optional


@attr.s
class Credential(object):
    username: Optional[str] = attr.ib()
    password: Optional[str] = attr.ib()


class AccountType(Enum):
    Girokonto = "Girokonto"
    Savings = "Savings"
    FixedTermDeposit = "FixedTermDeposit"
    Loan = "Loan"
    CreditCard = "CreditCard"
    Portfolio = "Portfolio"
    Other = "Other"

    @classmethod
    def moneymoneymap(cls, s: str) -> "AccountType":
        mmmap = {
            "AccountTypeGiro": cls.Girokonto,
            "AccountTypeSavings": cls.Savings,
            "AccountTypeFixedTermDeposit": cls.FixedTermDeposit,
            "AccountTypeLoan": cls.Loan,
            "AccountTypeCreditCard": cls.CreditCard,
            "AccountTypePortfolio": cls.Portfolio,
            "AccountTypeOther": cls.Other,
        }
        return mmmap[s]


@attr.s
class Account(Jsonable):

    name: str = attr.ib()
    portfolio: bool = attr.ib()
    currency: str = attr.ib()
    type: AccountType = attr.ib()
    owner: str = attr.ib(default="")
    number: str = attr.ib(default="")
    subAccount: str = attr.ib(default="")
    bankCode: str = attr.ib(default="")
    iban: str = attr.ib(default="")
    bic: str = attr.ib(default="")
