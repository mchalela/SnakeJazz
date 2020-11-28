# SnakeJazz


SnakeJazz provides decorators to let you listen to the running status of your ~~Snake~~ Python functions. Most definitly inspired by Rick and Morty ;)

These are the decorators:

 - `snakejazz.zzz`:
    You can choose to reproduce a sound at the moment your function starts to excecute, when it finishes or when an error occurs. A different sound for each event can be given. 

 - `snakejazz.www`:
    Exactly the same as zzz, but you can specify youtube links and the audio will be downloaded.

 - `snakejazz.rattle`:
    Rattle from start to finish. This will loop the sound until your function ends. You can either give a local path or a youtube link.

All three of them can be used directly to run with the default configuration. But you can also give some custom sounds for a more enjoyable moment.


# Examples
Let's say you have a function that takes some time to compute. Just plug in the decorator of your preference and you're good to go!

```python
import time
import snakejazz

@snakejazz.rattle
def wait(t):
    """Some function to simulate computing time."""
    time.sleep(t)
    return

# Put on your headphones and run it!
wait(22)
```
The `rattle` decorator will play a sound in loop until your function ends.


Now let's say you want to be notified if an error occurs during the execution of your function.
```python
import time
import snakejazz

@snakejazz.zzz(when_error=True)
def wait(t):
    """Some function to simulate computing time."""
    time.sleep(t)
    raise ValueError('Something went wrong')
    return

# Put on your headphones and run it!
wait(3)
```

# Sounds
For the moment SnakeJazz comes with one pack of 33 free sounds called Rhodesmas (available here: [link](https://freesound.org/people/rhodesmas/packs/17958/)). You can listen to them with the function snakejazz.play_sound. Just run this code:
```python

import snakejazz

for sound, path in snakejazz.sounds.RHODESMAS.items():
    print(f'Playing {sound}')
    snakejazz.play_sound(path)
```


# Documentation
You can read the full documentation here: https://snakejazz.readthedocs.io/


## Author

Martin Chalela (E-mail: tinchochalela@gmail.com)
