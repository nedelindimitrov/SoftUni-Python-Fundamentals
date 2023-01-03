num = int(input())

for _ in range(num):
    current = int(input())

    if current == 88:
        print("Hello")
    elif current == 86:
        print("How are you?")
    elif current < 88:
        print("GREAT!")
    elif current > 88:
        print("Bye.")
