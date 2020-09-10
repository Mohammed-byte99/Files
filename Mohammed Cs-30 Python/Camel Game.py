print ("Welcome to Dolphin!")  
print ("You have stolen a camel to make your way across the great red sea.")  
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
    print ("F. Stop for the night")      
    print ("D. Status Check")
    print ("E. Quit")
    answer = input("")    

    if answer == "E":
        done = True 
    elif answer == "D":
        print ("Miles traveled:", miles_traveled)
        print ("Fish in Fish Basket:", fish_Basket)
        print ("The Natives are", natives, "miles behind you!")
    elif answer == "F":
        Dolphin == 0
        natives = random.randrange(7, 14)
        print ("Dolphin is happy and is ready to go!")



