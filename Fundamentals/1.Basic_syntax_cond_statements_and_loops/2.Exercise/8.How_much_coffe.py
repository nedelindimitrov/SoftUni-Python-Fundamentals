coffees = 0

while True:
    current = input()
    if current == "coding" or current == "dog" or current == "cat" or current == "movie":
        coffees += 1
    elif current == "CODING" or current == "DOG" or current == "CAT" or current == "MOVIE":
        coffees += 2
    else:
        if current == "END":
            break
        else:
            pass

if coffees <= 5:
    print(coffees)
else:
    print("You need extra sleep")
