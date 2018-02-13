import os
import contextlib


@contextlib.contextmanager
def onDir(path):
    current = os.getcwd()
    os.chdir(path)
    yield
    os.chdir(current)
