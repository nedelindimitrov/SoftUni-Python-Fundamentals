def grade_function():
    grade = float(input())

    if grade < 3:
        print("Fail")
    elif grade < 3.50:
        print("Poor")
    elif grade < 4.50:
        print("Good")
    elif grade < 5.50:
        print("Very Good")
    else:
        print("Excellent")

grade_function()
