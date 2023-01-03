def math_func():
    number = int(input())

    found = True

    for n in range(number):
        current_num = int(input())
        if current_num % 2 == 0:
            pass
        else:
            print(f"{current_num} is odd!")
            found = False
            break

    if found:
        print("All numbers are even.")


math_func()
