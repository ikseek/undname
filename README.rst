``undname``: CFFI wrapper for Wine MSVC name un-decorator
=======
.. image:: https://github.com/ikseek/undname/workflows/Python%20package/badge.svg
.. image:: https://img.shields.io/pypi/v/undname?style=plastic
   :target: https://pypi.org/project/undname/

Tiny cffi wrapper around patched `undname.c`_ module from `Wine`_ project.

**WARNING**: this package is built on top of pretty tricky third-party
**C code** that might have bugs **causing python interpreter to crash**.
I've fixed those I spotted myself but there might be more.
Please report if you find any input causing a crash.

Usage example:

>>> from undname import undname
>>> undname("?xyz@?$abc@V?$def@H@@PAX@@YAXXZ")
'void __cdecl abc<class def<int>,void *>::xyz(void)'

Un-decoration errors are raised as python exceptions:

>>> undname("?")
Traceback (most recent call last):
 ...
undname.UndnameFailure: Failed at...

Strings that doesn't seem to be decorated symbols are left as is

>>> undname("main")
'main'

.. _undname.c: https://github.com/wine-mirror/wine/blob/master/dlls/msvcrt/undname.c
.. _Wine: https://www.winehq.org