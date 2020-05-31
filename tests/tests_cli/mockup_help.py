# -*- coding: utf-8 -*-

_help_accounts = """Usage: bse accounts [OPTIONS] SLUG

  Retrieves the list of accounts for a given slug.

Options:
  --help  Show this message and exit.
"""

_help_balance = """Usage: bse balance [OPTIONS] SLUG

  Retrieves the balance in multiple currencies for a given slug.

Options:
  --help  Show this message and exit.
"""

_help_config = """Usage: bse config [OPTIONS]

  Get configuration options.

Options:
  --help  Show this message and exit.
"""

_help_securities = """Usage: bse securities [OPTIONS] SLUG

  Retrieves the list of securities for a given slug.

Options:
  --help  Show this message and exit.
"""

_help_slugs = """Usage: bse slugs [OPTIONS]

  Shows the slugs loaded in bse. A slug is the identifier used for a script

Options:
  --help  Show this message and exit.
"""

_help_transfers = """Usage: bse transfers [OPTIONS] SLUG

  Retrieves the list of transfers for a given slug.

Options:
  --help  Show this message and exit.
"""

help = {
    "accounts": _help_accounts,
    "balance": _help_balance,
    "config": _help_config,
    "securities": _help_securities,
    "slugs": _help_slugs,
    "transfers": _help_transfers,
}
