#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   SnakeJazz Project (https://github.com/mchalela/SnakeJazz/).
# Copyright (c) 2020, Martin Chalela
# License: MIT
#   Full Text: https://github.com/mchalela/SnakeJazz/blob/master/LICENSE


from os import path
from unittest.mock import MagicMock, patch

import pytest


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Configuration
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@pytest.fixture(autouse=True, scope="function")
def function_setup_teardown():
    # This will run for every test
    multiprocessing = MagicMock()
    multiprocessing.Process = MagicMock()
    mock_modules = {"multiprocessing.Process": multiprocessing.Process}

    module_patcher = patch.dict("sys.modules", mock_modules)
    module_patcher.start()

    # The yield runs the test
    yield

    # Now teardown
    module_patcher.stop()


@pytest.fixture
def user_function():
    def foo(t=1):
        import time

        # Simulate computing time
        time.sleep(t)
        return

    return foo


@pytest.fixture
def user_error_function():
    def foo(t=1):
        import time

        # Simulate computing time
        time.sleep(t)
        raise ValueError("Some error different to the catched Error")

    return foo


@pytest.fixture
def default_start():
    import snakejazz

    return snakejazz.sounds.RHODESMAS["connected-01.wav"]


@pytest.fixture
def default_finish():
    import snakejazz

    return snakejazz.sounds.RHODESMAS["disconnected-01.wav"]


@pytest.fixture
def default_error():
    import snakejazz

    return snakejazz.sounds.RHODESMAS["failure-01.wav"]


@pytest.fixture
def default(default_start, default_finish, default_error):
    return {
        "start": default_start,
        "finish": default_finish,
        "error": default_error,
    }


@pytest.fixture
def path_sound():
    import snakejazz

    return snakejazz.sounds.RHODESMAS["level-up-02.wav"]

@pytest.fixture
def url_sound():
    import snakejazz

    return snakejazz.sounds.RICK_AND_MORTY

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test zzz
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Wait time for the user_function and user_error_function
T = 0.01  # in seconds


@patch("multiprocessing.Process")
def test_zzz_non_callable(process, user_function):
    import snakejazz

    method_zzz = snakejazz.zzz(user_function)
    method_zzz(T)
    process.assert_called()


# Test sending a path ====================================================


@patch("multiprocessing.Process")
def test_zzz_callable_path_start(process, user_function, path_sound):
    import snakejazz

    zzz = snakejazz.zzz(
        when_start=path_sound, when_finish=False, when_error=False
    )
    method_zzz = zzz(user_function)
    method_zzz(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )


@patch("multiprocessing.Process")
def test_zzz_callable_path_finish(process, user_function, path_sound):
    import snakejazz

    zzz = snakejazz.zzz(
        when_start=False, when_finish=path_sound, when_error=False
    )
    method_zzz = zzz(user_function)
    method_zzz(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )


@patch("multiprocessing.Process")
def test_zzz_callable_path_error(
    process, user_error_function, path_sound
):
    import snakejazz

    with pytest.raises(Exception):
        zzz = snakejazz.zzz(
            when_start=False, when_finish=False, when_error=path_sound
        )
        method_zzz = zzz(user_error_function)
        method_zzz(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )


# Test sending a bool ====================================================


@patch("multiprocessing.Process")
def test_zzz_callable_bool_start(process, user_function, default_start):
    import snakejazz

    zzz = snakejazz.zzz(
        when_start=True, when_finish=False, when_error=False
    )
    method_zzz = zzz(user_function)
    method_zzz(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(default_start,)
    )


@patch("multiprocessing.Process")
def test_zzz_callable_bool_finish(
    process, user_function, default_finish
):
    import snakejazz

    zzz = snakejazz.zzz(
        when_start=False, when_finish=True, when_error=False
    )
    method_zzz = zzz(user_function)
    method_zzz(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(default_finish,)
    )


@patch("multiprocessing.Process")
def test_zzz_callable_bool_error(
    process, user_error_function, default_error
):
    import snakejazz

    with pytest.raises(Exception):
        zzz = snakejazz.zzz(
            when_start=False, when_finish=False, when_error=True
        )
        method_zzz = zzz(user_error_function)
        method_zzz(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(default_error,)
    )




# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test url
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Wait time for the user_function and user_error_function
T = 0.01  # in seconds

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_www_non_callable(process, get_sound, user_function, path_sound):
    import snakejazz

    get_sound.return_value = path_sound

    method_www = snakejazz.www(user_function)
    method_www(T)
    process.assert_called()
    get_sound.assert_called_once()


# Test sending a path ====================================================

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_www_callable_path_start(process, get_sound, user_function, path_sound, url_sound):
    import snakejazz

    get_sound.return_value = path_sound

    www = snakejazz.www(
        when_start=url_sound, when_finish=False, when_error=False
    )
    method_www = www(user_function)
    method_www(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )
    get_sound.assert_called_once()


@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_www_callable_path_finish(process, get_sound, user_function, path_sound, url_sound):
    import snakejazz

    get_sound.return_value = path_sound

    www = snakejazz.www(
        when_start=False, when_finish=url_sound, when_error=False
    )
    method_www = www(user_function)
    method_www(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )
    get_sound.assert_called_once()

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_www_callable_path_error(
    process, get_sound, user_error_function, path_sound, url_sound
):
    import snakejazz

    get_sound.return_value = path_sound

    with pytest.raises(Exception):
        www = snakejazz.www(
            when_start=False, when_finish=False, when_error=url_sound
        )
        method_www = www(user_error_function)
        method_www(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )
    get_sound.assert_called_once()


# Test sending a bool ====================================================

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_www_callable_bool_start(process, get_sound, user_function, path_sound):
    import snakejazz

    get_sound.return_value = path_sound

    www = snakejazz.www(
        when_start=True, when_finish=False, when_error=False
    )
    method_www = www(user_function)
    method_www(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )
    get_sound.assert_called_once()

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_www_callable_bool_finish(
    process, get_sound, user_function, path_sound
):
    import snakejazz

    get_sound.return_value = path_sound

    www = snakejazz.www(
        when_start=False, when_finish=True, when_error=False
    )
    method_www = www(user_function)
    method_www(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )
    get_sound.assert_called_once()

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_www_callable_bool_error(
    process, get_sound, user_error_function, path_sound
):
    import snakejazz

    get_sound.return_value = path_sound

    with pytest.raises(Exception):
        www = snakejazz.www(
            when_start=False, when_finish=False, when_error=True
        )
        method_www = www(user_error_function)
        method_www(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,)
    )
    get_sound.assert_called_once()



# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test rattle
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# Wait time for the user_function and user_error_function
T = 0.01  # in seconds

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_rattle_non_callable(process, get_sound, user_function, path_sound):
    import snakejazz

    get_sound.return_value = path_sound

    method_rattle = snakejazz.rattle(user_function)
    method_rattle(T)
    process.assert_called()
    get_sound.assert_called_once()


# Test sending a path ====================================================

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_rattle_callable_url(process, get_sound, user_function, path_sound, url_sound):
    import snakejazz

    get_sound.return_value = path_sound

    rattle = snakejazz.rattle(url=url_sound)
    method_rattle = rattle(user_function)
    method_rattle(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,-1)
    )
    get_sound.assert_called_once()

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_rattle_callable_zound(process, get_sound, user_function, path_sound):
    import snakejazz

    rattle = snakejazz.rattle(zound=path_sound)
    method_rattle = rattle(user_function)
    method_rattle(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,-1)
    )
    get_sound.assert_not_called()

@patch("snakejazz.snakejazz.get_sound")
@patch("multiprocessing.Process")
def test_rattle_callable_exception(process, get_sound, user_error_function, path_sound):
    import snakejazz

    rattle = snakejazz.rattle(zound=path_sound)
    method_rattle = rattle(user_error_function)
    with pytest.raises(Exception):
        method_rattle(T)

    process.assert_called_once_with(
        target=snakejazz.play_sound, args=(path_sound,-1)
    )
    get_sound.assert_not_called()