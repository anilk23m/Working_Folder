import os
from contextlib import contextmanager

@contextmanager
def change_dir(destination):
    try:
        cwd = os.getcwd()
        os.chdir(destination)
        yield
    finally:
        os.chdir(cwd)

with change_dir('D:\Python folder\python_projects\OOOps'):
    print(os.listdir())

with change_dir("D:\Python folder\python_projects\FileI_O"):
    print(os.listdir())

print(os.getcwd())
