import time
import random
#This game is about a person who is trying to find the hidden treasure.
#You have a gun without bullets. You must kill the creature to get the treasure. 
#You have go to the river first to find the box
#This box contains bullets and a sword
#You can use the bullets to kill the ghost
#You can use the sword to kill the dragon
#You can go to the cave, kill the creature and claim the treasure.
#You can go to the checkpoint to decide where to go next.
#You have 3 trials to make a decision. If you fail to make it, you will die.
#You have 3 trials to kill the ghost. If you fail to kill it, you will die.
#You have 3 trials to kill the dragon. If you fail to kill it, you will die.
#You have 3 trials to find the box. If you fail to find them, you will die.
# You start the game with 10 points. You lose 1 point for each trial.
# You gain 1 point for finding the box.
# You gain 4 point for killing the ghost.
# You gain 4 point for killing the dragon.
# You lose 1 point for each unsuccessful trial.
# If you lost three points in a row, you will die.
# To win the game, you must have 15 points.
# You can play again if you win or lose.
current_score = 10
temp_score = current_score

def game_intro(): #introduction to the game
    global current_score
    global temp_score
    points = 0
    current_score = 10
    temp_score = current_score
    print('Welcome to the Treasure Game')
    time.sleep(1)
    print('You are searching for the hidden treasure and you ended up here.')
    time.sleep(1)
    print('You have a gun without bullets.') 
    time.sleep(1)
    print('On your left there is the treasure cave.')
    time.sleep(1)
    print('But you need to kill the creature to get the treasure.')
    time.sleep(1)
    print('The creature can be a ghost or a dragon.')
    time.sleep(1)
    print('On your right there is a river.')
    time.sleep(1)
    print('You can go to the river to find a box.')
    time.sleep(1)
    print('This box contains bullets and a sword.')
    time.sleep(1)
    print('You can use the bullets to kill the ghost.')
    time.sleep(1)
    print('You can use the sword to kill the dragon.')
    time.sleep(1)
    print('Your initial score is 10.')
    checkpoint(points)

def cave(points): #describes what happens at the cave
    global current_score
    global temp_score    
    time.sleep(1.5)
    print('You are in the cave.')
    time.sleep(1)
    global current_score
    global temp_score
    creature = ['ghost', 'dragon']
    random_creature_chosen = random.choice(creature)#randomly choose a creature
    if random_creature_chosen == 'ghost':
        ghost_names = ['killer robot','disco','caesar']
        ghost_name = random.choice(ghost_names) #randomly choose a ghost   
        time.sleep(1.5)
        print('You found a', ghost_name, 'ghost guarding the treasure.')
        time.sleep(1)
        print('You can: (a) kill the ghost  (b) go to the checkpoint')
        time.sleep(1)
        print('Enter "a" or "b"')
        ghost_decision_in_cave = input()
        for ghost_trials_in_cave in range(3):
            if ghost_decision_in_cave == 'a':
                current_score = temp_score
                if points == 1:
                    ghosts(points,ghost_name)
                elif points == 0:
                    ghosts(points,ghost_name)
            elif ghost_decision_in_cave == 'b':
                checkpoint(points)
            else :
                lose()
                print('You have', 2-ghost_trials_in_cave,  'trials left')
                print('Enter "a" or "b"')
                cave_decision = input()
    elif random_creature_chosen == 'dragon':
            print('You found a dragon guarding the treasure.')
            time.sleep(1)
            print('You can: (a) kill the dragon  (b) go to the checkpoint')
            time.sleep(1)
            print('Enter "a" or "b"')
            dragon_decision_in_cave = input()
            for drgon_trials_in_cave in range(3):
                if dragon_decision_in_cave == 'a':
                    current_score = temp_score
                    if points == 1:
                        dragon(points)
                        
                    elif points == 0:
                        dragon(points)
                elif dragon_decision_in_cave == 'b':
                    checkpoint(points)
                else :
                    lose()
                    print('You have', 2-drgon_trials_in_cave,  'trials left')
                    print('Enter "a" or "b"')
                    cave_decision = input()

                
def river(points):#river function used to describe what happens at the river
    global current_score
    global temp_score    
    time.sleep(1.5)
    if points == 0:
        print('You went to the river bank and found a cross sign near it')
        time.sleep(1.5)
        print('You can: (a) dig into it (b) return to checkpoint')
        time.sleep(1)
        print('Enter "a" or "b"')
        river_decision = input()
        for river_trials in range(3):
            if river_decision == 'a':
                print('You found the box! Now go to checkpoint')
                win()    
            elif river_decision == 'b':
                current_score = temp_score
                points = 0
                checkpoint(points)    
            else:
                lose()
                print('You have', 2-river_trials,  'trials left')
                print('Enter "a" or "b"')
                river_decision = input()
    elif points == 1:
        print('You have been here before. Go to the cave to find treasure')
        checkpoint(points)

