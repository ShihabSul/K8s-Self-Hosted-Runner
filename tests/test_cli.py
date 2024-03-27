import subprocess
import sys

from my_package import __version__


def test_cli_version():
    cmd = [sys.executable, "-m", "my_package", "--version"]
    assert subprocess.check_output(cmd).decode().strip() == __version__
