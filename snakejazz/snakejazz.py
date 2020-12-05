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
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import multiprocessing as mp
import os
from contextlib import redirect_stdout
from functools import partial, wraps

# Hide print message at import
os.environ["PYGAME_HIDE_SUPPORT_PROMPT"] = "hide"
import pygame

from validator_collection import checkers

from youtube_dl import YoutubeDL

from . import sounds


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DEFAULT_START = sounds.RHODESMAS["connected-01.wav"]
DEFAULT_FINISH = sounds.RHODESMAS["disconnected-01.wav"]
DEFAULT_ERROR = sounds.RHODESMAS["failure-01.wav"]

DEFAULT_URL_START = sounds.RICK_AND_MORTY
DEFAULT_URL_FINISH = sounds.RICK_AND_MORTY
DEFAULT_URL_ERROR = sounds.RICK_AND_MORTY

DEFAULT_RATTLE = sounds.RICK_AND_MORTY

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# EXCEPTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


class SnakeNotFoundError(FileNotFoundError):
    """Raised when the file can't be found."""

    pass


class URLError(OSError):
    """Raised when the url is invalid."""

    pass


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRIVATE FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def _parse_param(param, default):

    if param is not None and not isinstance(param, (bool, str)):
        raise ValueError(f"Invalid parameter input {param}.")

    if param is None or param is False:
        return False
    elif param is True:
        return default
    elif os.path.isfile(str(param)):
        return str(param)
    else:
        raise SnakeNotFoundError(f"The snake file {param} doesn't exists.")


def _parse_url(param, default):
    if param is not None and not isinstance(param, (bool, str)):
        raise ValueError(f"Invalid parameter input {param}.")

    if param is None or param is False:
        return False
    elif param is True:
        return default
    elif checkers.is_url(str(param)):
        return str(param)
    else:
        raise URLError(f"Invalid url: {param}")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SOUND PLAYER
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def play_sound(sound_path, loops=0):
    """Reproduce the sound.

    The library PyGame is used to reproduce sounds.

    Parameters
    ----------
    sound_path: string, path
        Path to the sound file.
    loops: int
        Number of times the sound will be played.

        0: A single time

        -1: Inifinte loop
    """
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play(loops=loops)
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    return


def get_sound(
    yt_url=None,
    yt_id="ahgcD1xjRiQ",
    use_cache=True,
):
    """Download the sound.

    The library youtube-dl is used to download sounds.

    Parameters
    ----------
    yt_url: string, link
        Youtube link. The audio will be extracted from the video.
    yt_id: str, id
        Youtube video id. Is this is given the full url will be
        completed as https://www.youtube.com/watch?v=yt_id
    use_cache: bool
        When True, a sound will be downloaded just once and save it
        for later use if needed.
    """
    # Build the video url
    if yt_url is None:
        yt_url = f"https://www.youtube.com/watch?v={yt_id}"
    else:
        # = for long urls and / for short urls
        s = "=" if "=" in yt_url else "/"
        yt_id = yt_url.split(s)[-1]

    # Build the final output path
    sound_path = str(sounds.DOWNLOAD_PATH / f"{yt_id}.wav")

    # If cache then dont't download again
    if use_cache and os.path.isfile(sound_path):
        return sound_path

    # Prepare the parameters needed by youtube_dl
    outtmpl = str(sounds.DOWNLOAD_PATH / "%(id)s.%(ext)s")
    ydl_opts = {
        "format": "bestaudio/best",
        "outtmpl": outtmpl,
        "postprocessors": [
            {
                "key": "FFmpegExtractAudio",
                "preferredcodec": "wav",
                "preferredquality": "120",
            }
        ],
    }

    # Download the audio. Dissable all prints
    with open(os.devnull, "w") as fp, redirect_stdout(fp):
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([yt_url])

    if not os.path.isfile(sound_path):
        raise SnakeNotFoundError("Ups! Something went wrong.")

    return sound_path


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DECORATOR
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def zzz(method=None, *, when_start=False, when_finish=True, when_error=False):
    """Sound decorator to notify the execution status of a function.

    Parameters
    ----------
    method: callable
        Function, class method or any callable object. SnakeJazz will track
        the strating and finishing event and play the desired sound.
    when_start: string, path, optional
        Path to the sound file that will be played at the same instant that
        the execution of 'method' starts. A new process handles the
        reproduction of the sound.
    when_finish: string, path, optional
        Path to the sound file that will be played at the same instant that
        the execution of 'method' ends. A new process handles the
        reproduction of the sound.
    when_error: string, path, optional
        Path to the sound file that will be played if an exception occurs
        during the execution of 'method'. If an error occurs, no finishing
        sound is played. A new process handles the reproduction of the sound.

    Notes
    -----
    SnakeJazz uses PyGame API to reproduce sounds.
    The default sounds distributed with SnakeJazz belong to the respective
    creators.

    Rhodesmas:

    >> Downloaded from https://freesound.org/people/rhodesmas/packs/17958/
    """

    @wraps(method)
    def wrapper(*args, **kwargs):

        start = _parse_param(when_start, default=DEFAULT_START)
        finish = _parse_param(when_finish, default=DEFAULT_FINISH)
        error = _parse_param(when_error, default=DEFAULT_ERROR)

        # START SOUND ----------------------------------------------------
        if start:
            start_proc = mp.Process(target=play_sound, args=(start,))
            start_proc.start()

        # EXCECUTION ----------------------------------------------------
        # Catch momentarily any exception to determine
        # if the sound must be played
        if error:
            try:
                output = method(*args, **kwargs)
            except Exception as exc:
                error_occurred = True
                raise exc
            else:
                error_occurred = False
            finally:
                if error_occurred:
                    if start:
                        start_proc.terminate()
                    error_proc = mp.Process(target=play_sound, args=(error,))
                    error_proc.start()
        else:
            output = method(*args, **kwargs)
            error_occurred = False
            if start:
                start_proc.terminate()

        # FINISH SOUND ----------------------------------------------------
        if finish and not error_occurred:
            finish_proc = mp.Process(target=play_sound, args=(finish,))
            finish_proc.start()

        return output

    # Return wrapper depending on the type of 'method'.
    # It's a function if it's used as `@snakejazz.zzz`
    # but ``None`` if used as `@snakejazz.zzz()`.
    if method is None:
        return partial(
            zzz,
            when_start=when_start,
            when_finish=when_finish,
            when_error=when_error,
        )
    else:
        return wrapper


