def ft_count_harvest_recursive(a=1, b=0):
    if (not b):
        b = int(input("Days until harvest: "))
    if (a == b):
        print("Harvest time!")
        return
    print("Day", a)
    ft_count_harvest_recursive(a + 1, b)
