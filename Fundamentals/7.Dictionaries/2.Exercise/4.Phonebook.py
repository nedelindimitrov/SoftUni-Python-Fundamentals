phone_dict = {}

command = input()

while "-" in command:
    phone_info = command.split("-")
    name = phone_info[0]
    number = phone_info[1]

    phone_dict[name] = number

    command = input()

number = int(command)

for i in range(number):
    search_name = input()

    if search_name in phone_dict:
        print(f"{search_name} -> {phone_dict[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")
