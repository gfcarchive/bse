# -*- coding: utf-8 -*-

import tempfile
import traceback
from bse import defaults, cli
from click.testing import CliRunner


_cfg = f"""{{
    "netrc": "{defaults.NETRC}"
}}
"""


def test_config() -> None:
    """Test the config command"""
    runner = CliRunner()
    result = runner.invoke(cli.main, "config")
    assert result.output == _cfg
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0


def test_config_netrc() -> None:
    with tempfile.NamedTemporaryFile() as f:
        runner = CliRunner()
        result = runner.invoke(cli.main, f"--netrc {f.name} config")
        cfg = f"""{{
    "netrc": "{f.name}"
}}
"""
        assert result.output == cfg
        traceback.print_exception(*result.exc_info)
        assert result.exit_code == 0


_cfg_help = f"""Usage: bse config [OPTIONS]

  Get configuration options

Options:
  --help  Show this message and exit.
"""


def test_config_help() -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, "config --help")
    assert result.output == _cfg_help
    traceback.print_exception(*result.exc_info)
    assert result.exit_code == 0
