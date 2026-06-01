# Program: Do numbers ka sum, difference, product aur comparison

# User se do numbers input lena
num1 = int(input("Pehla number enter karo: "))
num2 = int(input("Doosra number enter karo: "))

# Sum calculate karna
sum = num1 + num2
print(f"Sum: {sum}")

# Difference calculate karna (pehla - doosra)
difference = num1 - num2
print(f"Difference: {difference}")

# Product calculate karna
product = num1 * num2
print(f"Product: {product}")

# Check karna ki pehla number bada hai ya nahi
if num1 > num2:
    print(f"{num1} bada hai {num2} se")
else:
    print(f"{num1} chhota hai ya barabar hai {num2} ke")
