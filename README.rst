Lambda fork of term2048 adapted for AI play

========
term2048
========

.. image:: https://img.shields.io/travis/bfontaine/term2048.png
   :target: https://travis-ci.org/bfontaine/term2048
   :alt: Build status

.. image:: https://img.shields.io/coveralls/bfontaine/term2048/master.png
   :target: https://coveralls.io/r/bfontaine/term2048?branch=master
   :alt: Coverage status

.. image:: https://img.shields.io/pypi/v/term2048.png
   :target: https://pypi.python.org/pypi/term2048
   :alt: Pypi package

.. image:: https://img.shields.io/pypi/dm/term2048.png
   :target: https://pypi.python.org/pypi/term2048

**term2048** is a terminal-based version of 2048_.

.. _2048: http://gabrielecirulli.github.io/2048/

.. image:: https://github.com/bfontaine/term2048/raw/master/img/term2048.png

Install
-------
Clone repo

    git clone <url>

Play
----

To run in manual controls mode:
    python run.py
Then use arrow keys to move.

To run in ai solution mode:
    python run.py -ai
And watch the game!

To change the AI behaviour edit 
    term2048.ai_solution.get_move
All instructions are inside 
    ai_solution.py

