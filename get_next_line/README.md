*This project has been created as part of the 42 curriculum by mmkrtchy.*

📄 get_next_line
===============================================================================

🧩 DESCRIPTION
---------------
get_next_line is a core project of the 42 curriculum written in C. The goal of
this project is to implement a function capable of reading from a file
descriptor line by line, returning one line at each function call.

The difficulty of this project lies in correctly handling:
- Buffered reading using read()
- Static memory between function calls
- Memory allocation and deallocation
- Edge cases such as EOF, errors, and files without a trailing newline

This implementation is fully commented to clearly explain the logic and
algorithmic choices made throughout the project.

🎯 PROJECT GOAL
===============================================================================

Implement the following function:

    char *get_next_line(int fd);

Behavior:
- Each call returns the next line from the file descriptor `fd`
- The returned line includes the '\n' character if it exists
- Returns NULL if there is nothing more to read or if an error occurs

⚙️ INSTRUCTIONS
===============================================================================

📦 COMPILATION
---------------
Compile the project using the following command:

    cc -Wall -Wextra -Werror get_next_line.c get_next_line_utils.c

To test with a main file:

    cc -Wall -Wextra -Werror get_next_line.c \
        get_next_line_utils.c main.c

You can define the buffer size at compile time:

    cc -D BUFFER_SIZE=42 get_next_line.c get_next_line_utils.c


▶️ EXECUTION EXAMPLE
--------------------
Example usage inside a main function:

    int     fd;
    char    *line;

    fd = open("example.txt", O_RDONLY);
    while ((line = get_next_line(fd)))
    {
        printf("%s", line);
        free(line);
    }
    close(fd);

The caller is always responsible for freeing the returned line.

🧠 ALGORITHM EXPLANATION & JUSTIFICATION
===============================================================================

📌 OVERVIEW
-----------
The algorithm is based on incremental buffered reading using the read()
system call. A static variable is used to store leftover data between function
calls, allowing the function to resume reading exactly where it left off.

🛠️ CORE STEPS
--------------
1. STATIC STORAGE
   A static variable keeps unread data between calls. This is mandatory since
   local variables would be destroyed after each function call.

2. BUFFERED READING
   Data is read in chunks of size BUFFER_SIZE and appended to the static buffer
   until a newline character ('\\n') is found or EOF is reached.

3. LINE EXTRACTION
   - When a newline is found, a line is extracted from the buffer.
   - The remaining data after the newline is saved for the next call.

4. MEMORY MANAGEMENT
   - Each returned line is dynamically allocated.
   - Memory is freed appropriately to avoid leaks.
   - All allocations are checked for safety.

5. EOF HANDLING
   - If EOF is reached and leftover data exists, it is returned as the final line.
   - Subsequent calls return NULL.

✅ WHY THIS ALGORITHM?
----------------------
- Efficient: reads only what is needed
- Scalable: works with any BUFFER_SIZE
- Robust: handles all edge cases
- Compliant: respects 42 subject constraints

✨ FEATURES
===============================================================================

- Reads from a file descriptor line by line
- Handles multiple calls correctly
- Uses static memory safely
- Leak-free and error-resistant
- Fully commented for educational purposes


📚 RESOURCES
===============================================================================

📖 TECHNICAL REFERENCES
----------------------
- man read
- man open
- man malloc
- GNU C Library Documentation
  https://www.gnu.org/software/libc/manual/
- 42 get_next_line subject PDF

🤖 AI USAGE DISCLOSURE
----------------------
AI tools were used exclusively for documentation-related tasks:
- Structuring explanations
- Improving clarity of comments
- Writing this documentation block

No AI-generated code was copied into the final implementation, ensuring full
compliance with 42 academic integrity rules.
