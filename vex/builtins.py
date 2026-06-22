def vex_append(lst, value):
    lst.append(value)
    return None


BUILTINS = {
    "len": len,
    "append": vex_append,
}