def factorial(num):
    num_result = num
    integer = num - 1
    while integer > 0:
        num_result = num_result * integer
        integer -= 1
    return(num_result)




num1 = int(input())
num2 = int(input())

result = factorial(num1) / factorial(num2)
print(f"{result:.2f}")
