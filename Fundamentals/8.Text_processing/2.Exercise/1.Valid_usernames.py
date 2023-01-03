usernames = input().split(", ")

for item in usernames:
    is_it_okay = True
    current_username = item
    if len(current_username) < 3 or len(current_username) > 16:
        is_it_okay = False
    for symbol in current_username:
        if symbol.isdigit() or symbol.isalpha():
            pass
        else:
            if symbol == "-" or symbol == "_":
                pass
            else:
                is_it_okay = False

    if is_it_okay:
        print(current_username)
