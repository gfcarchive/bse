# -*- coding: utf-8 -*-

from bse import defaults, cli
from click.testing import CliRunner


_cfg = f"""{{
    "netrc": "{defaults.NETRC}"
}}
"""


def test_config() -> None:
    """Test the config command"""
    runner = CliRunner()
    result = runner.invoke(cli.cmd_root, 'config')
    assert result.exit_code == 0
    assert result.output == _cfg


_cfg_help = f"""Usage: bse config [OPTIONS]

  Get configuration options

Options:
  --help  Show this message and exit.
"""


def test_config_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.cmd_root, 'config --help')
    assert result.exit_code == 0
    assert result.output == _cfg_help
