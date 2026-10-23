# boop fixture (IMPL-0001 8.1): building this sdist runs repository code.
import sys

with open("/tmp/boopd-sdist-marker", "w") as f:
    f.write("setup.py ran\n")
print("BOOPD-SDIST-MARKER: setup.py ran and wrote /tmp/boopd-sdist-marker", file=sys.stderr)

from setuptools import setup

setup(name="boop-fixture-sdist", version="0.1.0", py_modules=[])
