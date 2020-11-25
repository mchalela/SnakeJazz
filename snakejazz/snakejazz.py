# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# IMPORTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

import os
from functools import partial, wraps
import multiprocessing as mp
#from multiprocessing import Process

# Hide print message at import
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame

from . import sounds


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# CONSTANTS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

DEFAULT_START = sounds.RHODESMAS["connected-01.wav"]
DEFAULT_FINISH = sounds.RHODESMAS["disconnected-01.wav"]
DEFAULT_ERROR = sounds.RHODESMAS["failure-01.wav"]


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# PRIVATE FUNCTIONS
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def _parse_param(param, default):
    if param is None or param is False:
        return False
    elif param is True:
        return default
    elif os.path.isfile(str(param)):
        return str(param)
    else:
        raise FileNotFoundError(f"The sound file {param} doesn't exists.")


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# SOUND PLAYER
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def play_sound(sound_path):
    """Reproduce the sound.

    The library PyGame is used to reproduce sounds.

    Parameters
    ----------
    sound_path: string, path
        Path to the sound file.
    """
    pygame.mixer.init()
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()
    while pygame.mixer.music.get_busy():
        continue
    pygame.mixer.music.unload()
    return


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# DECORATOR
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def decorator(
    method=None, *, when_start=True, when_finish=True, when_error=True
):
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

    Acknowledgements
    ----------------
    The default sounds distributed with SnakeJazz belong to the respective
    creators.
     - Rhodesmas:
        Downloaded from https://freesound.org/people/rhodesmas/packs/17958/
    """

    @wraps(method)
    def wrapper(*args, **kwargs):

        start = _parse_param(when_start, default=DEFAULT_START)
        finish = _parse_param(when_finish, default=DEFAULT_FINISH)
        error = _parse_param(when_error, default=DEFAULT_ERROR)

        # START SOUND ----------------------------------------------------
        if isinstance(start, str):
            start_proc = mp.Process(target=play_sound, args=(start,))
            start_proc.start()

        # EXCECUTION ----------------------------------------------------
        # Catch momentarily any exception to determine
        # if the sound must be played
        if isinstance(error, str):
            try:
                output = method(*args, **kwargs)
            except Exception as exc:
                error_occurred = True
                raise exc
            else:
                error_occurred = False
            finally:
                if error_occurred:
                    error_proc = mp.Process(target=play_sound, args=(error,))
                    error_proc.start()
        else:
            output = method(*args, **kwargs)
            error_occurred = False

        # FINISH SOUND ----------------------------------------------------
        if isinstance(finish, str) and not error_occurred:
            finish_proc = mp.Process(target=play_sound, args=(finish,))
            finish_proc.start()

        return output

    # Return wrapper depending on the type of 'method'.
    # It's a function if it's used as `@snakejazz.decorator`
    # but ``None`` if used as `@snakejazz.decorator()`.
    if method is None:
        return partial(
            decorator,
            when_start=when_start,
            when_finish=when_finish,
            when_error=when_error,
        )
    else:
        return wrapper

# shortcut
zzz = decorator