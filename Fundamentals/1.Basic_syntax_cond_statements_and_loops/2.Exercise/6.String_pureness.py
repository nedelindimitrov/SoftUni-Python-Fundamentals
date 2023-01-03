num = int(input())

for _ in range(num):
    string = input()

    pure = True

    if "," in string or "." in string or "_" in string:
        pure = False

    if pure:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")
