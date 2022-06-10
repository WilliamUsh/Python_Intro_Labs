print("Applying your knowledge\n")

#Create a for loop that prints off the numbers 89, 41, 73, and 90 - each on their own line
numbers = [89,41,73,90]
for number in numbers:
  print(number)
print()

#Create a for loop that prints off the numbers 5 up-to but not including 15
for number in range(5,15):
  print(number, end = " ")
print("\n")

#Create a for loop that prints off the numbers 100 to 200 by 10's
for number in range(100,201,10):
  print(number, end = " ")
print("\n")

#Create a for loop that prints off the numbers from 80 to 32 by 8's
for number in range(80,31,-8):
  print(number, end = " ")
print("\n")

#Create a for loop that prints off the word Alright three times.
for i in range(3):
  print("Alright", end = " ")
print("\n")

#Using range, create a for loop that prints off the numbers 1, 4, 9, 16.
for num in range(1,5):
  print(num ** 2, end = " ")
print("\n")