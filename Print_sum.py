#Question: Input two numbers and print sum

print("=" * 60)
print("METHOD 1: Simple print (सधारण तरीका)")
print("=" * 60)
input1 = int(input("enter first number: "))
input2 = int(input("enter second number: "))
total = input1 + input2
print("sum of the two value is:", total)

print("\n" + "=" * 60)
print("METHOD 2: Using f-string (Modern तरीका) ⭐")
print("=" * 60)
num1 = int(input("enter first number: "))
num2 = int(input("enter second number: "))
result = num1 + num2
print(f"Sum of {num1} and {num2} is {result}")

print("\n" + "=" * 60)
print("METHOD 3: Using format() method")
print("=" * 60)
a = int(input("enter first number: "))
b = int(input("enter second number: "))
addition = a + b
print("Sum of {} and {} is {}".format(a, b, addition))

print("\n" + "=" * 60)
print("METHOD 4: Direct print (बिना message के)")
print("=" * 60)
x = int(input("enter first number: "))
y = int(input("enter second number: "))
print(x + y)

print("\n" + "=" * 60)
print("METHOD 5: Fancy format with emoji")
print("=" * 60)
num_a = int(input("enter first number: "))
num_b = int(input("enter second number: "))
sum_result = num_a + num_b
print(f"✨ Sum of {num_a} and {num_b} is {sum_result}")

print("\n" + "=" * 60)
print("METHOD 6: Using str concatenation")
print("=" * 60)
first = int(input("enter first number: "))
second = int(input("enter second number: "))
total_sum = first + second
print("Sum = " + str(total_sum))

print("\n" + "=" * 60)
print("METHOD 7: Multiple operations and print")
print("=" * 60)
p = int(input("enter first number: "))
q = int(input("enter second number: "))
sum_pq = p + q
print(f"➕ {p} + {q} = {sum_pq}")
print(f"❌ {p} × {q} = {p * q}")
print(f"➖ {p} - {q} = {p - q}")
print(f"➗ {p} / {q} = {p / q:.2f}")
