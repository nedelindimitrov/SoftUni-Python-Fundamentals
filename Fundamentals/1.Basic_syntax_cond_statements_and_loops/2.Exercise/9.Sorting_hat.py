while True:
    name = input()

    if name == "Welcome!":
        print("Welcome to Hogwarts.")
        break

    if name == "Voldemort":
        print("You must not speak of that name!")
        break

    len_ot_name = len(name)

    if len_ot_name < 5:
        print(f"{name} goes to Gryffindor.")
    elif len_ot_name == 5:
        print(f"{name} goes to Slytherin.")
    elif len_ot_name == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len_ot_name > 6:
        print(f"{name} goes to Hufflepuff.")
