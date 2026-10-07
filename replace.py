def replace_char(string: str, old: str, new: str) -> str:
    result = ""

    for char in string:
        if char == old:
            result += new
        else:
            result += char

    return result


string = "banana"
old = "a"
new = "o"

print(replace_char(string, old, new))