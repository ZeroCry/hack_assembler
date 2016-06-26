hack_assembler
==============

An implementation of the assembler for the Hack computer, described on
`Chapter 6 <http://nand2tetris.org/06.php>`__ of
`"From NAND to Tetris" <http://nand2tetris.org>`__ course.

|Build Status| |Code Climate| |Test Coverage|

Installation
------------

::

    $ pip install hack_assembler

Usage
-----

Consider the following file ``Add.asm``:

::

    // This file is part of www.nand2tetris.org
    // and the book "The Elements of Computing Systems"
    // by Nisan and Schocken, MIT Press.
    // File name: projects/06/add/Add.asm

    // Computes R0 = 2 + 3

    @2
    D=A
    @3
    D=D+A
    @0
    M=D

Invoke the ``hack-assembler`` binary passing the file:

::

    $ hack-assembler Add.asm
    0000000000000010
    1110110000010000
    0000000000000011
    1110000010010000
    0000000000000000
    1110001100001000

License
-------

`Apache License
2.0 <https://github.com/thiagoalessio/hack_assembler/blob/master/LICENSE>`__.

.. |Build Status| image:: https://travis-ci.org/thiagoalessio/hack_assembler.svg?branch=master
   :target: https://travis-ci.org/thiagoalessio/hack_assembler
.. |Code Climate| image:: https://codeclimate.com/github/thiagoalessio/hack_assembler/badges/gpa.svg
   :target: https://codeclimate.com/github/thiagoalessio/hack_assembler
.. |Test Coverage| image:: https://codeclimate.com/github/thiagoalessio/hack_assembler/badges/coverage.svg
   :target: https://codeclimate.com/github/thiagoalessio/hack_assembler/coverage
