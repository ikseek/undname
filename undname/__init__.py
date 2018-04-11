import threading

from ._undname import ffi, lib

_flag_values = {
    "leading_underscores": 0x0001,
    "ms_keywords": 0x0002,
    "function_returns": 0x0004,
    "allocation_language": 0x0010,
    "thistype": 0x0060,
    "access_specifiers": 0x0080,
    "member_type": 0x0200,
    "name_only": 0x1000,
    "arguments": 0x2000,
    "complex_type": 0x8000
}


class UndnameFailure(Exception):
    pass


def undname(mangled, name_only=False, leading_underscores=True,
            ms_keywords=True, function_returns=True, allocation_language=True,
            thistype=True, access_specifiers=True, member_type=True,
            arguments=True, complex_type=True):
    args = locals()
    if args.pop('name_only'):
        no_flags = _flag_values['name_only']
    else:
        no_flags = sum(_flag_values[k] for k, v in args.items() if v is False)
    _thread_local.error_messages = []
    try:
        result = lib.undname(mangled.encode('ascii'), no_flags)
        if _thread_local.error_messages:
            raise UndnameFailure(", ".join(_thread_local.error_messages))
        else:
            demangled = ffi.string(result).decode('ascii')
            return demangled
    finally:
        lib.free(result)


@ffi.def_extern()
def error_message(severity, text):
    if severity < 2:
        _thread_local.error_messages.append(ffi.string(text).decode('ascii'))


_thread_local = threading.local()
