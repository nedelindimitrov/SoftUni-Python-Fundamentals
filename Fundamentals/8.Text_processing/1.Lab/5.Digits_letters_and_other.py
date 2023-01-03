single_string = input()

digits = ""
words = ""
other = ""

for symbol in single_string:
    if symbol.isalpha():
        words += symbol
    elif symbol.isdigit():
        digits += symbol
    else:
        other += symbol

print(digits)
print(words)
print(other)
