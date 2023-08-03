import os
import sys
from shutil import copyfile
from pathlib import Path

DEV = 'dev'
LINUX = 'linux'
ZSHRC = f"{LINUX}/.zshrc"
VIMRC = f"{DEV}/.vimrc"
BASHRC = f"{LINUX}/.bashrc"

DEFAULT_HOME_DIR = os.environ['HOME']

CURRENT_CONFS = os.listdir(LINUX) + os.listdir(DEV)

CURRENT_CONFS = [
    'linux/.zshrc',
    'linux/.bashrc',
    'dev/.vimrc'
]
