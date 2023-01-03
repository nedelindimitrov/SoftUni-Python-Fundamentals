our_list = ["", "", "", "", "", "", "", "", "", "", ""]

command = input()

while command != "End":
    current_command = command.split("-")
    current_addional = current_command[1]
    current_index = int(current_command[0])
    our_list[current_index] = current_addional

    command = input()

new_list = [x for x in our_list if x != ""]

print(new_list)
