keyword = input()
string = input()

while keyword in string:
    string = string.replace(keyword, "")

print(string)
