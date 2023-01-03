output = ""

number = float(input())

if number < 0:
    if number < -1000000:
        output = "large negative"
    elif number > -1:
        output = "small negative"
    else:
        output = "negative"
elif number == 0:
    output = "zero"
elif number > 0:
    if number > 1000000:
        output = "large positive"
    elif number < 1:
        output = "small positive"
    else:
        output = "positive"

print(output)
