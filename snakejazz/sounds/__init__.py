#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   SnakeJazz Project (https://github.com/mchalela/SnakeJazz/).
# Copyright (c) 2020, Martin Chalela
# License: MIT
#   Full Text: https://github.com/mchalela/SnakeJazz/blob/master/LICENSE

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DOCS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

"""Collection of sounds to use with SnakeJazz."""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
import pathlib

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))
DOWNLOAD_PATH = PATH / "yt_downloads"

RICK_AND_MORTY = "https://youtu.be/ahgcD1xjRiQ"
"""str, url: Youtube link to original Snake Jazz song by Rick and Morty."""

RHODESMAS = {}
"""dict: Paths to all sounds available in this pack."""

for name in os.listdir(PATH / "rhodesmas"):
    if name.endswith(".wav"):
        RHODESMAS[name] = str(PATH / "rhodesmas" / name)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DONLOADS DIRECTORY
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Check if exists, create it otherwise
if not os.path.exists(DOWNLOAD_PATH):
    os.makedirs(DOWNLOAD_PATH)
