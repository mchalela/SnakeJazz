

import pytest

from unittest.mock import patch, MagicMock


# =================================================
# CONFIGURATION
# =================================================

@pytest.fixture(autouse=True, scope='function')
def function_setup_teardown():
    # This will run for every test
    multiprocessing = MagicMock()
    multiprocessing.Process = MagicMock()
    mock_modules = {
        "multiprocessing": multiprocessing,
        "multiprocessing.Process": multiprocessing.Process
        }

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
        raise ValueError('Some error different to the catched Error')
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
    return {'start': default_start, 'finish': default_finish, 'error': default_error}

@pytest.fixture
def path_sound():
    import snakejazz
    return snakejazz.sounds.RHODESMAS["level-up-02.wav"]


# =================================================
# TESTS
# =================================================

# Wait time for the user_function and user_error_function
T = 0.01  # in seconds

@patch('multiprocessing.Process')
def test_decorator_non_callable(process, user_function):
    import snakejazz

    method_dec = snakejazz.decorator(user_function)
    method_dec(T)
    process.assert_called()

# Test sending a path ====================================================

@patch('multiprocessing.Process')
def test_decorator_callable_path_start(process, user_function, path_sound):
    import snakejazz
    
    decorator = snakejazz.decorator(when_start=path_sound, when_finish=False, when_error=False)
    method_dec = decorator(user_function)
    method_dec(T)

    process.assert_called_once_with(target=snakejazz.play_sound, args=(path_sound,))

@patch('multiprocessing.Process')
def test_decorator_callable_path_finish(process, user_function, path_sound):
    import snakejazz
    
    decorator = snakejazz.decorator(when_start=False, when_finish=path_sound, when_error=False)
    method_dec = decorator(user_function)
    method_dec(T)

    process.assert_called_once_with(target=snakejazz.play_sound, args=(path_sound,))

@patch('multiprocessing.Process')
def test_decorator_callable_path_error(process, user_error_function, path_sound):
    import snakejazz
    
    with pytest.raises(Exception):
        decorator = snakejazz.decorator(when_start=False, when_finish=False, when_error=path_sound)
        method_dec = decorator(user_error_function)
        method_dec(T)

    process.assert_called_once_with(target=snakejazz.play_sound, args=(path_sound,))

# Test sending a bool ====================================================

@patch('multiprocessing.Process')
def test_decorator_callable_bool_start(process, user_function, default_start):
    import snakejazz
    
    decorator = snakejazz.decorator(when_start=True, when_finish=False, when_error=False)
    method_dec = decorator(user_function)
    method_dec(T)

    process.assert_called_once_with(target=snakejazz.play_sound, args=(default_start,))

@patch('multiprocessing.Process')
def test_decorator_callable_bool_finish(process, user_function, default_finish):
    import snakejazz
    
    decorator = snakejazz.decorator(when_start=False, when_finish=True, when_error=False)
    method_dec = decorator(user_function)
    method_dec(T)

    process.assert_called_once_with(target=snakejazz.play_sound, args=(default_finish,))

@patch('multiprocessing.Process')
def test_decorator_callable_bool_error(process, user_error_function, default_error):
    import snakejazz
    
    with pytest.raises(Exception):
        decorator = snakejazz.decorator(when_start=False, when_finish=False, when_error=True)
        method_dec = decorator(user_error_function)
        method_dec(T)

    process.assert_called_once_with(target=snakejazz.play_sound, args=(default_error,))
