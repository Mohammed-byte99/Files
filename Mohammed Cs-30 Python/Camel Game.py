print ("Welcome to Dolphin!")  
print ("You have stolen a dolphin to make your way across the great red sea.")  
print ("The natives of the nation Poon, want their dolphin back and are chasing you down! Survive your")  
print ("sea trek and outswim the natives!")          

import random

miles_traveled = 0
hunger = 0
Dolphin = 0
natives = -20
fish_Basket = 0

done = False
while not done:
    
    print ("A. Eat a fish")  
    print ("B. Ahead moderate speed.")  
    print ("C. Ahead full speed")  
    print ("D. Stop for the night")      
    print ("E. Status Check")
    print ("F. Quit")
    answer = input("")    

    if answer == "F":
        done = True 
    elif answer == "E":
        print ("Miles traveled:", miles_traveled)
        print ("Fish in Fish Basket:", fish_Basket)
        print ("The Natives are", natives, "miles behind you!")
    elif answer == "D":
        Dolphin == 0
        natives = random.randrange(7, 14)
        print ("Dolphin is happy and is ready to go!")



