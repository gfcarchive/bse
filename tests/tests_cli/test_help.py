# -*- coding: utf-8 -*-

import mockup_help as mh
import pytest  # type: ignore
from bse import cli
from click.testing import CliRunner


@pytest.mark.parametrize("command", list(cli.main.commands.keys()))
def test_help(command) -> None:
    runner = CliRunner()
    help_result = runner.invoke(cli.main, [command, "--help"])
    assert help_result.exit_code == 0
    assert help_result.output == mh.help[command]
