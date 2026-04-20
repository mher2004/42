try:
    from alchemy.grimoire import dark_spellbook
    print(dark_spellbook)
except NameError:
    print("Hi")
finally:
    print("=== Kaboom 1 ===")
    print("Access to alchemy/grimoire/dark_spellbook.py directly")
    print("Test import now - THIS WILL RAISE AN UNCAUGHT EXCEPTION")
