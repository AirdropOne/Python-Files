import time
name = input("What is your name?")
print ("Hello, " + name, "Time to PLay Hangman!")
print ("Start Guessing")       
word = "(secret)"
guesses = ''          
turns = 10
while turns > 0:
    failed = 0
    for char in word:
        if char in guesses:
            