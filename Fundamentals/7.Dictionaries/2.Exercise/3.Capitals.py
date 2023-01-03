country_names = input().split(", ")
capital_names = input().split(", ")

final_dict = zip(country_names, capital_names)

for key, value in final_dict:
    print(f"{key} -> {value}")
