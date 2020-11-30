<!--
*** Thanks for checking out the Best-README-Template. If you have a suggestion
*** that would make this better, please fork the repo and create a pull request
*** or simply open an issue with the tag "enhancement".
*** Thanks again! Now go create something AMAZING! :D
***
***
***
*** To avoid retyping too much info. Do a search and replace for the following:
*** github_username, repo_name, twitter_handle, email, project_title, project_description
-->



<!-- PROJECT SHIELDS -->
<!--
*** I'm using markdown "reference style" links for readability.
*** Reference links are enclosed in brackets [ ] instead of parentheses ( ).
*** See the bottom of this document for the declaration of the reference variables
*** for contributors-url, forks-url, etc. This is an optional, concise syntax you may use.
*** https://www.markdownguide.org/basic-syntax/#reference-style-links
-->
[![PyPI version](https://badge.fury.io/py/snakejazz.svg)](https://badge.fury.io/py/snakejazz)
[![Documentation Status](https://readthedocs.org/projects/snakejazz/badge/?version=latest)](https://snakejazz.readthedocs.io/en/latest/?badge=latest)
[![Build Status](https://travis-ci.com/mchalela/SnakeJazz.svg?branch=master)](https://travis-ci.com/mchalela/SnakeJazz)
[![Coverage Status](https://coveralls.io/repos/github/mchalela/SnakeJazz/badge.svg)](https://coveralls.io/github/mchalela/SnakeJazz)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)
[![Python 3.6+](https://img.shields.io/badge/python-3.6+-blue.svg)](https://www.python.org/downloads/release/python-370/)



<!-- PROJECT LOGO -->
<br />
<p align="center">
  <a href="https://github.com/mchalela/SnakeJazz">
    <img src="res/snakejazz.png" alt="Logo" width="175" height="175">
  </a>

  <h3 align="center">SnakeJazz</h3>

  <p align="center">
    Decorators for sound reproduction
    <br />
    <a href="https://snakejazz.readthedocs.io"><strong>Explore the docs »</strong></a>
    <br />
    <br />
    <a href="#basic-usage">View Demo</a>
    ·
    <a href="https://github.com/mchalela/SnakeJazz/issues">Report Bug</a>
    ·
    <a href="https://github.com/mchalela/SnakeJazz/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details close>
  <summary><b>Table of Contents</b></summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#standard-installation">Standard Installation</a></li>
        <li><a href="#development-install">Development Install</a></li>
      </ul>
    </li>
    <li><a href="#basic-usage">Basic Usage</a></li>
    <li><a href="#roadmap">Sounds</a></li>
    <li><a href="#contributing">Contributing</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#author">Author</a></li>
    <li><a href="#acknowledgements">Acknowledgements</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

SnakeJazz provides decorators to let you listen to the running status of your ~~Snake~~ Python functions. Most definitly inspired by Rick and Morty :wink: 

These are the decorators:

 - `snakejazz.zzz`:
    You can choose to reproduce a sound at the moment your function starts to excecute, when it finishes or when an error occurs. A different sound for each event can be given. 

 - `snakejazz.www`:
    Exactly the same as zzz, but you can specify youtube links and the audio will be downloaded.

 - `snakejazz.rattle`:
    Rattle from start to finish. This will loop the sound until your function ends. You can either give a local path or a youtube link.

All three of them can be used directly to run with the default configuration. But you can also give some custom sounds for a more enjoyable moment.

<!-- GETTING STARTED -->
## Getting Started

There are two simple steps to have SnakeJazz running on you python scripts.

### Prerequisites

SnakeJazz works with ffmpeg library for audio processing. To install it simply run:
* apt
  ```console
  sudo apt update
  sudo apt install ffmpeg
  ```


* dnf
  ```console
  sudo dnf install ffmpeg
  ```

You will also need a nice set of headphones to run SnakeJazz. :headphones:

### Installation

1. Standard Installation
   ```console
   pip install snakejazz
   ```


2. Development Install
   ```console
   git clone https://github.com/mchalela/SnakeJazz.git
   cd SnakeJazz
   pip install -e .
   ```


<!-- USAGE EXAMPLES -->
## Basic Usage

Let's say you have a function that takes some time to compute. Just plug-in the decorator of your preference and you're good to go!

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



<!-- SOUNDS -->
## Sounds
For the moment SnakeJazz comes with one pack of 33 free sounds called Rhodesmas (available here: [link](https://freesound.org/people/rhodesmas/packs/17958/)). You can listen to them with the function snakejazz.play_sound. Just run this code:
```python

import snakejazz

for sound, path in snakejazz.sounds.RHODESMAS.items():
    print(f'Playing {sound}')
    snakejazz.play_sound(path)
```


<!-- CONTRIBUTING -->
## Contributing

This is an open source project made to be shared. Any contributions you make are **greatly appreciated**.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.


<!-- AUTHOR -->
## Author

Martin Chalela - email: tinchochalela@gmail.com

Project Link: [https://github.com/mchalela/SnakeJazz](https://github.com/mchalela/SnakeJazz)



<!-- ACKNOWLEDGEMENTS -->
## Acknowledgements

* <div>Rhodesmas sounds created by <a href="https://freesound.org/people/rhodesmas/" title="rhodesmas">rhodesmas</a> from <a href="https://freesound.org/people/rhodesmas/packs/17958/" title="Freesound">Freesound</a>.</div>


* <div>Snake and Saxophone icons: Icons made by <a href="https://www.flaticon.com/authors/freepik" title="Freepik">Freepik</a> from <a href="https://www.flaticon.com/" title="Flaticon">www.flaticon.com</a>.</div>
