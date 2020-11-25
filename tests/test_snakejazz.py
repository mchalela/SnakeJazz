

import pytest

from unittest.mock import patch, MagicMock

import snakejazz

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


def test_play_sound(default_finish):
    
    with patch('pygame.mixer') as mock_mixer:
        mock_mixer.music.get_busy = MagicMock(return_value=False)
        snakejazz.play_sound(default_finish)
    
    mock_mixer.init.assert_called()

def test_parse_param():
    result = snakejazz._parse_param(True, 'foo')
    assert result=='foo'