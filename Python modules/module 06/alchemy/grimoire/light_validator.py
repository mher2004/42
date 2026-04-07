from alchemy.grimoire import light_spellbook


def validate_ingredients(ingredients: str) -> str:
    text = ""
    # from .light_spellbook import light_spell_allowed_ingredients
    ingredients = ingredients.lower()
    allowed = [
        word.lower(

        ) for word in light_spellbook.light_spell_allowed_ingredients()]
    if ingredients in allowed:
        text += f"{ingredients}: VALID "
    else:
        text += f"{ingredients}: INVALID "
    return text
