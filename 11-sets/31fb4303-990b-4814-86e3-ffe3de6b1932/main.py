def remove_duplicates(spells):
    seen_spells = set()
    unique_spells = []
    for spell in spells:
        if spell not in seen_spells:
            seen_spells.add(spell)
            unique_spells.append(spell)
    return unique_spells
