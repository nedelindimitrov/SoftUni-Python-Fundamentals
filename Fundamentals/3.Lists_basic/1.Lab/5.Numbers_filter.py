number = int(input())

even = list()
odd = list()
positive = list()
negative = list()

for n in range(number):
    current_num = int(input())
    if current_num % 2 == 0 or current_num == 0:
        even.append(current_num)
    if current_num % 2 == 1:
        odd.append(current_num)
    if current_num >= 0:
        positive.append(current_num)
    if current_num < 0:
        negative.append(current_num)

command = input()

print(eval(command))
