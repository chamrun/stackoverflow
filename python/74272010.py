def check(val, values=None):
    if values is None:
        values = []
    values.append(val)
    return values


list1 = check("a")
list2 = check("b", [])
list3 = check("c")
pass