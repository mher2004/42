from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    text = ""
    ingredients = ingredients.lower()
    allowed = [word.lower() for word in dark_spell_allowed_ingredients()]
    for i in ingredients:
        if i in allowed:
            text += f"{i}: VALID "
        else:
            text += f"{i}: INVALID "
    return text
