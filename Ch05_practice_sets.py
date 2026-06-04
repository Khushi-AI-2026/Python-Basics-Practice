# ============================================
# PROBLEM 1: Hindi Dictionary with Translation
# ============================================

# Create dictionary with hindi words and english translations
words_dict = {
    "madad": "help",
    "kursi": "chair",
    "billi": "cat"
}

# Take input from user
word = input("Enter the word you want meaning of: ")

# Check if word exists and print meaning
if word in words_dict:
    print(f"Meaning: {words_dict[word]}")
else:
    print("Word not found!")


# ============================================
# PROBLEM 2: Display Unique Numbers
# ============================================

print("\n--- PROBLEM 2 ---")

# Use set to store unique numbers
unique_numbers = set()

# Take 8 numbers from user
for i in range(8):
    num = int(input(f"Enter number {i+1}: "))
    unique_numbers.add(num)

# Print unique numbers
print("Unique numbers you entered:")
print(unique_numbers)


# ============================================
# PROBLEM 3: Can set have int 18 and str "18"?
# ============================================

print("\n--- PROBLEM 3 ---")

# Create set with both int and string
my_set = {18, "18"}
print(f"Set: {my_set}")
print(f"Length: {len(my_set)}")
print("YES! Set can have both 18 (number) and '18' (text)")
print("They are different types, so set treats them as DIFFERENT values")


# ============================================
# PROBLEM 4: Length after adding 20, 20.0, "20"
# ============================================

print("\n--- PROBLEM 4 ---")

s = set()
s.add(20)
s.add(20.0)
s.add("20")

print(f"Set: {s}")
print(f"Length: {len(s)}")

print("\nWhy length is 2?")
print("- 20 (int) and 20.0 (float) are SAME in Python")
print("- So only ONE is stored")
print("- '20' (text) is DIFFERENT")
print("- So we have 2 items total: {20, '20'}")


# ============================================
# PROBLEM 5: What is the type of s = 0?
# ============================================

print("\n--- PROBLEM 5 ---")

s = 0
print(f"s = {s}")
print(f"Type of s: {type(s)}")
print(f"Answer: Type is 'int' (integer)")


# ============================================
# PROBLEM 6: 4 Friends' Favourite Languages
# ============================================

print("\n--- PROBLEM 6 ---")

# Create empty dictionary
friends_languages = {}

# Take input from 4 friends
for i in range(4):
    name = input(f"Enter name of friend {i+1}: ")
    language = input(f"What is {name}'s favourite language? ")
    
    # Store in dictionary
    friends_languages[name] = language

# Display the dictionary
print("\n--- Friends and Their Favourite Languages ---")
for friend_name, lang in friends_languages.items():
    print(f"{friend_name}: {lang}")


# ============================================
# PROBLEM 7: What if 2 friends have same name?
# ============================================

print("\n--- PROBLEM 7 ---")

print("Question: If 2 friends have same name, what happens?")
print("\nAnswer: The second entry will OVERWRITE the first entry!")
print("\nWhy? Because dictionary keys must be UNIQUE")
print("Only one value can be stored for each key")

print("\nExample:")
example = {}
example["Priya"] = "Python"
print(f"After adding Priya-Python: {example}")

example["Priya"] = "Java"
print(f"After adding Priya-Java: {example}")

print("Notice: Priya's language changed from Python to Java")
print("Python key got overwritten!")


# ============================================
# PROBLEM 8: What if 2 friends like same language?
# ============================================

print("\n--- PROBLEM 8 ---")

print("Question: If 2 friends like same language, what happens?")
print("\nAnswer: NO PROBLEM! Values CAN be duplicate in dictionary")
print("Only KEYS must be unique, not values")

print("\nExample:")
example2 = {
    "Alice": "Python",
    "Bob": "Python",
    "Charlie": "Java"
}
print(f"Dictionary: {example2}")
print("\nNotice: Both Alice and Bob like Python")
print("This is ALLOWED because keys are different")
print("Dictionary doesn't care if values repeat")


# ============================================
# PROBLEM 9: Can we change list inside set?
# ============================================

print("\n--- PROBLEM 9 ---")

print("Question: Can you change values inside a list in a set?")
print("\nAnswer: NO, you CANNOT!")

print("\nWhy?")
print("1. Lists are MUTABLE (can be changed)")
print("2. Sets require IMMUTABLE elements")
print("3. So lists CANNOT be added to sets")

print("\nExample of ERROR:")
print(">>> my_set = {8, 7, [1, 2]}")
print("TypeError: unhashable type: 'list'")

print("\nBUT tuples ARE allowed in sets (tuples are immutable):")
my_set = {8, 7, 17, "khushi", (1, 2)}
print(f"This works: {my_set}")

print("\nAnd tuples CANNOT be changed:")
print(">>> tuple_example = (1, 2)")
print(">>> tuple_example[0] = 10")
print("TypeError: 'tuple' object does not support item assignment")
