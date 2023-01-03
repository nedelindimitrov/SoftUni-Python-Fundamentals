employees_happiness = input().split(" ")
useless_input = input()

employees_count = int(len(employees_happiness))

int_list = map(int, employees_happiness)

average_happy = float(sum(int_list) / employees_count)
happy_employees = 0

for i in range(employees_count):
    current_number = int(employees_happiness[i])
    if current_number >= average_happy:
        happy_employees += 1

if happy_employees >= (employees_count / 2):
    print(f"Score: {happy_employees}/{employees_count}. Employees are happy!")
else:
    print(f"Score: {happy_employees}/{employees_count}. Employees are not happy!")
