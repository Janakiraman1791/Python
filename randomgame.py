import random

print(random.randint(1, 100))

print(random.random())  #this is for float between 0 and 1

#program to print random answers
answer = random.randint(1, 3)
if answer == 1:
  print("Rock")
elif answer == 2:
  print("Paper")
else:
  print("Scissors")