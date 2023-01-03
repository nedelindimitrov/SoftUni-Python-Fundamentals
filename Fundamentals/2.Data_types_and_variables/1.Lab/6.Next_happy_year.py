year_input = input()
year_int = 0
year_int = int(year_input)

year_int += 1
year_input = str(year_int)

num_digits = len(year_input)

while True:
    numbers_set = set()

    num_digits = len(year_input)

    for number in range(num_digits):
        numbers_set.add(year_input[number])

    if len(numbers_set) == len(year_input):
        print(year_input)
        break
    else:
        year_int = int(year_input)
        year_int += 1
        year_input = str(year_int)
        continue
