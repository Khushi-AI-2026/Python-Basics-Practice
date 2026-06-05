# problem1: write a program to find a greatedt of 4 number entered by the user
a1 = int(input("enter number 1: "))
a2 = int(input("enter number 2: "))
a3 = int(input("enter number 3: "))
a4 = int(input("enter number 4: "))

if(a1>a2 and a1>a3 and a1>a3):
   print("greatest number is a1 :",a1)
  
elif(a2>a1 and a2>a3 and a2>a4):
   print("greatest number is a2: ",a2)

elif(a3>a1 and a3>a2 and a3>a4):
   print("greatest number is a3: ",a3)

elif(a4>a1 and a4>a2 and a4>a3):
   print("greatest number is a4: ",a4)

# problem2: write a program to check wheather students pass or failed if it requires total 40% and at least 33% in each subject to pass and we have to assume three subjects 

marks1 = int(input("enter marks 1: "))
marks2 = int(input("enter marks 2: "))
marks3 = int(input("enter marks 3: "))

#check for total percentage
total_percentage = (100*(marks1 + marks2 + marks3))/300

if(total_percentage>=40 and marks1>=33 and marks2>=33 and marks3>=33):
   print("you are pass",total_percentage)

else:
   print("you failed, try again next year!",total_percentage)

# problem3: a spam comment is defined as a text containing following keywords if this word is used in any comment, then it will be considered as a spam
 IN keyword
p1 = "make a lot of money"
p2 = "buy now"
p3 = "subscribe this"
p4 = "click this"

message = input("enter your comment: ")
if((p1 in message) or ( p2 in message) or ( p3 in message) or ( p4 in message))

   print(" this comment is a spam")
else:
   print("this comment is not a spam")

# problem4: write a program to find a wheather a given username contains less than 10 character or not.
 username = input("enter username")

if(len(username)<10):
  print("your username contains less than 10 character")

else:
  print("your username more than or equal to 10 character")

# problem5: write a program which finds out wheather a given number name is present in a list or not.

l = ["khushi","rohan","shubham"]

name = input("enter your name: ")

if(name is 1):
  print("your name is in the list")

else:
  print("your name is not in the list")
  
#problem6 write a program to calculate the grade of a student from the following scheme

marks = int(input("enter your marks: "))

if(marks<=100 and marks>=90):
   grade = "Ex"
elif(marks<=90 and marks>=80):
   grade = "A"
elif(marks<=80 and marks>=70):
   grade = "B"
elif(marks<=70 and marks>=60):
   grade = "C"
elif(marks<=60 and marks>=50):
   grade = "D"
elif(marks<=50):
   grade = "F"

print("your grade is:" grade)

#problem7: write a program to find out the given wheather a give post is khushi or not

post = "hey khushi is good khushi is very good and khushi is great"

post = input("enter the post")


if("khushi".lower() is post.lower()):
  print("this post is talking about khushi")
  
else:
  print("this post is not talking about khushi")












