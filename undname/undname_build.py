from pathlib import Path

import cffi

ffi_builder = cffi.FFI()
ffi_builder.cdef("""
extern void free(void*);
extern char* undname(const char* mangled, unsigned short int flags);
extern "Python+C" void error_message(int severity, const char* message);
""")

ffi_builder.set_source("undname._undname", """
typedef void* (*malloc_func_t)(size_t);
typedef void  (*free_func_t)(void*);

char* __unDName(char *,const char*,int,malloc_func_t,free_func_t,unsigned short int);

char* undname(const char* mangled, unsigned short int flags) {
    return __unDName(NULL, mangled, 0, malloc, free, flags);
}

""", sources=[str(Path(__file__).parent / "src" / "undname.c")])

if __name__ == "__main__":
    ffi_builder.compile(verbose=True)
