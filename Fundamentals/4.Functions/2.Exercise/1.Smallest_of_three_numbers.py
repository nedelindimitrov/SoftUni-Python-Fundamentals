def smallest_num(x, y, z):
    smallest_number = x

    if y < x:
        smallest_number = y

    if z < smallest_number:
        smallest_number = z

    return smallest_number

first_num = int(input())
second_num = int(input())
third_num = int(input())

print(smallest_num(first_num, second_num, third_num))
