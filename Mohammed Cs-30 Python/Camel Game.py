print ("Welcome to Dolphin!")  
print ("You have stolen a camel to make your way across the great red sea.")  
print ("The natives of the nation Poon, want their dolphin back and are chasing you down! Survive your")  
print ("sea trek and outswim the natives!")          

done = False
while not done:
    print ("A. Eat a fish")  
    print ("B. Ahead moderate speed.")  
    print ("C. Ahead full speed")  
    print ("F. Stop for the night")      
    print ("D. Status Check")
    print ("E. Quit")
    answer = input("")    

    if done == "E":
        done = True 

done = False
while not done:
    quit = input("Do you want to quit? ")
    if quit == "y":
        done = True
 
    attack = input("Does your elf attack the dragon? ")
    if attack == "y":
        print("Bad choice, you died.")
        done = True