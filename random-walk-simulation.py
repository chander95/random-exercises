# Import the random module to utilize it random selection feature
# Define a list of directions that the entity can take
# use a for loop to simulate 10 steps
# in each iteration, randomly select a direction and simulate taking a step in that direction
# Print out the direction of each step.

import random

directions =["Left", "Right", "Forward", "Back"]
random.shuffle(directions)

for direction in directions:
    print(f"Please take a step {direction}" )