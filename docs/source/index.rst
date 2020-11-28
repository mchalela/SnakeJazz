.. SnakeJazz documentation master file, created by
   sphinx-quickstart on Fri Nov 27 22:47:36 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SnakeJazz's documentation!
=====================================

**SnakeJazz** provides decorators to let you listen to the running status of your ~~Snake~~ Python functions. Most definitly inspired by Rick and Morty ;)

These are the decorators:

 - `snakejazz.zzz`:
    You can choose to reproduce a sound at the moment your function starts to excecute, when it finishes or when an error occurs. A different sound for each event can be given. 

 - `snakejazz.www`:
    Exactly the same as zzz, but you can specify youtube links and the audio will be downloaded.

 - `snakejazz.rattle`:
    Rattle from start to finish. This will loop the sound until your function ends. You can either give a local path or a youtube link.

All three of them can be used directly to run with the default configuration. But you can also give some custom sounds for a more enjoyable moment.


| **Author**
| Martin Chalela (E-mail: tinchochalela@gmail.com)


Repository and Issues
---------------------

https://github.com/mchalela/SnakeJazz

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   api
   installation
   licence


Indices and tables
==================

* :ref:`genindex`
* :ref:`search`
