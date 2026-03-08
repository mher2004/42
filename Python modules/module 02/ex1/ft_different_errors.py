#!/usr/bin/env python3
def garden_operations(value: int = 1,
                      file: str = '1',
                      key: str = 'Rose') -> None:
    dict = {'Rose': 5}
    int(value)
    value = value / value
    if file != '1':
        with open(file) as file:
            pass
    dict = dict[key]


def test_error_types(value: int = 1,
                     file: str = "ft_different_errors.py",
                     key: str = 'Rose') -> None:
    a = 0
    try:
        print("Testing ValueError...")
        garden_operations(value="aaa")
    except ValueError:
        print("Caught ValueError: invalid literal for int()\n")
        a = 1
    try:
        print("Testing ZeroDivisionError...")
        garden_operations(value=0)
    except ZeroDivisionError:
        print("Caught ZeroDivisionError: division by zero\n")
        a = 1
    try:
        print("Testing FileNotFoundError...")
        file_name = "Bxdo"
        garden_operations(file=file_name)
    except FileNotFoundError:
        print(f"Caught FileNotFoundError: No such file {file_name}\n")
        a = 1
    try:
        print("Testing KeyError...")
        key_name = "Bxdo"
        garden_operations(key=key_name)
    except KeyError:
        print(f"Caught KeyError: {key_name}\n")
        a = 1
    if a:
        print("Caught an error, but program continues!\n")
    else:
        print("Everything right, program continues!\n")
    print("All error types tested successfully!")


if __name__ == "__main__":
    print("=== Garden Error Types Demo ===\n")
    test_error_types()
