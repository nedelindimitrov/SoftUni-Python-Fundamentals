current_string = input()

new_string = ""

for i in range(len(current_string)):
    current_symbol = current_string[i]
    ord_num = int(ord(current_symbol))
    new_ord = ord_num + 3
    new_symbol = chr(new_ord)
    new_string += new_symbol

print(new_string)
