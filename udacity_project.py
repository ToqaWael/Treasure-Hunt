# Run the game by entering python3 adventure_game.py in the terminal
import time
import random
# This game is about a person who is trying to find the hidden treasure.
# The person has a gun without bullets. The person needs to kill the ghost to get the treasure. 
# The person can go to the river to find the bullets to kill the ghost.So the person has to go to the river first. 
# The person can go to the cave to kill the ghost and claim the treasure.
# The person can go to the checkpoint to decide where to go next.
# The person has 3 trials to make a decision. If the person fails to make a decision, the person will die.
# The person has 3 trials to kill the ghost. If the person fails to kill the ghost, the person will die.
# The person has 3 trials to find the bullets. If the person fails to find the bullets, the person will die.
# The person has 3 trials to make a decision. If the person fails to make a decision, the person will die.


def game_intro(): #introduction to the game
    points = 0
    print('Welcome to the Treasure Game')
    time.sleep(1)
    print('You are searching for the hidden treasure and you winded up here. You have a gun without bullets.') 
    time.sleep(2)
    print('On your left there the treasure cave.')
    time.sleep(1)
    print('But you need to kill the ghost to get the treasure.')
    time.sleep(1)
    print('On your right there is a river.')
    time.sleep(1)
    print('You can go to the river to find the bullets to kill the ghost.')
    checkpoint(points)


def cave(points): #cave function used to describe what happens in the cave
    time.sleep(1.5)
    print('You are in the cave.')
    time.sleep(1)
    print('You can: (a) kill the ghost and claim the treasure  (b) go to the checkpoint')
    time.sleep(1)
    print('Enter "a" or "b"')
    cave_decision = input()
    for cave_trials in range(3):
        if cave_decision == 'a':
            if points == 1:
                ghosts(points)
                
            elif points == 0:
                ghosts(points)

        elif cave_decision == 'b':
            checkpoint(points)
        else :
            if cave_trials == 2:
                print('You lost all your trials. You are dead.')
                play_again()
            print('You have', 2-cave_trials,  'trials left')
            # cave_trials += 1
            print('Enter "a" or "b"')
            cave_decision = input()
                
                

def river(points): #river function used to describe what happens at the river
    time.sleep(1.5)
    if points == 0:
        print('You went down the hill to the river bank and found a cross sign near the river')
        time.sleep(1.5)
        print('You can: (a) dig into it (b) return to checkpoint')
        time.sleep(1)
        print('Enter "a" or "b"')
        river_decision = input()
        for river_trials in range(3):
            if river_decision == 'a':
                print('You finally found the bullets to kill the ghost! Now go back to checkpoint')
                points = 1 
                checkpoint(points)    
            elif river_decision == 'b':
                points = 0
                checkpoint(points)    
            else:
                if river_trials == 2:
                    print('You lost all your trials. You are dead.')
                    play_again()
                print('You have', 2-river_trials,  'trials left')
                # river_trials += 1
                print('Enter "a" or "b"')
                river_decision = input()
    elif points == 1:
        print('You have been here before. Go to the cave to find treasure')
        checkpoint(points)


def checkpoint(points): #checkpoint function used to describe what happens at the checkpoint
    time.sleep(1.5)
    print('You are at the checkpoint. ')
    if points == 1:
        time.sleep(1)
        print('You have finally found the bullets to kill the ghost. Go to the cave to kill the ghost and find the treasure.')
    time.sleep(2)
    print('You can: (a) go to the cave (b) go to the river')
    time.sleep(1)
    print('Enter "a" or "b"')
    cave_or_river = input()
    for trials in range(3):
        if cave_or_river == 'a':
            cave(points)    
        elif cave_or_river == 'b':
            river(points)    
        else:   
            if trials == 2:
                print('You lost all your trials. You are dead.')
                play_again()
            print('You have', 2-trials,  'trials left')
            # trials += 1
            print('Enter "a" or "b"')
            cave_or_river = input()


def ghosts(points): #ghosts function used to describe what happens when you encounter the ghost
    time.sleep(1.5)
    ghost_names = ['killer robot','disco','caesar']
    ghost_name = random.choice(ghost_names) #randomly choose a ghost
    if points == 1:
        if ghost_name == 'killer robot':
            print('The killer robot is trying to kill you! Enter "G" to use the golden bullet to kill it')
            bullet= input()
            for bullet_trials in range(3):
                if bullet == 'G':
                    print('Good job! You killed the ghost!')
                    print('Congarulations! You won the treasure!')
                    play_again()
                else:
                    if bullet_trials == 2:
                        print('You lost all your trials. You are dead.')
                        play_again()
                    print('You have', 2-bullet_trials,  'trials left')
                    # bullet_trials += 1
                    print('Please enter the letter "G"')
                    bullet = input()
        elif ghost_name == 'disco': 
            print('The disco is trying to kill you! Enter "S" to use the silver bullet to kill it')
            bullet= input()
            for bullet_trials in range(3):
                if bullet == 'S': 
                    print('Good job! You killed the ghost!')
                    print('Congarulations! You won the treasure!')
                    play_again()
                else:
                    if bullet_trials == 2:
                        print('You lost all your trials. You are dead.')
                        play_again()
                    print('You have', 2-bullet_trials,  'trials left')
                    # bullet_trials += 1
                    print('Please enter the letter "S"')
                    bullet = input()
        elif ghost_name == 'caesar': 
            print('The caesar is trying to kill you! Enter "P" to use the platinum bullet to kill it')
            bullet= input()
            for bullet_trials in range(3):
                if bullet == 'P':
                    print('Good job! You killed the ghost!')
                    print('Congarulations! You won the treasure!')
                    play_again()
                else:
                    if bullet_trials == 2:
                        print('You lost all your trials. You are dead.')
                        play_again()
                    print('You have', 2-bullet_trials,  'trials left')
                    # bullet_trials += 1
                    print('Please enter the letter "P"')
                    bullet = input()
    elif points == 0:
        print('There was no bullets in the gun')
        time.sleep(2)
        print('You were killed by the ghost')
        play_again()


def play_again(): #play again function used to ask the user if they want to play again
    print('Do you wanna play again (Y/N) ?')
    print('Enter "Y" or "N"')
    answer = input()
    if answer == 'Y':
        game_intro()
    elif answer == 'N':
        print('Thank you for playing. Hope you enjoyed it')
        exit()
    else:
        for trials in range(3): #if the user enters something other than Y or N, they will be asked to enter Y or N again
            if trials == 2: #if the user enters something other than Y or N 3 times, the game will exit
                print('You lost all your trials. Good Bye! :D')
                exit()
            print('You have ', 2-trials,  ' trials left')
            # trials += 1
            print('Enter "Y" or "N"')
            answer = input()
        



game_intro() #call the game_intro function to start the game