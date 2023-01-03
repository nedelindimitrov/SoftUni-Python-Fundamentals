number = int(input())

for i in range(1, number + 1):
    symbol = "*"
    print(i * symbol)

for i in range(number - 1, 0, -1):
    symbol = "*"
    print(i * symbol)
