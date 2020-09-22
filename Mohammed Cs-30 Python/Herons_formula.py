print ("Heron's Formula")

def herons_formula (side_a, side_b, side_c):
    side = ((side_a + side_b + side_c) / 2)
    return ((side * (side - side_a) * (side - side_b) * (side - side_c)) ** 0.5)

side_a = int(input("Enter Side A:"))
side_b = int(input("Enter Side B:"))
side_c = int(input("Enter side C:"))   
my_result = herons_formula(side_a, side_b, side_c)
print (my_result)