# -*- coding: utf-8 -*-

import tempfile
import traceback
from bse import cli
from click.testing import CliRunner


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
