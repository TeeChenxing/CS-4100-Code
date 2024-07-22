import time
import numpy as np
import copy
import random
import json
from gridgame import *

##############################################################################################################################

# You can visualize what your code is doing by setting the GUI argument in the following line to true.
# The render_delay_sec argument allows you to slow down the animation, to be able to see each step more clearly.

# For your final submission, please set the GUI option to False.

# The gs argument controls the grid size. You should experiment with various sizes to ensure your code generalizes.

##############################################################################################################################

grid_size = 7
num_of_shapes = 9

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

def execute_instructions(action_list):
    # can execute instructions on lists of any depth (1D, 2D, 3D, etc)
    if isinstance(action_list[0], list):
        for sublist in action_list:
            g, ps, d = execute_instructions(sublist)
    else:
        for action in action_list:
            g, ps, d = execute(action)

    return g, ps, d


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
    return [move_back_to_beginning]


def choose_shape_sequence(action_list, valid_shapes):
    action_list_copy = copy.deepcopy(action_list)

    for cell_action in action_list_copy:
        random_shape = random.choice(valid_shapes)  # Choose a random number from valid_shapes_1
        switchshape_list = ['switchshape'] * random_shape  # Create a list with 'switchshape' repeated random_number times

        # Insert the switchshape_list at the beginning of the cell_action
        cell_action[0:0] = switchshape_list

        # Make sure we switch shapes again to get back to the first shape
        if random_shape != 0:
            reset_list = ['switchshape'] * (num_of_shapes - random_shape)
            insert_index = random_shape + 1
            cell_action[insert_index:insert_index] = reset_list  # Append the reset_list after "place"

    return action_list_copy


def generate_random_solution(action_list, evolution_shard, iteration):
    # Valid Shapes
    valid_shapes = [[3, 5], [1, 8], [0]]
    move_back = move_back_sequence(grid_size)

    if iteration == 0:
        all_actions = []

        sequence_1 = choose_shape_sequence(action_list, valid_shapes[0])
        all_actions.append(sequence_1)
        all_actions.append(move_back)

        sequence_2 = choose_shape_sequence(action_list, valid_shapes[1])
        all_actions.append(sequence_2)
        all_actions.append(move_back)

        sequence_3 = choose_shape_sequence(action_list, valid_shapes[2])
        all_actions.append(sequence_3)

        last_g, last_ps, last_d = execute_instructions(all_actions)

        return last_g, last_ps, last_d, all_actions
    
    elif iteration == 1:
        all_actions = []

        all_actions.append(evolution_shard[0])
        all_actions.append(evolution_shard[1])

        sequence_2 = choose_shape_sequence(action_list, valid_shapes[1])
        all_actions.append(sequence_2)
        all_actions.append(move_back)

        sequence_3 = choose_shape_sequence(action_list, valid_shapes[2])
        all_actions.append(sequence_3)

        last_g, last_ps, last_d = execute_instructions(all_actions)

        return last_g, last_ps, last_d, all_actions
    
    elif iteration == 2:
        all_actions = []

        all_actions.append(evolution_shard[0])
        all_actions.append(evolution_shard[1])
        all_actions.append(evolution_shard[2])
        all_actions.append(evolution_shard[3])

        sequence_3 = choose_shape_sequence(action_list, valid_shapes[2])
        all_actions.append(sequence_3)

        last_g, last_ps, last_d = execute_instructions(all_actions)

        return last_g, last_ps, last_d, all_actions
    
    else:
        print("Error")
        return None
    

def genetic_algorithm(num_of_solutions, default_actions):
    shard = []
    keep_periods = [[0, 1], [0, 1, 2, 3], [0, 1, 2, 3, 4]]

    results = []
    for i in range(3): 
        for _ in range(num_of_solutions):
            setup(GUI=False, render_delay_sec=0.0, gs=grid_size)
            execute('export')

            g, ps, d, a = generate_random_solution(default_actions, shard, i)
            results.append((g, ps, d, a))
        
        best_solution = min(results, key=lambda x: len(x[1]))
        best_solution_actions = best_solution[3]
        
        indices_to_keep = keep_periods[i]
        # Keep part of the solution and mutate the rest
        shard = [best_solution_actions[i] for i in indices_to_keep]

    return best_solution


def main():
    movements = grid_movement(grid_size)
    default_actions = create_default_action_list(movements, grid_size)
    best_solution = genetic_algorithm(100, default_actions)

    grid = best_solution[0]
    placedShapes = best_solution[1]
    print(f"Number of Shapes Used: {len(placedShapes)}")

    actions = best_solution[3]
    file_path = 'Programming_Assignments/Assignment_1/actions.json'

    # Write the list to a JSON file
    with open(file_path, 'w') as json_file:
        json.dump(actions, json_file)
        
    # ########################################
    # # Do not modify any of the code below. 
    # ########################################

    end = time.time()

    # Save the grid to a text file
    np.savetxt(f'grid.txt', grid, fmt="%d")

    # Save the placed shapes to a text file
    with open(f"shapes.txt", "w") as outfile:
        outfile.write(str(placedShapes))

    # Save the elapsed time to a text file
    with open(f"time.txt", "w") as outfile:
        outfile.write(str(end-start))

if __name__ == "__main__":
    main()