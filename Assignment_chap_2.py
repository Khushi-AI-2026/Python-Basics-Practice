# ============================================================================
# QUESTION 1: DATA TYPES IN PYTHON - 4 EXAMPLES KE SAATH
# ============================================================================

# Question: What are data types in python? List any 4 with examples.
# Answer: Data types alag alag types ke data ko represent karte hain

print("=" * 50)
print("QUESTION 1: DATA TYPES IN PYTHON")
print("=" * 50)

# Data Type 1: INTEGER (int)
# Pura number jo decimal point nahi hai, integer kehte hain
number1 = 25
print(f"Integer Example: {number1}")
print(f"Data type: {type(number1)}")

# Data Type 2: FLOAT (float)
# Decimal point wale numbers ko float kehte hain
number2 = 25.5
print(f"\nFloat Example: {number2}")
print(f"Data type: {type(number2)}")

# Data Type 3: STRING (str)
# Text ya characters ko quotes mein likhte hain - isse string kehte hain
name = "Khushi"
print(f"\nString Example: {name}")
print(f"Data type: {type(name)}")

# Data Type 4: BOOLEAN (bool)
# Sirf 2 values ho sakti hain - True ya False
is_student = True
print(f"\nBoolean Example: {is_student}")
print(f"Data type: {type(is_student)}")


# ============================================================================
# QUESTION 2: IMPLICIT vs EXPLICIT TYPE CONVERSION
# ============================================================================

print("\n" + "=" * 50)
print("QUESTION 2: TYPE CONVERSION")
print("=" * 50)

# IMPLICIT TYPE CONVERSION
# Jab Python khud se ek data type ko doosre mein convert kar de
# without user ke kehe - isse implicit conversion kehte hain

print("\n--- IMPLICIT TYPE CONVERSION ---")
int_num = 10          # Integer
float_num = 5.5       # Float
result = int_num + float_num  # Python khud int ko float mein convert kar deta hai
print(f"Integer: {int_num} (type: {type(int_num).__name__})")
print(f"Float: {float_num} (type: {type(float_num).__name__})")
print(f"Result (10 + 5.5) = {result}")
print(f"Result ka type: {type(result).__name__}")
print("→ Python ne khud int ko float mein convert kar diya!")

# EXPLICIT TYPE CONVERSION
# Jab hum directly int(), float(), str() use karke conversion karte hain
# isse explicit conversion kehte hain

print("\n--- EXPLICIT TYPE CONVERSION ---")
string_number = "100"  # Yeh string hai, number nahi
print(f"String: '{string_number}' (type: {type(string_number).__name__})")
converted_int = int(string_number)  # Hum khud se int() use karke convert kar rahe hain
print(f"After int() conversion: {converted_int} (type: {type(converted_int).__name__})")
print("→ Hum ne khud se int() function use karke conversion kiya!")


# ============================================================================
# QUESTION 3: OPERATORS IN PYTHON - 3 TYPES KE SAATH
# ============================================================================

print("\n" + "=" * 50)
print("QUESTION 3: OPERATORS IN PYTHON")
print("=" * 50)

# OPERATOR TYPE 1: ARITHMETIC OPERATORS
# Ganit ke operations ke liye (+, -, *, /, %, //, **)
print("\n--- TYPE 1: ARITHMETIC OPERATORS ---")
a = 20
b = 3

print(f"a = {a}, b = {b}")
print(f"Addition (+): {a} + {b} = {a + b}")
print(f"Subtraction (-): {a} - {b} = {a - b}")
print(f"Multiplication (*): {a} * {b} = {a * b}")
print(f"Division (/): {a} / {b} = {a / b}")

# OPERATOR TYPE 2: COMPARISON OPERATORS
# Comparision karte hain (<, >, ==, !=, <=, >=)
print("\n--- TYPE 2: COMPARISON OPERATORS ---")
x = 15
y = 10

print(f"x = {x}, y = {y}")
print(f"x > y: {x > y}")        # Greater than - x bada hai y se?
print(f"x < y: {x < y}")        # Less than - x chhota hai y se?
print(f"x == y: {x == y}")      # Equal to - x aur y barabar hain?
print(f"x != y: {x != y}")      # Not equal to - x aur y alag hain?

# OPERATOR TYPE 3: LOGICAL OPERATORS
# Logic ke operations ke liye (and, or, not)
print("\n--- TYPE 3: LOGICAL OPERATORS ---")
p = True
q = False

print(f"p = {p}, q = {q}")
print(f"p and q: {p and q}")    # Dono true hone chahiye
print(f"p or q: {p or q}")      # Koi ek true ho sakta hai
print(f"not p: {not p}")        # Value ko opposite kar de


# ============================================================================
# QUESTION 4: SMART TEMPERATURE CONVERTER
# ============================================================================

print("\n" + "=" * 50)
print("QUESTION 4: TEMPERATURE CONVERTER")
print("=" * 50)

# User se input lo (string milta hai)
celsius = input("\nTemperature dein Celsius mein: ")

# Explicit type conversion - string ko float mein convert karo
# Kyunki calculation karne ke liye number chahiye
celsius = float(celsius)
print(f"Input type tha: {type(celsius).__name__} - ab {celsius} hai")

# Arithmetic operators use karte hue formulas lagao
fahrenheit = (celsius * 9/5) + 32  # Note: Formula mein 35 se 32 likha hona chahiye (standard formula)
kelvin = celsius + 273.15

# Output print karo
print(f"\n{celsius}°C equals to:")
print(f"Fahrenheit: {fahrenheit}°F")
print(f"Kelvin: {kelvin}K")
print(f"\nData types:")
print(f"Celsius: {type(celsius).__name__}")
print(f"Fahrenheit: {type(fahrenheit).__name__}")
print(f"Kelvin: {type(kelvin).__name__}")


# ============================================================================
# QUESTION 5: BILL SPLIT CALCULATOR
# ============================================================================

print("\n" + "=" * 50)
print("QUESTION 5: BILL SPLIT CALCULATOR")
print("=" * 50)

# User se input lo
total_bill = input("\nTotal bill amount batao: ")
num_friends = input("Kitne friends hain: ")

# Explicit type conversion - string ko float aur int mein convert karo
total_bill = float(total_bill)      # Float isliye taaki decimal points ho sakein
num_friends = int(num_friends)      # Int isliye kyunki friends pura number hote hain

# Division operator use karke per person bill nikalo
per_person_bill = total_bill / num_friends

# Output print karo
print(f"\nTotal Bill: {total_bill}")
print(f"Number of Friends: {num_friends}")
print(f"Per Person: {per_person_bill}")

# Har variable ka data type batao
print(f"\n--- Data Types ---")
print(f"total_bill: {type(total_bill).__name__} = {total_bill}")
print(f"num_friends: {type(num_friends).__name__} = {num_friends}")
print(f"per_person_bill: {type(per_person_bill).__name__} = {per_person_bill}")

print("\n" + "=" * 50)
print("ASSIGNMENT COMPLETE!")
print("=" * 50)
