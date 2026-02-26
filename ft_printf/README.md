*This project has been created as part of the 42 curriculum by mmkrtchy.*

📄 ft_printf
===============================================================================

DESCRIPTION
===============================================================================

ft_printf is a reimplementation of the standard C library function printf.

The goal of this project is to understand how formatted output works internally
by handling variadic arguments, parsing format strings, and printing different
data types to standard output.

This project recreates the behavior of printf for a limited set of conversion
specifiers while respecting the constraints imposed by the 42 curriculum.

It is designed to strengthen low-level C programming skills, especially:
- Variadic functions
- Parsing logic
- Output formatting
- Modular code organization

INSTRUCTIONS
===============================================================================

Compilation:

Use the provided Makefile to compile the project:

    make

This will generate a static library named:

    libftprintf.a

Usage:

Include the header file in your source code:

    #include "ft_printf.h"

Compile your program with the library:

    cc main.c libftprintf.a

Example usage:

    ft_printf("Hello %s, number: %d\n", "world", 42);

Makefile rules:

- make        : compile the library
- make clean  : remove object files
- make fclean : remove object files and the library
- make re     : recompile everything

SUPPORTED CONVERSIONS
===============================================================================

The following conversion specifiers are supported:

- %c : character
- %s : string
- %p : pointer address
- %d : signed decimal integer
- %i : signed decimal integer
- %u : unsigned decimal integer
- %x : hexadecimal (lowercase)
- %X : hexadecimal (uppercase)
- %% : literal percent sign

ALGORITHM AND DATA STRUCTURE EXPLANATION
===============================================================================

Overall Algorithm:

1. ft_printf receives a format string and a variable number of arguments.
2. A va_list is initialized using va_start to access the arguments.
3. The format string is read character by character.
4. If the current character is not '%', it is written directly to stdout.
5. If a '%' is encountered:
   - The next character is interpreted as a conversion specifier.
   - The corresponding handler function is called.
6. Each handler prints its argument and returns the number of characters written.
7. The total number of printed characters is accumulated.
8. va_end is called before returning the total count.

Data Structures:

No complex data structures are used in this project.

The implementation relies on:
- va_list to manage variadic arguments
- Primitive data types (int, char, unsigned int, pointers)
- Recursive or iterative logic for number printing

This approach keeps the implementation simple, efficient, and compliant with
project constraints.

Dispatcher Logic:

A dispatcher function or conditional structure is used to route each conversion
specifier to its corresponding printing function.

Example logic:
- 'c' -> print character
- 's' -> print string
- 'd' or 'i' -> print signed integer
- 'x' or 'X' -> print hexadecimal number

Each conversion is handled by a dedicated function to improve readability,
maintainability, and modularity.

Number Printing:

Integers are printed by:
- Handling negative values explicitly
- Using division and modulo to extract digits
- Printing digits recursively or iteratively using write()

Hexadecimal values are printed using a base string:
- "0123456789abcdef" for %x
- "0123456789ABCDEF" for %X

Return Value:

Every call to write increments a counter.
ft_printf returns the total number of characters written, matching the behavior
of the original printf function.

RESOURCES
===============================================================================

Documentation and References:

- man printf
- man stdarg
- GNU C Library Documentation
- cppreference.com (Variadic Functions)

AI Usage Disclosure:

AI tools were used exclusively for:
- Understanding variadic functions (va_list, va_start, va_arg)
- Reviewing algorithm design and edge cases
- Improving documentation clarity

AI was NOT used to generate final source code or bypass project rules.
All implementation logic and code were written and validated by the author.
