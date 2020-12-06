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

"""
SnakeJazz.

Listen to the running status of your ~~Snake~~ Python functions.
"""

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# METADATA
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

__version__ = "0.1.1"

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

from . import sounds  # noqa

from .snakejazz import zzz, www, rattle  # noqa
from .snakejazz import play_sound, get_sound  # noqa
from .snakejazz import DEFAULT_URL_START, DEFAULT_START  # noqa
from .snakejazz import DEFAULT_URL_FINISH, DEFAULT_FINISH  # noqa
from .snakejazz import DEFAULT_URL_ERROR, DEFAULT_ERROR  # noqa
from .snakejazz import SnakeNotFoundError, URLError  # noqa
