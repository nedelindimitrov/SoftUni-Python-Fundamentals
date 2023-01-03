def add_and_subtract(first, second, third):
    def sum_numbers(x, y):
        return x + y


    def subtract(x, y):
        return x - y

    print(subtract(sum_numbers(first, second), third))

first_number = int(input())
second_number = int(input())
third_number = int(input())

add_and_subtract(first_number, second_number, third_number)
