'''
Title: Project 6-2 – Rock, Paper, Scissors
Author: Cody Carlton
Credits: N/A
Description: create a function that uses built in funciton library random to
play a rock, paper, scissors game against a computer.
'''
from random import randint

def rps():
    '''
    python function that plays rock paper scissors game
    and asks if the player wants to keep playing after each
    round
    
    >>> rps()
    Side 1 is s and Side 2 is p.
    The winner is Side 1!
    Do you want to play again (y or n)? y
    Side 1 is s and Side 2 is s.
    tie ... playing again
    Side 1 is s and Side 2 is p.
    The winner is Side 1!
    Do you want to play again (y or n)? n
    '''
    
    player1 = True # asigns player1 to boolean value

    while player1 == True: # while player1 is set to true the game will continue to play
        player1 = input('choose either rock, paper or scissors to begin playing: ')
        actions = ('rock', 'paper', 'scissors')
        player2 = actions[randint(0,2)] # sets player twos actions to choose between variabls asigned to actions
        print('side 1 is', player1, 'and side 2 is', player2) # lets the player know their choice and the opponents choice

        if player1 == player2: # conditional statement if game ends in tie
            print('tie... playing again')
            player1 = True # continues while loop from top
            
        elif player1 == 'rock': # conditional statement for possible outcomes if player1 picks rock
            if player2 == 'paper':
                print('the winner is side 2!')
            if player2 == 'scissors':
                print("the winner is side 1")
                      
        elif player1 == 'paper': # conditional statement for possible outcomes if player1 picks paper
            if player2 == 'rock':
                print('the winner is side 1!')
            if player2 == 'scissors':
                print('the winner is side 2!')
                      
        elif player1 == 'scissors':
            if player2 == 'rock':
                print('the winner is side 2!')
            if player2 == 'paper':
                print('the winner is side 1!')
        replay = input("would you like to play again y or n?: ") # replay takes input y or n and asigns them to boolean values
        "y" == True # y continues while loop
        "n" == False # n breaks while loop by returning player1 as false
        if replay == "y":
            player1 = True
        if replay == "n":
            player1 = False

    
            
rps()
    
