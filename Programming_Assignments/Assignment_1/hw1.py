import time
import numpy as np
from gridgame import *

##############################################################################################################################

# You can visualize what your code is doing by setting the GUI argument in the following line to true.
# The render_delay_sec argument allows you to slow down the animation, to be able to see each step more clearly.

# For your final submission, please set the GUI option to False.

# The gs argument controls the grid size. You should experiment with various sizes to ensure your code generalizes.

##############################################################################################################################

setup(GUI = True, render_delay_sec = 0.0, gs = 8)

##############################################################################################################################

# Initialization

# grid represents the current state of the board. 
    
    # -1 indicates an empty cell
    # 0 indicates a cell colored in the first color (indigo by default)
    # 1 indicates a cell colored in the second color (taupe by default)
    # 2 indicates a cell colored in the third color (veridian by default)
    # 3 indicates a cell colored in the fourth color (peach by default)

# placedShapes is a list of shapes that have currently been placed on the board.
    
    # Each shape is represented as a list containing three elements: a) the brush type (number between 0-8), 
    # b) the location of the shape (coordinates of top-left cell of the shape) and c) color of the shape (number between 0-3)

    # For instance [0, (0,0), 2] represents a shape spanning a single cell in the color 2=veridian, placed at the top left cell in the grid.

# done is a Boolean that represents whether coloring constraints are satisfied. Updated by the gridgames.py file.

##############################################################################################################################

grid, placedShapes, done = execute('export')
# input()   # <-- workaround to prevent PyGame window from closing after execute() is called, for when GUI set to True. Uncomment to enable.

####################################################
# Timing your code's execution for the leaderboard.
####################################################

start = time.time()  # <- do not modify this.

##########################################
# Write all your code in the area below. 
##########################################

grid_size = len(grid)
print(f"Grid Size: {grid_size}")

def pretty_print_movements(movements, line_length):
    for i in range(0, len(movements), line_length):
        print(movements[i:i + line_length])

def grid_movement(grid_size):
    movements = []
    for current_row in range(grid_size - 1):
        if (current_row % 2 == 0):
           # Move right (grid_size - 1) times then move down
            movements.extend(["right"] * (grid_size - 1)) 
            movements.append("down")
        else:
            # Move left (grid_size - 1) times then move down
            movements.extend(["left"] * (grid_size - 1))  
            movements.append("down")

    # deal with last row of the grid
    if ((grid_size - 1) % 2 == 0):
        movements.extend(["right"] * (grid_size - 1))
    else:
        movements.extend(["left"] * (grid_size - 1))

    return movements

def create_default_action_list(movements, grid_size):
    placements = ["place"] * (grid_size ** 2)
    colors = ["switchcolor"] * (grid_size ** 2)
    
    action = []
    index = 0
    
    for i in range(len(placements)):
        action.append(placements[i])
        if index < len(movements):
            action.append(movements[index])
            action.append(colors[index])
            index += 1
    
    return action

movements = grid_movement(grid_size)
default_actions = create_default_action_list(movements, grid_size)
print(default_actions)

for action in default_actions:
    grid, placedShapes, done = execute(action)

print(grid, placedShapes, done)
input()

########################################

# Do not modify any of the code below. 

########################################

end = time.time()

# Define the directory variable... MAKE SURE TO CHANGE BEFORE SUBMITTING TO GRADESCOPE
assignment_dir = "Programming_Assignments/Assignment_1/pa1_data/"

# Save the grid to a text file
np.savetxt(f'{assignment_dir}grid.txt', grid, fmt="%d")

# Save the placed shapes to a text file
with open(f"{assignment_dir}shapes.txt", "w") as outfile:
    outfile.write(str(placedShapes))

# Save the elapsed time to a text file
with open(f"{assignment_dir}time.txt", "w") as outfile:
    outfile.write(str(end-start))