def checkpoint(points): #function describes what happens at the checkpoint
    global current_score
    global temp_score    
    time.sleep(1.5)
    print('You are at the checkpoint.')
    time.sleep(1)
    print('Your current score is', current_score)
    if points == 1:
        time.sleep(1)
        print('You have found the box. Go to the cave to kill the creature!')
    time.sleep(1)
    print('You can: (a) go to the cave (b) go to the river')
    time.sleep(1)
    print('Enter "a" or "b"')
    cave_or_river = input()
    for the_trial in range(3):
        if cave_or_river == 'a':
            current_score = temp_score
            cave(points)    
        elif cave_or_river == 'b':
            current_score = temp_score
            river(points)    
        else: 
            lose()
            print('You have', 2-the_trial,  'trials left')
            print('Enter "a" or "b"')
            cave_or_river = input()

 
def dragon(points): #function describes what happens when encountering a dragon
    global current_score
    global temp_score    
    time.sleep(1.5)
    if points == 1:
        print('Good job! You killed the dragon!')
        kill_dragon()        
    elif points == 0:
        print('You had no sword to kill the dragon.')
        time.sleep(1)
        print('You were killed by the dragon')
        time.sleep(1)
        current_score = 0
        temp_score = current_score
        print('You have', current_score,'points')
        play_again()

def ghosts(points,ghost_name): #describes what happens when encountering the ghost
    global current_score
    global temp_score 
    if points == 1:
        if ghost_name == 'killer robot':
            time.sleep(0.5)
            print('Oh no! It is trying to kill you.')
            time.sleep(0.5)
            print('Enter "G" to use the golden bullet to kill it')
            bullet= input()
            for bullet_trials in range(3):
                if bullet == 'G':
                    print('Good job! You killed the ghost!')
                    kill_ghost()
                else:
                    lose()
                    print('You have', 2-bullet_trials,  'trials left')
                    print('Please enter the letter "G"')
                    bullet = input()
        elif ghost_name == 'disco': 
            time.sleep(0.5)
            print('Oh no! It is trying to kill you.')
            time.sleep(0.5)
            print('Enter "S" to use the silver bullet to kill it')
            bullet= input()
            for bullet_trials in range(3):
                if bullet == 'S': 
                    print('Good job! You killed the ghost!')
                    kill_ghost()
                else:
                    lose()
                    print('You have', 2-bullet_trials,  'trials left')
                    print('Please enter the letter "S"')
                    bullet = input()
        elif ghost_name == 'caesar': 
            time.sleep(0.5)
            print('Oh no! It is trying to kill you.')
            time.sleep(0.5)
            print('Enter "P" to use the platinum bullet to kill it')
            bullet= input()
            for bullet_trials in range(3):
                if bullet == 'P':
                    print('Good job! You killed the ghost!')
                    kill_ghost()
                else:
                    lose()
                    print('You have', 2-bullet_trials,  'trials left')
                    print('Please enter the letter "P"')
                    bullet = input()                
    elif points == 0:
        print('There was no bullets in the gun')
        time.sleep(2)
        print('You were killed by the ghost')
        current_score = 0
        temp_score = current_score
        print('You have', current_score,'points')
        play_again()




def play_again(): #function asks the user if they want to play again
    global current_score
    global temp_score 
    time.sleep(1)   
    print('Do you wanna play again (Y/N) ?')
    time.sleep(1)
    print('Enter "Y" or "N"')
    answer = input()
    if answer == 'Y':
        game_intro()
    elif answer == 'N':
        print('Thank you for playing. Hope you enjoyed it')
        exit()
    else:
        lose()
        for trials in range(3): #to allow user to enter Y or N 3 times
            endgame()
            print('You have ', 2-trials,  ' trials left')
            print('Enter "Y" or "N"')
            answer = input()
            if answer == 'Y':
                game_intro()
            elif answer == 'N':
                print('Thank you for playing. Hope you enjoyed it')
                exit()
        
def lose(): #decreases points by 1 for each unsuccessful trial
    global current_score
    global temp_score
    current_score = current_score - 1
    if temp_score == current_score + 3:
        time.sleep(1)
        print('You lost all your trials. You are dead.')
        time.sleep(1)
        print('You score is', current_score, 'points')
        time.sleep(1)
        play_again()

def endgame(): #endgame function used to end the game
    global current_score
    global temp_score
    current_score = current_score - 1
    if temp_score == current_score + 3:
        time.sleep(1)
        current_score = 0
        temp_score = current_score
        print('You have', current_score,'points')
        print('You lost all your trials. Game over :(')
        exit()

def win():# increases points to 11 when finding the box
    global current_score
    global temp_score
    current_score = current_score + 1
    temp_score = current_score
    if current_score == 11:
        points = 1
        checkpoint(points)
        play_again()


def kill_ghost(): # increases points to 15
    global current_score
    global temp_score
    current_score = current_score + 4
    temp_score = current_score
    if current_score == 15:
        print('You have', current_score, 'points')
        time.sleep(1)
        print('You found the treasure and won the game!')
        play_again()

def kill_dragon(): # increases points to 15
    global current_score
    global temp_score
    current_score = current_score + 4
    temp_score = current_score
    if current_score == 15:
        print('You have', current_score, 'points')
        time.sleep(1)
        print('You found the treasure and won the game!')
        play_again()


game_intro() #call the game_intro function to start the game
