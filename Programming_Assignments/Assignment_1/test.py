import time
import numpy as np
import copy
import random
import json
from gridgame import *

grid_size = 7

def evaluate_actions(action_list):
    for iteration in action_list:
        for cell_action in iteration:
            for action in cell_action:
                g, ps, d = execute(action) 

    return g, ps, d

setup(GUI=True, render_delay_sec=0.0, gs=grid_size)
execute('export')

with open("Programming_Assignments/Assignment_1/actions.json", "r") as file:
    actions = json.load(file)

g, ps, d = evaluate_actions(actions)