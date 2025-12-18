def check_ingredient_match(recipe, inventory):
    missing = []
    for ingredient in recipe:
        if (ingredient not in inventory):
            missing.append(ingredient)
    return (100 - (len(missing) / len(recipe) * 100)) , missing
