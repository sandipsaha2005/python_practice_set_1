'''The game(_) function in a program lets a user  play a game and returns the score as an integer . You need to read
a file 'hiscore.txt' which is either blank or contains the previous hi-score. You need to write a program to update
the hi-score whenever the game() breks the hi-score. '''

def game():
    return 112

score=game()
with open("hiscore.txt",) as f:
    hiscore=int(f.read())

if score>hiscore:
    with open('hiscore.txt',"w") as f:
            f.write(str(score))
             





