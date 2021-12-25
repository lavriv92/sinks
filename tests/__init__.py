import pathlib
import sys


BASE_PATH = pathlib.Path('.').absolute()


sys.path.append(str(BASE_PATH / 'src'))
