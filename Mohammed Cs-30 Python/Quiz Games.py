print("Quiz time")

score = 0 

fingers = int(input("1.How many fingers do you have? "))
if fingers == 10:
    print("correct")    
    score += 1
else:
    print("Wrong")


temperatures = int(input("2.What temperatures is between boiling point and freezing point? "))
if temperatures > 0 and temperatures < 100:
    print("correct")
    score += 1
else:
    print("Wrong")


captial = input("3.What is the captial of Alberta? ")
if  captial == "Edmonton":
    print("correct")
    score += 1
else:
    print("Wrong")


print ("4.At least how many seeds are in a watermelon")
print ("1. 100")
print ("2. 200")
print ("3. 250")
print ("4. 300")
watermelon = int(input(""))
if watermelon == 2:
    print("correct")
    score += 1
else:
    print("Wrong")

print ("5.Who is the main character in Kung Fu Panda?")
print ("1. Mantis")
print ("2. Tigreess")
print ("3. Master Shifu")
print ("4. Po")
panda = int(input(""))
if panda == 4:
    print("correct")
    score += 1
else:
    print("Wrong")

print ("Congrutaltions your score is", score "!")



