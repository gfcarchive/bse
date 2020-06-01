# -*- coding: utf-8 -*-

from bse import defaults

_main = f"""Usage: bse [OPTIONS] COMMAND [ARGS]...

Options:
  --netrc PATH  Path to the .netrc file.  [environment variable: BSE_NETRC]
                [default: {defaults.NETRC}]

  --help        Show this message and exit.

Commands:
  accounts    Retrieves the list of accounts for a given slug.
  balance     Retrieves the balance in multiple currencies for a given slug.
  config      Get configuration options.
  securities  Retrieves the list of securities for a given slug.
  slugs       Shows the slugs loaded in bse.
  transfers   Retrieves the list of transfers for a given slug.
"""

_accounts = """Usage: bse accounts [OPTIONS] SLUG
Try 'bse accounts --help' for help.

Error: Missing argument 'SLUG'.
"""

_balance = """Usage: bse balance [OPTIONS] SLUG
Try 'bse balance --help' for help.

Error: Missing argument 'SLUG'.
"""

_config = f"""{{
    "netrc": "{defaults.NETRC}"
}}
"""

_securities = """Usage: bse securities [OPTIONS] SLUG
Try 'bse securities --help' for help.

Error: Missing argument 'SLUG'.
"""

_slugs = """[
    {
        "slug": "coinbase",
        "description": "Fetch balances from Coinbase API and list them as securities"
    }
]
"""

_transfers = """Usage: bse transfers [OPTIONS] SLUG
Try 'bse transfers --help' for help.

Error: Missing argument 'SLUG'.
"""

commands = {
    # this first entry for the basic bse run, without any command
    "": (_main, lambda exit_code: exit_code == 0),
    "accounts": (_accounts, lambda exit_code: exit_code > 0),
    "balance": (_balance, lambda exit_code: exit_code > 0),
    "config": (_config, lambda exit_code: exit_code == 0),
    "securities": (_securities, lambda exit_code: exit_code > 0),
    "slugs": (_slugs, lambda exit_code: exit_code == 0),
    "transfers": (_transfers, lambda exit_code: exit_code > 0),
}
