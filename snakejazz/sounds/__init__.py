# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import pathlib

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PATHS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))

AVAILABLE_PACKS = ["rhodesmas"]
PACK_PATHS = [
    PATH / name for name in AVAILABLE_PACKS if os.path.isdir(PATH / name)
]

RHODESMAS = {}
for pack in PACK_PATHS:
    for name in os.listdir(pack):
        if name.endswith(".wav"):
            RHODESMAS[name] = str(PATH / pack / name)
