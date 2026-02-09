*This project has been created as part of the 42 curriculum by mmkrtchy.*

# 📚 libft

## Description

 libft is a custom C library that reimplements a selection of
   standard C library functions, along with additional utility
   functions that will be reused throughout future projects.

   The main goal of this project is to gain a deeper understanding
   of how standard library functions work internally, while
   improving skills in memory management, pointer manipulation,
   and clean code structure.

   This library serves as a foundational toolbox for all upcoming
   C projects in the 42 curriculum.


##Instructions


   Compilation:
     Use the provided Makefile to compile the library.

     make        -> compiles libft.a
     make clean  -> removes object files
     make fclean -> removes object files and libft.a
     make re     -> recompiles the library

   Usage:
     Include the header file in your source code:
       #include "libft.h"

     Compile your program with:
       gcc main.c -L. -lft

##Library Description

   The libft library is composed of several groups of functions:

   1. Libc Functions
      Reimplementations of standard C functions such as:
      strlen, memcpy, memset, bzero, atoi, and strdup.

   2. String Manipulation
      Functions for handling strings, including:
      substr, strjoin, strtrim, split, and strmapi.

   3. Memory Management
      Functions for allocating and manipulating memory safely,
      including calloc and related helpers.

   4. Character Classification and Conversion
      Functions such as isalpha, isdigit, isalnum,
      isascii, isprint, toupper, and tolower.

   5. File Descriptor Output
      Functions to write characters, strings, and numbers
      to a given file descriptor.
 
   All functions are implemented according to the 42 Norm,
   without using forbidden functions and with proper
   protection against memory leaks and undefined behavior.

##Resources

   References:

   - Linux man pages (man 3)

   AI Usage:

   - AI was used to clarify function behavior and edge cases.
   - AI assisted in writing the text for readme and writing tests for the functions.
   - All code implementations were written, tested, and reviewed
     by the project author.
    
##Notes
   libft is intended to be reused in all future C projects
   within the 42 curriculum.

   It provides a reliable and consistent set of utilities
   that follow strict coding standards and best practices.