def www(method=None, *, when_start=False, when_finish=True, when_error=False):
    """Sound decorator to notify the execution status of a function.

    Parameters
    ----------
    method: callable
        Function, class method or any callable object. SnakeJazz will track
        the strating and finishing event and play the desired sound.
    when_start: string, link, optional
        Youtube link to the audio that will be played at the same instant that
        the execution of 'method' starts. A new process handles the
        reproduction of the sound.
    when_finish: string, link, optional
        Youtube link to the audio that will be played at the same instant that
        the execution of 'method' ends. A new process handles the
        reproduction of the sound.
    when_error: string, link, optional
        Youtube link to the audio that will be played if an exception occurs
        during the execution of 'method'. If an error occurs, no finishing
        sound is played. A new process handles the reproduction of the sound.

    Notes
    -----
    SnakeJazz uses PyGame API to reproduce sounds and YoutubeDL to
    download audio from youtube videos.
    The default sounds distributed with SnakeJazz belong to the respective
    creators.

    Rhodesmas:

    >> Downloaded from https://freesound.org/people/rhodesmas/packs/17958/
    """
    start_url = _parse_url(when_start, default=DEFAULT_URL_START)
    finish_url = _parse_url(when_finish, default=DEFAULT_URL_FINISH)
    error_url = _parse_url(when_error, default=DEFAULT_URL_ERROR)

    start = get_sound(yt_url=start_url) if start_url else False
    finish = get_sound(yt_url=finish_url) if finish_url else False
    error = get_sound(yt_url=error_url) if error_url else False

    # Return wrapper depending on the type of 'method'.
    # It's a function if it's used as `@snakejazz.decorator`
    # but ``None`` if used as `@snakejazz.decorator()`.
    if method is None:
        return partial(
            zzz,
            when_start=start,
            when_finish=finish,
            when_error=error,
        )
    else:
        return zzz(
            method=method,
            when_start=start,
            when_finish=finish,
            when_error=error,
        )


def rattle(method=None, *, zound=None, url=DEFAULT_RATTLE):
    """Reproduce the sound in loop until the execution is completed.

    Parameters
    ----------
    method: callable
        Function, class method or any callable object. SnakeJazz will track
        the strating and finishing event and play the desired sound.
    zound: string, path, optional
        Path to the sound file that will be played during the execution
        of 'method'. A new process handles the reproduction of the sound.
    url: string, path, optional
        Youtube link to the audio that will be played during the execution
        of 'method'. A new process handles the reproduction of the sound.

    Notes
    -----
    SnakeJazz uses PyGame API to reproduce sounds and YoutubeDL to
    download audio from youtube videos.
    The default sounds distributed with SnakeJazz belong to the respective
    creators.

    Rhodesmas:

    >> Downloaded from https://freesound.org/people/rhodesmas/packs/17958/
    """

    @wraps(method)
    def wrapper(*args, **kwargs):

        if zound is None and isinstance(url, str):
            sound_path = get_sound(yt_url=url)
        elif isinstance(zound, str):
            sound_path = _parse_param(zound, default=None)
        proc = mp.Process(target=play_sound, args=(sound_path, -1))

        try:
            # START SOUND ----------------------------------------------------
            proc.start()
            # EXCECUTION ----------------------------------------------------
            return method(*args, **kwargs)
        finally:
            proc.terminate()

    # Return wrapper depending on the type of 'method'.
    # It's a function if it's used as `@snakejazz.rattle`
    # but ``None`` if used as `@snakejazz.rattle()`.
    if method is None:
        return partial(
            rattle,
            zound=zound,
            url=url,
        )
    else:
        return wrapper
