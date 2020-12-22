from click.testing import CliRunner

from knowbox import main


def test_main():
    runner = CliRunner()
    result = runner.invoke(main.test)
    assert result.exit_code == 0
    assert result.output == "Hello World!\n"
