def get_most_common_enemy(enemies_dict):
    if (enemies_dict == {}):
        return None
    else:
        highest_count_so_far = float("-inf")
        most_common_enemy = None
        for enemy in enemies_dict:
            if (enemies_dict[enemy] > highest_count_so_far):
                highest_count_so_far = enemies_dict[enemy]
                most_common_enemy = enemy
        return most_common_enemy
