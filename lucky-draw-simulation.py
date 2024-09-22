# Create a list of participant names, including 'Alex'.
# Use a while loop to repeatedly draw a name randomly from the list of participants.
# The loop should only terminate when 'Alex' is drawn.
# Ensure that the loop does not produce any output until 'Alex' is drawn.

import random

participants = ["Victoria", "Alex", "Emmy", "Phionna", "Ursula", "Klaus", "Luis", "Yuly", "Gerry", "Maria"]
#random.shuffle(participants)


while "Alex" not in random.choice(participants):
    pass

print("Congratulations Alex! You won the lucky draw!")
