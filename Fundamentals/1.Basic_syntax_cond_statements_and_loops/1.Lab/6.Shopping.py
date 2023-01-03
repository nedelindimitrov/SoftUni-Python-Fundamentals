budget = int(input())

while True:
    command = input()

    if command == "End":
        print("You bought everything needed.")
        break

    current_sum = int(command)

    if current_sum <= budget:
        budget -= current_sum

    else:
        print("You went in overdraft!")
        break
