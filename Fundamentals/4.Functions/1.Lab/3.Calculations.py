def calculator():
    operator = input()
    num1 = int(input())
    num2 = int(input())
    if operator == "multiply":
        print(int(num1 * num2))
    elif operator == "divide":
        print(int(num1 / num2))
    elif operator == "add":
        print(int(num1 + num2))
    elif operator == "subtract":
        print(int(num1 - num2))

calculator()
