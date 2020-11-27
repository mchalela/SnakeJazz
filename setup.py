#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   SnakeJazz Project (https://github.com/mchalela/SnakeJazz/).
# Copyright (c) 2020, Martin Chalela
# License: MIT
#   Full Text: https://github.com/mchalela/SnakeJazz/blob/master/LICENSE


# =============================================================================
# DOCS
# =============================================================================

"""SnakeJazz installation file.
"""


# =============================================================================
# IMPORTS
# =============================================================================

import os
import pathlib

from ez_setup import use_setuptools

use_setuptools()

from setuptools import setup


# =============================================================================
# CONSTANTS
# =============================================================================

REQUIREMENTS = ["pygame", "youtube_dl", "validator_collection"]

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))

with open(PATH / "README.md") as fp:
    LONG_DESCRIPTION = fp.read()

with open(PATH / "snakejazz" / "__init__.py") as fp:
    for line in fp.readlines():
        if line.startswith("__version__ = "):
            VERSION = line.split("=", 1)[-1].replace('"', "").strip()
            break


DESCRIPTION = "Decorators for sound reproduction."


# =============================================================================
# FUNCTIONS
# =============================================================================


def do_setup():
    setup(
        name="snakejazz",
        version=VERSION,
        description=DESCRIPTION,
        long_description=LONG_DESCRIPTION,
        long_description_content_type="text/markdown",
        author="Martin Chalela",
        author_email="tinchochalela@gmail.com",
        url="https://github.com/mchalela/SnakeJazz",
        license="MIT",
        keywords=["snakejazz", "snake", "jazz", "decorator", "sound", "music"],
        classifiers=[
            "Development Status :: 4 - Beta",
            "Intended Audience :: Education",
            "Intended Audience :: Science/Research",
            "License :: OSI Approved :: MIT License",
            "Operating System :: OS Independent",
            "Programming Language :: Python",
            "Programming Language :: Python :: 3.8",
            "Programming Language :: Python :: Implementation :: CPython",
            "Topic :: Games/Entertainment",
            "Topic :: Multimedia :: Sound/Audio",
            "Topic :: Multimedia :: Video",
        ],
        packages=[
            "snakejazz",
            "snakejazz.sounds",
            "snakejazz.sounds.rhodesmas",
        ],
        include_package_data=True,
        py_modules=["ez_setup"],
        install_requires=REQUIREMENTS,
    )


if __name__ == "__main__":
    do_setup()
