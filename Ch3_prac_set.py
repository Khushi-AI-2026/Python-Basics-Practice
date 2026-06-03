# problem1: write a python program to display a user entered name followed by good afternoon uding input() function.

name = input("enter your name: ")

print(f"good afternoon ,{name} ")


# problem2: write a program to fill in a letter template given below with name and data .
    
letter =''' dear<| name|>
you are selected!
<|date|>  '''

print(letter.replace("<|name|>", " khushi").replace("<|date|>","24 august 2026"))

# problem3: write a program to detect double space in a string.

name = " khushi is a good  girl and "

print(name.find(" "))# ager double space hoga to yha per likh jayega ager nhi hoga to -1 likh jayega

print(name.find("khu"))# ye 9 print hoga kyuki 9 per khu stop hua h 


# problem4: replace the double space from problem 3 with single spaces.

name= " khushi is a good girl and"

print(name.replace("  "," "))# replace karega double space ko single space me

print(name)# name strung change nhi hogi  new string ko bna ker print karta h 
           #strings are immutable which means that you cannot change them by running functions on them

# proboem5: write a program to format the following letter using escape sequence characters.

letter = " dear khushi , this python course is nice. thanks!"

print(letter)# output: dear khushi,this python course is nice thanks! jo ki bahut simple lg rha h 

letter = " dear khushi,\n \t this python course is nice.\n thanks!"
# output: dear khushi
#       this python course is nice # space \t ki vajah se hui h.
#       thanks!
