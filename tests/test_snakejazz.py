#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   SnakeJazz Project (https://github.com/mchalela/SnakeJazz/).
# Copyright (c) 2020, Martin Chalela
# License: MIT
#   Full Text: https://github.com/mchalela/SnakeJazz/blob/master/LICENSE

import os
from unittest.mock import MagicMock, patch

import pytest

import snakejazz
from snakejazz import SnakeNotFoundError, URLError

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Fixtures
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@pytest.fixture
def method():
    def foo(t=1):
        import time

        # Simulate computing time
        time.sleep(t)
        return

    return foo


@pytest.fixture
def default_error():
    return snakejazz.sounds.RHODESMAS["failure-01.wav"]


@pytest.fixture
def default_start():
    return snakejazz.sounds.RHODESMAS["connected-01.wav"]


@pytest.fixture
def default_finish():
    return snakejazz.sounds.RHODESMAS["disconnected-01.wav"]


@pytest.fixture
def default_url():
    return snakejazz.sounds.RICK_AND_MORTY


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test _parse_param
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def test_parse_param_true():
    result = snakejazz.snakejazz._parse_param(True, "foo")
    assert result == "foo"


def test_parse_param_false():
    result = snakejazz.snakejazz._parse_param(False, "foo")
    assert result is False


def test_parse_param_none():
    result = snakejazz.snakejazz._parse_param(None, "foo")
    assert result is False


def test_parse_param_invalid_type():
    with pytest.raises(ValueError):
        snakejazz.snakejazz._parse_param(42, "foo")


def test_parse_param_invalid_file():
    valid_path = snakejazz.DEFAULT_START
    invalid_path = valid_path.replace(".wav", ".mp3")
    with pytest.raises(SnakeNotFoundError):
        snakejazz.snakejazz._parse_param(invalid_path, valid_path)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test _parse_url
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def test_parse_url_true():
    result = snakejazz.snakejazz._parse_url(True, "foo")
    assert result == "foo"


def test_parse_url_false():
    result = snakejazz.snakejazz._parse_url(False, "foo")
    assert result is False


def test_parse_url_none():
    result = snakejazz.snakejazz._parse_url(None, "foo")
    assert result is False


def test_parse_url_invalid_type():
    with pytest.raises(ValueError):
        snakejazz.snakejazz._parse_url(42, "foo")


def test_parse_url_invalid_file():
    valid_url = snakejazz.DEFAULT_URL_START
    invalid_url = valid_url.replace("://", ":/")
    with pytest.raises(URLError):
        snakejazz.snakejazz._parse_url(invalid_url, valid_url)


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test play_sound
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def test_mixer_init(default_finish):
    with patch("pygame.mixer") as mock_mixer:
        mock_mixer.music.get_busy = MagicMock(return_value=False)
        snakejazz.play_sound(default_finish)
    mock_mixer.music.get_busy.assert_called()
    mock_mixer.init.assert_called_once()


def test_mixer_load(default_finish):
    with patch("pygame.mixer") as mock_mixer:
        mock_mixer.music.get_busy = MagicMock(return_value=False)
        snakejazz.play_sound(default_finish)
    mock_mixer.music.get_busy.assert_called()
    mock_mixer.music.load.assert_called_once_with(default_finish)


def test_mixer_play(default_finish):
    with patch("pygame.mixer") as mock_mixer:
        mock_mixer.music.get_busy = MagicMock(return_value=False)
        snakejazz.play_sound(default_finish)
    mock_mixer.music.get_busy.assert_called()
    mock_mixer.music.play.assert_called_once()


def test_mixer_unload(default_finish):
    with patch("pygame.mixer") as mock_mixer:
        mock_mixer.music.get_busy = MagicMock(return_value=False)
        snakejazz.play_sound(default_finish)
    mock_mixer.music.get_busy.assert_called()
    mock_mixer.music.unload.assert_called_once()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test get_sound
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


@patch("youtube_dl.YoutubeDL.download")
def test_get_sound_defaults(mock_download):
    snakejazz.get_sound(use_cache=False)
    mock_download.assert_called_once()


@patch("youtube_dl.YoutubeDL.download")
def test_get_sound_bad_url(mock_download, default_url):
    bad_url = default_url[:-5]
    with pytest.raises(SnakeNotFoundError):
        snakejazz.get_sound(yt_url=bad_url)
    mock_download.assert_called()


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test default files exist
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~


def test_defaults_exist():
    assert os.path.isfile(snakejazz.DEFAULT_START)
    assert os.path.isfile(snakejazz.DEFAULT_FINISH)
    assert os.path.isfile(snakejazz.DEFAULT_ERROR)


def test_rhodesmas():
    for path in snakejazz.sounds.RHODESMAS.values():
        assert os.path.isfile(path)
