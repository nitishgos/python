import random
def game():
    print("You are playing the game....")
    score=random.randint(1,100)
    #Fetch the highscore
    with open("highscore.txt", "r") as f:
        hiscore=f.read()
        if(hiscore!=""):
            hiscore=int(hiscore)
        else:
            hiscore=0
    print(f"Your score is {score}")
    if(score>hiscore):
        with open("highscore.txt","w") as f:
            f.write(str(score))
    return score
game()

