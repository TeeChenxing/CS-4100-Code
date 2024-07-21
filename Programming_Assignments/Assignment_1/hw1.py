import time
import numpy as np
import copy
import random
from gridgame import *

##############################################################################################################################

# You can visualize what your code is doing by setting the GUI argument in the following line to true.
# The render_delay_sec argument allows you to slow down the animation, to be able to see each step more clearly.

# For your final submission, please set the GUI option to False.

# The gs argument controls the grid size. You should experiment with various sizes to ensure your code generalizes.

##############################################################################################################################

grid_size = 7

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

# input()   # <-- workaround to prevent PyGame window from closing after execute() is called, for when GUI set to True. Uncomment to enable.

####################################################
# Timing your code's execution for the leaderboard.
####################################################

start = time.time()  # <- do not modify this.

##########################################
# Write all your code in the area below. 
##########################################

print(f"Grid Size: {grid_size}")

def evaluator1(action_list):
    for cell_action in action_list:
        for action in cell_action:
            g, ps, d = execute(action) 

    return g, ps, d


def evaluator2(action_list):
    for action in action_list:
        g, ps, d = execute(action) 

    return g, ps, d


def pretty_print_actions(action_list):
    cell_count = 1
    for cell_action in action_list:
        print(f"Cell {cell_count}: {cell_action}")
        print()
        cell_count += 1


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
        temp = []
        temp.append(placements[i])
        if index < len(movements):
            temp.append(movements[index])
            temp.append(colors[index])
            index += 1
        
        action.append(temp)
    
    return action


def move_back_sequence(size):
    move_back_to_beginning = ['up'] * size
    if size % 2 != 0:
        move_back_to_beginning += ['left'] * size
    else:
        move_back_to_beginning.append('switchcolor')
    return move_back_to_beginning


def generate_random_solution(action_list):
    all_actions = []
    move_back = move_back_sequence(grid_size)

    num_of_shapes = 9
    last_g, last_ps, last_d = None, None, None

    # Valid Shapes
    valid_shapes_1 = [3, 5] 
    valid_shapes_2 = [1, 8]
    valid_shapes_3 = [0]

    action_list_copy_1 = copy.deepcopy(action_list)
    for cell_action in action_list_copy_1:
        random_shape = random.choice(valid_shapes_1)  # Choose a random number from valid_shapes_1
        switchshape_list = ['switchshape'] * random_shape  # Create a list with 'switchshape' repeated random_number times

        # Insert the switchshape_list at the beginning of the cell_action
        cell_action[0:0] = switchshape_list

        # Make sure we switch shapes again to get back to the first shape
        if random_shape != 0:
            reset_list = ['switchshape'] * (num_of_shapes - random_shape)
            insert_index = random_shape + 1
            cell_action[insert_index:insert_index] = reset_list  # Append the reset_list after "place"

        # grid, placedShapes, done
        evaluator2(cell_action)

    all_actions.append(action_list_copy_1)

    evaluator2(move_back)
    all_actions.append(move_back)

    action_list_copy_2 = copy.deepcopy(action_list)
    for cell_action in action_list_copy_2:
        random_shape = random.choice(valid_shapes_2)  # Choose a random number from valid_shapes_3
        switchshape_list = ['switchshape'] * random_shape  # Create a list with 'switchshape' repeated random_number times

        # Insert the switchshape_list at the beginning of the cell_action
        cell_action[0:0] = switchshape_list

        # Make sure we switch shapes again to get back to the first shape
        if random_shape != 0:
            reset_list = ['switchshape'] * (num_of_shapes - random_shape)
            insert_index = random_shape + 1
            cell_action[insert_index:insert_index] = reset_list  # Append the reset_list after "place"

        # grid, placedShapes, done
        evaluator2(cell_action)

    all_actions.append(action_list_copy_2)

    evaluator2(move_back)
    all_actions.append(move_back)

    action_list_copy_3 = copy.deepcopy(action_list)
    for cell_action in action_list_copy_3:
        random_shape = random.choice(valid_shapes_3)  # Choose a random number from valid_shapes_3
        switchshape_list = ['switchshape'] * random_shape  # Create a list with 'switchshape' repeated random_number times

        # Insert the switchshape_list at the beginning of the cell_action
        cell_action[0:0] = switchshape_list

        # Make sure we switch shapes again to get back to the first shape
        if random_shape != 0:
            reset_list = ['switchshape'] * (num_of_shapes - random_shape)
            insert_index = random_shape + 1
            cell_action[insert_index:insert_index] = reset_list  # Append the reset_list after "place"

        # grid, placedShapes, done
        g, ps, d = evaluator2(cell_action)

        last_g, last_ps, last_d = g, ps, d

    all_actions.append(action_list_copy_3)

    return last_g, last_ps, last_d, all_actions
    
movements = grid_movement(grid_size)
default_actions = create_default_action_list(movements, grid_size)

# setup(GUI=False, render_delay_sec=0.0, gs=grid_size)
# grid, placedShapes, done, all_actions = generate_random_solution(default_actions)

# print(all_actions[4])
# print(grid, placedShapes, done)

# print(len(all_actions))

# Initialize variables to store the desired g and ps
results = []
for i in range(10):
    setup(GUI=False, render_delay_sec=0.0, gs=grid_size)
    execute('export')
    g, ps, d, a = generate_random_solution(default_actions)
    
    # Store the values in the list
    results.append((g, ps, d, a))

# Initialize variables to None
grid, placedShapes, done, actions = None, None, None, None 

# Iterate through the results to find the first tuple where d is True
for g, ps, d, a in results:
    if d:
        grid, placedShapes, done, actions = g, ps, d, a
        break

# Print the selected tuple
print("Selected grid:", grid)
print("Selected placedShapes:", placedShapes)
print("Selected done:", done)
print("Selected Actions: ", actions)

########################################

# Do not modify any of the code below. 

########################################

end = time.time()

# Save the grid to a text file
np.savetxt(f'grid.txt', grid, fmt="%d")

# Save the placed shapes to a text file
with open(f"shapes.txt", "w") as outfile:
    outfile.write(str(placedShapes))

# Save the elapsed time to a text file
with open(f"time.txt", "w") as outfile:
    outfile.write(str(end-start))