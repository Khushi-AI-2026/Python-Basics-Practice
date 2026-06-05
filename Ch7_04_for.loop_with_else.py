# ============================================
# FOR LOOP WITH ELSE - EXPLANATION & EXAMPLES
# ============================================

# CONCEPT:
# The else block in a for loop executes when the loop completes normally (without break).
# If break is used inside the loop, else block is skipped.

print("=" * 50)
print("EXAMPLE 1: Basic For Loop with Else")
print("=" * 50)

l = [1, 7, 8]

for item in l:
    print(item)
else:
    print("done")  # This prints when loop exhausts!

# Output: 1, 7, 8, done

print("\n" + "=" * 50)
print("EXAMPLE 2: For Loop with Break (Else NOT Executed)")
print("=" * 50)

numbers = [1, 2, 3, 4, 5]

for num in numbers:
    if num == 3:
        print(f"Found {num}, breaking loop!")
        break
    print(num)
else:
    print("Loop completed successfully!")  # This will NOT print

# Output: 1, 2, Found 3, breaking loop!

print("\n" + "=" * 50)
print("EXAMPLE 3: Searching in a List (Practical Use Case)")
print("=" * 50)

numbers = [2, 4, 6, 8, 10]
search = 5

for num in numbers:
    if num == search:
        print(f"Found {search} in the list!")
        break
else:
    print(f"{search} is NOT in the list!")

# Output: 5 is NOT in the list!

print("\n" + "=" * 50)
print("EXAMPLE 4: Another Search Example (Item Found)")
print("=" * 50)

numbers = [2, 4, 6, 8, 10]
search = 6

for num in numbers:
    if num == search:
        print(f"Found {search} in the list!")
        break
else:
    print(f"{search} is NOT in the list!")

# Output: Found 6 in the list!

print("\n" + "=" * 50)
print("EXAMPLE 5: Check if String Contains Vowels")
print("=" * 50)

word = "xyz"

for char in word:
    if char.lower() in "aeiou":
        print(f"Vowel found: {char}")
        break
else:
    print(f"No vowels found in '{word}'!")

# Output: No vowels found in 'xyz'!

print("\n" + "=" * 50)
print("KEY POINTS:")
print("=" * 50)
print("✓ Else executes when loop completes normally")
print("✓ Else is SKIPPED if break statement is used")
print("✓ Useful for search operations and validations")
print("✓ Python feature not available in many other languages")
