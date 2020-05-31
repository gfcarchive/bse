# -*- coding: utf-8 -*-

import mockup_help as mh
from bse import cli
from click.testing import CliRunner


def test_help() -> None:
    commands = list(cli.main.commands.keys())
    for command in commands:
        runner = CliRunner()
        help_result = runner.invoke(cli.main, [command, "--help"])
        assert help_result.exit_code == 0
        assert help_result.output == mh.help[command]
