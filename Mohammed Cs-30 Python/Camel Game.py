print ("Welcome to Dolphin!")  
print ("You have stolen a dolphin to make your way across the great red sea.")  
print ("The natives of the nation Poon, want their dolphin back and are chasing you down! Survive your")  
print ("sea trek and outswim the natives!")          

import random

miles_traveled = 0
hunger = 0
dolphin = 0
natives = 20
fish_basket = 3

done = False
while not done:
    
    print ("A. Eat a fish")  
    print ("B. Ahead moderate speed.")  
    print ("C. Ahead full speed")  
    print ("D. Stop for the night")      
    print ("E. Status Check")
    print ("F. Catch Fish")
    print ("Q. Quit")
    answer = input("")    

    if answer == "Q":
        done = True 
    elif answer == "F":
        fish_basket += 2
        dolphin -= 1
        natives = miles_traveled - random.randrange(5, 11)
    elif answer == "E":
        print ("Miles traveled:", miles_traveled)
        print ("Fish in Fish Basket:", fish_basket)
        print ("The Natives are", natives, "miles behind you!")
        print ("Hunger Bar:", hunger)
        print ("Dolphin Tiredness:", dolphin)
    elif answer == "D":
        dolphin == 0
        natives -= random.randrange(7, 14)
        print ("Dolphin is happy and is ready to go!")
    elif answer == "C":
        miles = random.randrange(10,20)
        miles_traveled += miles_traveled
        print ("You have traveled", miles, "miles!")
        hunger += 1
        dolphin = random.randrange(1, 3)
        natives = miles_traveled - random.randrange(5, 11)
    elif answer == "B":
        miles = random.randrange(10,20)
        miles_traveled += miles_traveled
        print ("You have traveled", miles, "miles!")
        hunger += 1
        dolphin += 1
        natives == miles_traveled - random.randrange(6, 13)
    elif answer == "A":
        if hunger == 0:
            print ("error")
        elif hunger >= 1:
            fish_basket -= 1 
            hunger = 0
    if hunger >= 4:
        print ("You are getting hungry!") 
    if dolphin >= 5:
        print ("Your Dolphin is Getting Tired!")
    if natives <= 15:
        print ("The natives are getting close!")
    if hunger == 6:
        print ("YOU DIED!") 
        print ("END GAME!")
        done = True
    if dolphin == 6:
        print ("YOUR DOLPHIN DIED!") 
        print ("END GAME!")
        done = True
    if natives <= 0:
        print ("YOU GOT CAUGHT")
        print ("END GAME")
        done = True
    if miles_traveled >= 200:
        print ("YOu WIN!")
        print ("END GAME!")
        done = True
    
    
    
 
      
        
        
                
    



