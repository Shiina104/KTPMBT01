def contains(lst: list, value: int) -> bool:
    if lst == None:
        return False
    for i in lst:
        if i == value:
            return True
    return False