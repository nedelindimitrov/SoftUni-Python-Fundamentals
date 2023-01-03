persons = int(input())
capacity = int(input())

if persons % capacity == 0:
    print(int(persons / capacity))
else:
    print(int(persons / capacity) + 1)
