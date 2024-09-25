## user inputs one of three choices
## Computer randomly picks one of three choices
## If statements on what is a win, what is a loss and what is a draw <--- instead, what is a draw what is a win and 'if not' deliver loss?
## Wrong inputs that arent R, P or S should be rejected


import random



User_picks = input("Make your choice! R for Rock, P for Paper or S for Scissors?")

Computer_picks = random.choice (["R", "P", "S"])



def who_won(winning_scenario):                                ## REMEMBER to add parameters
    if User_picks == Computer_picks:
        return ("Draw")
    elif winning_scenario(User_picks, Computer_picks) == 1:     ## When you changed the parameters on line 29 for the def, this def broke. Domino effect.
        return ("You Win")
    else:
        return ("You lose")

    


def winning_scenario(User_picks, Computer_picks):
    if (User_picks == "R" and Computer_picks == "S") or (User_picks == "P" and Computer_picks == "R") or (User_picks == "S" and Computer_picks == "P"):           ## REMEMBER the fucking colon
        return 1           ## True instead on 1?





if (User_picks) not in ("R", "P", "S"):             ## Its detecting the R, not P or S          ## Also change to if not????       #if (User_picks) != ("R", "P", "S")  ->  youre comparing the User_picks to the whole tuple by using !=
    print ("Not a valid choice")
else:
    print ("You Chose", User_picks)
    print ("Opponent Chose", Computer_picks)
    print (who_won(winning_scenario))               ## When refencing a function include the parameter      
                                                    ## can we make this more efficient?   e.g else:
                                                    ##                                          print ("You Chose", User_picks \n "Opponent Chose", Computer_picks \n who_won(winning_scenario))



