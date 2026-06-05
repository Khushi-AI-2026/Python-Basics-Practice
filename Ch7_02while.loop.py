"""
WHILE LOOP - EXPLANATION AND EXAMPLES
=====================================
A while loop is used to execute a block of code repeatedly as long as a condition is True.

KEY POINTS:
-----------
1. Syntax: while(condition):
2. The loop continues until the condition becomes False
3. Must have an increment/decrement or condition update to avoid infinite loop
4. Indentation is important - statements inside loop must be indented
5. Useful when you don't know how many iterations are needed in advance
"""

# EXAMPLE 1: Basic While Loop
print("=== EXAMPLE 1: Basic While Loop ===")
i = 1
while(i < 6):
    print(i)
    i += 1
# Output: 1 2 3 4 5


# EXAMPLE 2: While Loop with Decrement
print("\n=== EXAMPLE 2: While Loop with Decrement ===")
count = 5
while(count > 0):
    print(f"Countdown: {count}")
    count -= 1
# Output: Countdown: 5, 4, 3, 2, 1


# EXAMPLE 3: While Loop with String
print("\n=== EXAMPLE 3: While Loop with String ===")
name = "Python"
index = 0
while(index < len(name)):
    print(name[index])
    index += 1
# Output: P, y, t, h, o, n


# EXAMPLE 4: While Loop with User Input (Simulated)
print("\n=== EXAMPLE 4: While Loop with Condition ===")
x = 10
while(x >= 5):
    print(f"x = {x}")
    x -= 2
# Output: x = 10, x = 8, x = 6


# EXAMPLE 5: While Loop with Break Statement
print("\n=== EXAMPLE 5: While Loop with Break ===")
num = 1
while(num <= 100):
    if num == 5:
        print("Found 5! Breaking out of loop...")
        break
    print(num)
    num += 1
# Output: 1, 2, 3, 4, Found 5! Breaking out of loop...


# EXAMPLE 6: While Loop with Continue Statement
print("\n=== EXAMPLE 6: While Loop with Continue ===")
j = 0
while(j < 5):
    j += 1
    if j == 3:
        continue  # Skip printing 3
    print(j)
# Output: 1, 2, 4, 5


# EXAMPLE 7: While Loop with Sum Calculation
print("\n=== EXAMPLE 7: While Loop - Sum of Numbers ===")
total = 0
number = 1
while(number <= 5):
    total += number
    number += 1
print(f"Sum of 1 to 5: {total}")
# Output: Sum of 1 to 5: 15


# IMPORTANT NOTES:
# - Always ensure the loop condition will eventually become False
# - Use 'break' to exit the loop prematurely
# - Use 'continue' to skip the current iteration
# - Infinite loop: while(True): will run forever unless broken with break statement
# - while(True) can be useful with break for event-driven loops
