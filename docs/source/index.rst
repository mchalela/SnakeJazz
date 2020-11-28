.. SnakeJazz documentation master file, created by
   sphinx-quickstart on Fri Nov 27 22:47:36 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

SnakeJazz's documentation!
=====================================

.. image:: https://badge.fury.io/py/snakejazz.svg
   :target: https://badge.fury.io/py/snakejazz
   :alt: PyPI Version

.. image:: https://readthedocs.org/projects/snakejazz/badge/?version=latest
   :target: https://snakejazz.readthedocs.io/en/latest/?badge=latest
   :alt: Documentation Status

.. image:: https://travis-ci.com/mchalela/SnakeJazz.svg?branch=master
   :target: https://travis-ci.com/mchalela/SnakeJazz
   :alt: Build Status

.. image:: https://img.shields.io/badge/License-MIT-blue.svg
   :target: https://tldrlegal.com/license/mit-license
   :alt: License MIT

.. image:: https://img.shields.io/badge/Python-3.6+-blue.svg
   :target: https://www.python.org/downloads/release/python-370/
   :alt: Python 3.6+
   
**SnakeJazz** provides decorators to let you listen to the running status of your Python functions. Most definitly inspired by Rick and Morty ;)

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
