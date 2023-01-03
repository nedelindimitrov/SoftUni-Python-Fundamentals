path_file = input().split(".")

extension = path_file[1]

second_split = path_file[0].split("\\")

file_name = second_split[-1]

print(f"File name: {file_name}")
print(f"File extension: {extension}")
