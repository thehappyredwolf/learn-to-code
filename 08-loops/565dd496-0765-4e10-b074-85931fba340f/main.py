def calculate_experience_points(level):
    total_xp = 0
    
    if (level > 1):
        for i in range(1, level):
            total_xp += i * 5
            
    return total_xp
