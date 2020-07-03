#creating hangman

#needs a time and random module so I will import that
import time
import random
#let's ask the user a basic question
name=input("What is your name? \n")
print ("Hello," + name, ". It is time to play hangman!")
print("Are you ready?")
#wait for 1 second
time.sleep(1)

print("Start guessing " + name, "\n")
time.sleep(0.5)
#the word for this game is gonna be chosen at random out of these choices
WORDS= ("Python" , "SQL Coding" , "Coding" , 'Binary Coded Decimal', 'Router' , 'Java', 'Ruby')
word = random.choice(WORDS)
#La variable with an empty value
guesses= " "
#only 10 turns to guess the word
turns = 10
#to check if there are more than zero turns
while turns > 0:
    #make a counter that starts with zero
    failed = 0
    #for every character in the secret_word
    for char in word:
        #see if the character is in the players guess
        if char in guesses:
            print (" "+ char),
        else:
            #if not found, print a dash
            print("_"),
            #and increase the failed counter with one
            failed += 1
            
    #if failed is equal to zero
    if failed == 0:
        print("You won " + name)

        #exit the script
        break
    print

    #ask the user go guess a character
    guess = input("guess a character:")

    #set the players guess to guesses
    guesses += guess
    #if the guess is not found in the secret word
    if guess not in word:
        #turns counter decreases by one (now 9)
        turns-= 1
        print("Wrong")
        #how many turns are left
        print("You have", + turns, " more guesses")
        #if the turns are equal to zero the game is over
        if turns == 0:
            #print "You Loose"
            print("You lose, better luck next time! The word was " + word)
            
            
