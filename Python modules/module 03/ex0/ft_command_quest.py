import sys

print("=== Command Quest ===")
if len(sys.argv) == 1:
    print("No arguments provided!")
else:
    i = 0
    while i < (len(sys.argv) - 1):
        print(f"Argument {i + 1}: {sys.argv[1 + i]}")
        i += 1
    print("Total arguments", i)
