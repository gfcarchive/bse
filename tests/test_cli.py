# -*- coding: utf-8 -*-

"""Tests Click CLI"""

from bse import defaults, cli
from click.testing import CliRunner


_ocfg = f"""{{
    "netrc": "{defaults.NETRC}"
}}
"""


def test_config() -> None:
    """Test the config command"""
    runner = CliRunner()
    result = runner.invoke(cli.bse, 'config')
    assert result.exit_code == 0
    assert result.output == _ocfg


_cfg_help = f"""Usage: bse config [OPTIONS]

  Get configuration options

Options:
  --help  Show this message and exit.
"""


def test_config_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.bse, 'config --help')
    assert result.exit_code == 0
    assert result.output == _cfg_help


_bse_help = f"""Usage: bse [OPTIONS] COMMAND [ARGS]...

Options:
  --netrc PATH  Path to the .netrc file.  [environment variable: BSE_NETRC]
                [default: {defaults.NETRC}]

  --help        Show this message and exit.

Commands:
  config  Get configuration options
"""


def test_bse_help() -> None:
    runner = CliRunner()
    help_result = runner.invoke(cli.bse, ["--help"])
    assert help_result.exit_code == 0
    assert help_result.output == _bse_help
