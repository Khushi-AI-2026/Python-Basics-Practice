Conditional Statements ?

Program me decision lene ke liye use hote hain
Condition True ya False hoti hai
Based on result, different code execute hota hai


1. if Statement
Jab condition true ho tab code run hota hai

age = 18
if age >= 18:
    print("You can vote")

2. if-else Statement
True ho to if wala block
False ho to else wala block
Python
num = 5
if num % 2 == 0:
    print("Even")
else:
    print("Odd")


3. if-elif-else Statement
Multiple conditions check karne ke liye
Python
marks = 75

if marks >= 90:
    print("Grade A")
elif marks >= 60:
    print("Grade B")
else:
    print("Fail")

4. Nested if
Ek if ke andar dusra if
Python
num = 10

if num > 0:
    if num % 2 == 0:
        print("Positive Even")


5. Short-hand if (One-line)
Ek line me likh sakte ho
Python
age = 20
if age >= 18: print(q"Adult")


6. Short-hand if-else (Ternary)
Python
num = 7
result = "Even" if num % 2 == 0 else "Odd"
print(result)




a = int(input("enter your age: "))

if(a>=18):
   print("you are above the age of consent")
   print("good for you")

elif(a<0):
   print("you are entering an invalud age")
  
else: 
   print("you are below the age of consent")

print("end of program")
