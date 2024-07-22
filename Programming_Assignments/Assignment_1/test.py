import numpy as np
import json
from gridgame import *

grid_size = 7

def execute_instructions(action_list):
    # can execute instructions on lists of any depth (1D, 2D, 3D, etc)
    if isinstance(action_list[0], list):
        for sublist in action_list:
            g, ps, d = execute_instructions(sublist)
    else:
        for action in action_list:
            g, ps, d = execute(action)

    return g, ps, d


def main():
    with open("Programming_Assignments/Assignment_1/actions.json", "r") as file:
        actions = json.load(file)

    setup(GUI=True, render_delay_sec=0.0, gs=grid_size)
    execute('export')

    execute_instructions(actions)

if __name__ == "__main__":
    main()