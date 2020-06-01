# -*- coding: utf-8 -*-

import mockup_commands as mc
import pytest  # type: ignore
from bse import cli
from click.testing import CliRunner


# "" for the main command (just `bse`)
@pytest.mark.parametrize("command", list(cli.main.commands.keys()) + [""])
def test_commands_without_params(command: str) -> None:
    runner = CliRunner()
    result = runner.invoke(cli.main, command)
    (cout, fcode) = mc.commands[command]
    assert fcode(result.exit_code)
    assert result.output == cout
