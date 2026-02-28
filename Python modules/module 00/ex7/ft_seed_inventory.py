def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    if (unit == "packets"): 
        print(seed_type.title(),"seeds:",quantity,"packets available")
    elif (unit == "grams"):
        print(seed_type.title(),"seeds:",quantity,"grams total")
    elif (unit == "area"):
        print(seed_type.title(),"seeds:","covers",quantity,"square meters")
    else:
        print("Unknown unit type")
