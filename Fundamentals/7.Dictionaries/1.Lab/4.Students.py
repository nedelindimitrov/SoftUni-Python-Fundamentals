def students_func():
    students_dict = {}
    command = input()

    while ":" in command:
        command = command.replace(" ", "_")
        tokens = command.split(":")
        student_name = tokens[0]
        student_id = tokens[1]
        student_course = tokens[2]
        if student_course not in students_dict:
            students_dict[student_course] = {}
            students_dict[student_course][student_id] = student_name
        else:
            students_dict[student_course][student_id] = student_name

        command = input()

    for key, value in students_dict[command].items():
        print(f"{value} - {key}")


students_func()
