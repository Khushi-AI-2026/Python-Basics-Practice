OOPs ek programming style hai jisme hum real-world objects (jaise car, student, etc.) ko code ke through represent karte hain.
🔑 Main Concepts of OOPs in Python
1. Class
Class ek blueprint hota hai (design/template).
Python
class Student:
    pass
2. Object
Object class ka instance hota hai (real use).
Python
s1 = Student()
3. Constructor (__init__)
Object create hote hi automatically call hota hai.
Python
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("Rahul")
print(s1.name)
4. Encapsulation
Data + functions ko ek jagah bind karna.
Python
class Student:
    def __init__(self, name):
        self.name = name
5. Inheritance
Ek class dusri class ke properties use karti hai.
Python
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    pass

d = Dog()
d.speak()
6. Polymorphism
Same function, different behavior.
Python
class Dog:
    def sound(self):
        print("Bark")

class Cat:
    def sound(self):
        print("Meow")

for obj in (Dog(), Cat()):
    obj.sound()
7. Abstraction
Important cheeze dikhana, unnecessary hide karna.
Python
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass



class Dog:
    # 1. 'self' को मत भूलना, ये सबसे ज़रूरी है!
    def __init__(self, name, breed):
        self.name = name    # अब हमने नाम को 'name' डिब्बे में रखा
        self.breed = breed  # और नस्ल को 'breed' डिब्बे में

    # 2. ये फंक्शन सिर्फ भौंकने का काम करेगा
    def bark(self):
        print(self.name + " भोंक रहा है: भौं-भौं!")

# 3. अब 'Sheru' नाम का असली कुत्ता बनाया
sheru = Dog("Sheru", "Labrador")

# 4. अब Sheru को भौंकने के लिए कहा
sheru.bark()


class TeddyBear:
    # __init__ का मतलब है 'मशीन को सेट करना'
    def __init__(self, name, color):
        self.name = name    # टेडी का अपना नाम
        self.color = color  # टेडी का अपना रंग

    # ये वो बटन है जिसे दबाते ही टेडी बोलेगा
    def speak(self):
        print(self.name + " कह रहा है: आई लव यू! ❤️")

# अब मशीन से दो टेडी बनाए
teddy1 = TeddyBear("Chiku", "Brown")
teddy2 = TeddyBear("Miku", "Pink")

# बटन दबाया
teddy1.speak()
teddy2.speak()


class Robot:
    # 1. कोलन (:) लगाया
    def __init__(self, name, battery_power):
        # 2. ये लाइनें थोड़ी आगे खिसका दीं (Indentation)
        self.name = name
        self.battery_power = battery_power

    # 3. फंक्शन का नाम 'introduce' रखा (जैसा हमने सोचा था)
    def introduce(self):
        print("मेरा नाम " + self.name + " है और मेरी बैटरी " + str(self.battery_power) + "% है!")

# 4. सही तरीके से रोबोट बनाया
chitti = Robot("Chitti", 90)

# 5. फंक्शन को चलाया
chitti.introduce()























