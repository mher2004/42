player1 = {'first_kill', 'level_10', 'treasure_hunter', 'speed_demon'}
player2 = {'first_kill', 'level_10', 'boss_slayer', 'collector'}
player3 = {'level_10', 'treasure_hunter', 'boss_slayer',
           'speed_demon', 'perfectionist'}

print("=== Achievement Tracker System ===\n")
print("Player alice achievements:", player1)
print("Player bob achievements:", player2)
print("Player charlie achievements:", player3)

print("=== Achievement Analytics ===")
print("All unique achievements:", player3.union(player1, player2))
print("Total unique achievements:", len(player3.union(player1, player2)), "\n")

print("Common to all players:", player1.intersection(player2, player3))
a = player1.intersection(player2)
b = player1.intersection(player3)
c = player2.intersection(player3)
d = player1.union(player2, player3).difference(a, b, c)
print("Rare achievements (1 player): ", d)

print("Alice vs Bob common:", player1.intersection(player2))
print("Bob unique:", player2.difference(player1, player3))
print("Charlie unique:", player3.difference(player1, player2))
