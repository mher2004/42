import sys

if len(sys.argv) == 1:
    print("Enter data please")
else:
    data = {}
    try:
        for arg in sys.argv[1:]:
            if (":" not in arg):
                raise ValueError
            if len(arg.split(":")[0]) < 1:
                raise ValueError
            if len(arg.split(":")[1]) < 1:
                raise ValueError
            if int(arg.split(":")[1]) < 0:
                raise ValueError
    except (ValueError, TypeError):
        print("Please enter valid data")
    else:
        for arg in sys.argv[1:]:
            data[arg.split(":")[0]] = int(arg.split(":")[1])
        print("=== Inventory System Analysis ===")
        quantity = 0
        for i in data.values():
            quantity += i
        print("Total items in inventory:", quantity)
        print("Unique item types:", len(data.keys()))

        print("\n=== Current Inventory ===")
        sort_data = {}
        for _ in data.items():
            max_name, max = None, -1
            for key1, value1 in data.items():
                if max < value1 and key1 not in sort_data:
                    max = value1
                    max_name = key1
            sort_data[max_name] = max
            unit = "unit" if max == 1 else "units"
            print(f"{max_name}: {max} {unit} ({(100*max/quantity):.1f}%)")

        print("\n=== Inventory Statistics ===")
        max_name, max = None, -1
        moderate = {}
        scarce = {}
        restock = {}
        for key, value in data.items():
            if value > max:
                max = value
                max_name = key
            if value >= 5:
                moderate[key] = value
            else:
                scarce[key] = value
            if value <= 1:
                restock[key] = [value]
        min_name, min = max_name, max
        for key, value in data.items():
            if value < min:
                min = value
                min_name = key
        if max > 1:
            print("Most abundant:", max_name, f"({max} units)")
        else:
            print("Most abundant:", max_name, f"({max} unit)")
        if min > 1:
            print("Least abundant:", min_name, f"({min} units)")
        else:
            print("Least abundant:", min_name, f"({min} unit)")

        print("\n=== Item Categories ===")
        print("Moderate:", moderate)
        print("Scarce:", scarce)

        print("\n=== Management Suggestions ===")
        print("Restock needed:", end=" ")
        i = 1
        for key in restock.keys():
            if i < len(restock.keys()):
                print(key + ", ", end="")
            else:
                print(key, end="\n")
            i += 1

        print("\n=== Dictionary Properties Demo ===")
        i = 1
        print("Dictionary keys:", end=" ")
        for key in data.keys():

            if i < len(data.keys()):
                print(key + ", ", end="")
            else:
                print(key, end="\n")
            i += 1
        i = 1
        print("Dictionary values:", end=" ")
        for key in data.keys():

            if i < len(data.keys()):
                print(data[key], ", ", sep="", end="")
            else:
                print(data[key], end="\n")
            i += 1
        print("Sample lookup - 'sword' in inventory:",
              True if 'sword' in data else False)
