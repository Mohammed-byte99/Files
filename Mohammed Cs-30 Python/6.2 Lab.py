n = int(input("Por ejemplo, para n = "))
for row in range (n):
    print ("o",end="")
print ()
for i in range (n-2):
    print ("o" + " " * (n-2) + "o")
for row in range (n):
    print ("o",end="")
print ()



