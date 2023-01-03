number = int(input())

for f in range(0, number):
    for s in range(0, number):
        for t in range(0 , number):
            print(f"{chr(97 + f)}{chr(97 + s)}{chr(97 + t)}")
