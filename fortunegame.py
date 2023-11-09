import random

lucky_number = random.randint(1, 100)

print('You will have a great day and your luck number is:' + str(lucky_number))

# Fortune number and text gaming program

fortune_number = random.randint(1, 3)
fortune_text = ''
if fortune_number == 1:
  fortune_text = 'You will have a great day'
elif fortune_number == 2:
  fortune_text = 'Go for a jog'
else:
  fortune_text = 'Take a roadtrip'

print(str(fortune_text), "" + 'Your lucky number is', "" + str(lucky_number))

# ,(comma) to seperate strings/words and "" for adding blank spaces
