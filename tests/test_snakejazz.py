import os

from unittest.mock import MagicMock, patch

import pytest

import snakejazz


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

def test_mixer_play(default_finish):
    with patch("pygame.mixer") as mock_mixer:
        mock_mixer.music.get_busy = MagicMock(return_value=False)
        snakejazz.play_sound(default_finish)
    mock_mixer.music.get_busy.assert_called()
    mock_mixer.music.unload.assert_called_once()

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test _parse_param
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_parse_param_True():
    result = snakejazz._parse_param(True, "foo")
    assert result == "foo"

def test_parse_param_False():
    result = snakejazz._parse_param(False, "foo")
    assert result is False

def test_parse_param_None():
    result = snakejazz._parse_param(None, "foo")
    assert result is False

def test_parse_param_invalid_type():
    with pytest.raises(ValueError):
        result = snakejazz._parse_param(42, "foo")

def test_parse_param_invalid_file():
    valid_path = snakejazz.DEFAULT_START
    invalid_path = valid_path.replace('.wav', '.mp3')
    with pytest.raises(FileNotFoundError):
        result = snakejazz._parse_param(invalid_path, valid_path)

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# Test default files exist
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

def test_defaults_exist():    
    assert os.path.isfile(snakejazz.DEFAULT_START)
    assert os.path.isfile(snakejazz.DEFAULT_FINISH)
    assert os.path.isfile(snakejazz.DEFAULT_ERROR)
    
def test_RHODESMAS():
    for name, path in snakejazz.sounds.RHODESMAS.items():
        assert os.path.isfile(path)