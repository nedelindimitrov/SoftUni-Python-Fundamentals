removed_units = input().split(" ")
removed_units_count = len(removed_units)

team_a_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
team_b_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

team_a_count = 11
team_b_count = 11

game_terminated = False

for i in range(removed_units_count):
    current_unit = removed_units[i]
    current_unit = current_unit.split("-")

    current_unit_team = current_unit[0]
    current_unit_player = int(current_unit[1])

    if current_unit_team == "A":
        if current_unit_player in team_a_list:
            team_a_list.remove(current_unit_player)
            team_a_count -= 1

            if team_a_count < 7 or team_b_count < 7:
                game_terminated = True

            if game_terminated:
                break
        else:
            continue
    elif current_unit_team == "B":
        if current_unit_player in team_b_list:
            team_b_list.remove(current_unit_player)
            team_b_count -= 1

            if team_a_count < 7 or team_b_count < 7:
                game_terminated = True

            if game_terminated:
                break
        else:
            continue


print(f"Team A - {team_a_count}; Team B - {team_b_count}")

if game_terminated:
    print("Game was terminated")
