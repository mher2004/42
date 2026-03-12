players = {
    'Alice': [2000, ['first_kill', 'level_10', 'treasure_hunter']],
    'Bob': [1500, ['level_10', 'treasure_hunter', 'boss_slayer']],
    'Grno': [2800, ['speed_demon', 'perfectionist']],
    'Bxdo': [2200, ['treasure_hunter', 'speed_demon']]
    }
scores = {'high': 3, 'medium': 2, 'low': 1}
print("=== Game Analytics Dashboard ===\n")

print("=== List Comprehension Examples ===")
high = [key for key, value in players.items() if value[0] >= 2000]
double = [value[0]*2 for value in players.values()]
active = [key for key, value in players.items() if len(value[1]) > 2]
print("High scorers (>2000):", high)
print("Scores doubled:", double)
print("Active players: ", active)

print("\n=== Dict Comprehension Examples ===")
dt = {key: value[0] for key, value in players.items()}
sc = {key: value for key, value in scores.items()}
count = {key: len(value[1]) for key, value in players.items()}
print("Player scores:", dt)
print("Score categories:", sc)
print("Achievement counts:", count)

print("\n=== Set Comprehension Examples ===")
test_regions = ["n", "n", "a", "a", "v"]
names = {val for val in players.keys()}
achiv = {a for i in players.values() for a in i[1]}
unique_regions = {a for a in test_regions}
print("Unique players:", names)
print("Unique achivements:", achiv)
print("Active regions:", unique_regions)

print("\n=== Combined Analysis ===")
print("Total players:", len(players))
print("Total unique achivements:", len(achiv))
print("Average score:", sum(dt.values())/len(players))
print("Top performer:", max(dt), f"({dt[max(dt)]} points,\
 {len(players[max(dt)][1])} achivements)")
