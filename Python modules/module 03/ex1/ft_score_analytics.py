import sys

scores = []
print("=== Player Score Analytics ===")
if len(sys.argv) == 1:
    print("No arguments provided. Usage:\
 python3 ft_score_analytics.py <score1> <score2> ..")
else:
    i = 0
    try:
        scores = [int(i) for i in sys.argv[1:]]
    except ValueError:
        print("Please provide valid scores")
    else:
        print(f'''Scores processed: {scores}
Total players: {len(scores)}
Total score: {sum(scores)}
Average score: {sum(scores)/len(scores)}
High score: {max(scores)}
Low score: {min(scores)}
Score range: {max(scores) - min(scores)}''')
