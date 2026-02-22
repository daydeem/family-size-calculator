def calculate_family_size(sisters: int, marriage_type: str, wives: int = 1) -> int:
    husband = 1
    sons = 9

    if marriage_type.lower() == "western":
        wives = 1
    elif marriage_type.lower() == "multiple":
        if wives < 1:
            raise ValueError("Wives must be at least 1.")
    else:
        raise ValueError("Choose 'western' or 'multiple'.")

    return husband + wives + sons + sisters


# Usage examples
result1 = calculate_family_size(sisters=1, marriage_type="western")
print("Western marriage ->", result1, "people")

result2 = calculate_family_size(sisters=1, marriage_type="multiple", wives=3)
print("3 wives ->", result2, "people")
