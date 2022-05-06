import threading

from ._undname import ffi, lib


class UndnameFailure(Exception):
    pass


def undname(mangled: str, name_only=False, leading_underscores=True,
            ms_keywords=True, function_returns=True, allocation_language=True,
            thistype=True, access_specifiers=True, member_type=True,
            arguments=True, complex_type=True) -> str:
    """
    Demangle MSVC++ linker symbol

    :param mangled: mangled C++ symbol
    :param name_only: Only report the variable/method name
    :param leading_underscores: Show __ in calling convention if enabled
    :param ms_keywords: Disable to not show calling convention at all
    :param function_returns: Show function/method return value
    :param allocation_language: Undocumented
    :param thistype: Undocumented
    :param access_specifiers: Show access specifier (public/protected/private)
    :param member_type: Show static/virtual specifier
    :param arguments: Show method arguments
    :param complex_type: Undocumented
    :return: C++ symbol

    Example:

    >>> undname("?xyz@?$abc@V?$def@H@@PAX@@YAXXZ", ms_keywords=False)
    'void abc<class def<int>,void *>::xyz(void)'

    """
    flags = 0
    if name_only:
        flags += 0x1000
    if not leading_underscores:
        flags += 0x0001
    if not ms_keywords:
        flags += 0x0002
    if not function_returns:
        flags += 0x0004
    if not allocation_language:
        flags += 0x0010
    if not thistype:
        flags += 0x0060
    if not access_specifiers:
        flags += 0x0080
    if not member_type:
        flags += 0x0200
    if not arguments:
        flags += 0x2000
    if not complex_type:
        flags += 0x8000
    _thread_local.undname_exc = None
    try:
        result = lib.undname(mangled.encode('ascii'), flags)
        if _thread_local.undname_exc:
            exc, _thread_local.undname_exc = _thread_local.undname_exc, None
            raise exc
        else:
            return ffi.string(result).decode('ascii')
    finally:
        lib.free(result)


def onerror(exception, exc_value, traceback):
    if not _thread_local.undname_exc:
        _thread_local.undname_exc = exc_value.with_traceback(traceback)


@ffi.def_extern(onerror=onerror)
def error_message(severity, text):
    if severity < 2:
        raise UndnameFailure(ffi.string(text).decode('ascii'))


_thread_local = threading.local()
