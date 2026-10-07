def count_vowels(string: str) -> int:
    count = 0

    for char in string:
        if char in "aeiouAEIOU":
            count += 1

    return count
string = "Hello World"
print(count_vowels(string))