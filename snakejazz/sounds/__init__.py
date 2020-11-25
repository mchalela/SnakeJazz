# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import pathlib

#from . import rhodesmas
from .rhodesmas import RHODESMAS

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PATHS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
'''
PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))

AVAILABLE_PACKS = ["rhodesmas"]

for name in AVAILABLE_PACKS:
    print(name)
    if not os.path.isdir(PATH / name):
        print(PATH / name)

PACK_PATHS = [
    str(PATH / name) for name in AVAILABLE_PACKS if os.path.isdir(PATH / name)
]
print(PACK_PATHS)
RHODESMAS = {}
for pack in PACK_PATHS:
    print(pack)
    for name in os.listdir(pack):
        print(name)
        if name.endswith(".wav"):
            RHODESMAS[name] = str(PATH / pack / name)
'''
print(RHODESMAS)