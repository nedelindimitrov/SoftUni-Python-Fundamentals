num_of_wagons = int(input())
train_list = [0 for x in range(num_of_wagons)]

command = input()

while command != "End":
    current_command = command.split(" ")
    current = current_command[0]
    if current == "add":
        num_people = int(current_command[1])
        train_list[-1] += num_people
    elif current == "insert":
        index = int(current_command[1])
        num_people = int(current_command[2])
        train_list[index] += num_people
    elif current == "leave":
        index = int(current_command[1])
        num_people = int(current_command[2])
        train_list[index] -= num_people
    command = input()

print(train_list)
