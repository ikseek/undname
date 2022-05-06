#include <ctype.h>
#include <stdarg.h>
#include <stddef.h>
#include <string.h>

typedef void* (*malloc_func_t)(size_t);
typedef void  (*free_func_t)(void*);

/* __unDName/__unDNameEx flags */
#define UNDNAME_NO_LEADING_UNDERSCORES   (0x0001) /* Don't show __ in calling convention */
#define UNDNAME_NO_MS_KEYWORDS           (0x0002) /* Don't show calling convention at all */
#define UNDNAME_NO_FUNCTION_RETURNS      (0x0004) /* Don't show function/method return value */
#define UNDNAME_NO_ALLOCATION_LANGUAGE   (0x0010)
#define UNDNAME_NO_THISTYPE              (0x0060)
#define UNDNAME_NO_ACCESS_SPECIFIERS     (0x0080) /* Don't show access specifier (public/protected/private) */
#define UNDNAME_NO_MEMBER_TYPE           (0x0200) /* Don't show static/virtual specifier */
#define UNDNAME_NAME_ONLY                (0x1000) /* Only report the variable/method name */
#define UNDNAME_NO_ARGUMENTS             (0x2000) /* Don't show method arguments */
#define UNDNAME_NO_COMPLEX_TYPE          (0x8000)

typedef int BOOL;
typedef char CHAR;

#define WINE_DEFAULT_DEBUG_CHANNEL(name)
#define WINAPIV
#define TRUE 1
#define FALSE 0
#define lstrcpynA strncpy
#define CDECL
#define debugstr_a(x) (x)

#define ERROR_MESSAGE(severity, ...) { \
    int needed = snprintf(NULL, 0, __VA_ARGS__); \
    char* buffer = malloc(needed); \
    snprintf(buffer, needed, __VA_ARGS__); \
    error_message(severity, buffer); \
    free(buffer); \
}

#define ERR(...) ERROR_MESSAGE(0, __VA_ARGS__ )
#define WARN(...) ERROR_MESSAGE(1, __VA_ARGS__ )

#ifdef NDEBUG
#define TRACE(...) 
#else
#define TRACE(...) ERROR_MESSAGE(2, __VA_ARGS__ )
#endif

extern void error_message(int severity, const char* message);
