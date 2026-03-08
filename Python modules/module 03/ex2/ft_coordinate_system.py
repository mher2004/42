import sys
old_point = (0, 0, 0)
print("=== Game Coordinate System ===")


def calc_distance(old_pos: tuple, new_pos: tuple) -> float:
    return (((old_pos[0] - new_pos[0])**2 + (old_pos[1] - new_pos[1])**2
            + (old_pos[2] - new_pos[2])**2)**0.5)


if len(sys.argv) == 1:
    print("\nStarting position created: (0, 0, 0)")
    try:
        new_point = "10,20,0"
        print(f"\nParsing coordinates: {new_point}")
        new_point = tuple(int(i) for i in new_point.split(","))
    except ValueError as error:
        print("Error parsing coordinates:", error)
        print(f"Error details - Type ValueError, Args: ({error})")
    else:
        print(f"Distance between {old_point} and {new_point}:\
 {calc_distance(old_point, new_point):.2f}")
        old_point = new_point
    try:
        new_point = "3,4,0"
        print(f"\nParsing coordinates: {new_point}")
        new_point = tuple(int(i) for i in new_point.split(","))
    except ValueError as error:
        print("Error parsing coordinates:", error)
        print(f"Error details - Type ValueError, Args: ({error})")
    else:
        print(f"Distance between {old_point} and {new_point}:\
 {calc_distance(old_point, new_point):.2f}")
        old_point = new_point
    try:
        new_point = "3,4,aaa"
        print(f"\nParsing coordinates: {new_point}")
        new_point = tuple(int(i) for i in new_point.split(","))
    except ValueError as error:
        print("Error parsing coordinates:", error)
        print(f"Error details - Type ValueError, Args: ({error})")
    else:
        print(f"Distance between {old_point} and {new_point}:\
 {calc_distance(old_point, new_point):.2f}")
        old_point = new_point

    print("\nUnpacking demonstrationn:")
    print(f"Player at x={old_point[0]} y={old_point[1]} z={old_point[2]}")

else:
    print("\nStarting position created: (0, 0, 0)")
    for coordinate in sys.argv[1:]:
        try:
            print(f"\nParsing coordinates: {coordinate}")
            new_point = tuple(int(i) for i in coordinate.split(","))
        except ValueError as error:
            print("Error parsing coordinates:", error)
            print(f"Error details - Type ValueError, Args: ({error})")
        else:
            print(f"Distance between {old_point} and {new_point}:\
 {calc_distance(old_point, new_point):.2f}")
            old_point = new_point

    print("\nUnpacking demonstrationn:")
    print(f"Player at x={old_point[0]} y={old_point[1]} z={old_point[2]}")
