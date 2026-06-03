marks = {
       "khushi": 100
      "shubham": 56,
       " rohan": 23
}

 #print(marks, type(marks))
print(marks("khushi")) #output: khushi= 100
print(marks("shubhum"))# output: Shubham= 56

student = {
    "name": "Rahul",
    "age": 20,
    "course": "BTech"
}

print(student)

print(student["name"])   # Output: Rahul


🟣 Dictionary in Python
Dictionary ek data type hai jo data ko key : value pair me store karta hai.
🔹 Features:
Curly braces {} use hoti hain
Har value ki ek unique key hoti hai
Mutable hota hai (change kar sakte ho)

Dictionary = data in key-value form

methods of dictionary:

# keys()
d = {"name": "Rahul", "age": 20}
print(d.keys())   # dict_keys(['name', 'age'])

# values()
 print(d.values())   # dict_values(['Rahul', 20])                                                      

#items()
print(d.items())   # dict_items([('name', 'Rahul'), ('age', 20)])

#get()
print(d.get("name"))   # Rahul

#update()
d.update({"age": 21})
print(d)

#pop()
d.pop("age")
print(d)

#popitem
d.popitem()
print(d)

#clear()
d.clear()
print(d)   # {}

#copy()
d2 = d.copy()

#setdefault
d.setdefault("city", "Lucknow")
print(d)








