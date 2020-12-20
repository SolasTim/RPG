def leaderboardAdd(name, health):
    #initialises some scratch lists as blank, for use when opening/closing files
    leaderboard=[]
    #opens leaderboard file and appends to list
    lb=open("leaderboard.csv")
    for line in lb:
        leaderboard.append(line)
    lb.close()
    #formats a new entry for the leaderboard file
    entry=(name+", "+str(health)+"\n")
    leaderboard.append(str(entry))
    #rewrites leaderboard file for new formatted value
    lb=open("leaderboard.csv", "w")
    for line in leaderboard:
        lb.write(line)
    lb.close()


def leaderboardRead():
    #another scratch list
    scores=[]
    #following lines are taken and adapted from https://bit.ly/32UlHrr
    #opens leaderboard file (yes, AGAIN) and formats it in a nice way
    with open('leaderboard.csv') as f:
       for line in f:
           name, score = line.split(',')
           scores.append((int(score), name.strip()))
    #sorts based on score, in descending order
    scores.sort(reverse=True)
    #outputs scores
    print("Top 5 scores:")
    for (score, name), _ in zip(scores, range(5)):
       print(f'{name} - {score}')





