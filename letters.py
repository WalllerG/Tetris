from arcade import color
from random import choice

letter_T = {
    1:[[1,1,1],
       [0,1,0]],

    2:[[0,0,1],
       [0,1,1],
       [0,0,1]],

    3:[[0,0,0],
       [0,1,0],
       [1,1,1]],

    4:[[1,0],
       [1,1],
       [1,0]],

    "color": color.VIOLET,
    "num_of_rotations": 4,
    "settled_letter": 11
}

letter_o = {
    1:[[1,1],[1,1]],
    "color": color.YELLOW,
    "num_of_rotations": 1,
    "settled_letter": 12
}

letter_left_l = {
    1:[[1,0,0],
       [1,0,0],
       [1,1,0]],

    2:[[1,1,1],
       [1,0,0],],

    3:[[0,1,1],
       [0,0,1],
       [0,0,1]],

    4:[[0,0,0],
       [0,0,1],
       [1,1,1]],

    "color": color.DARK_BLUE,
    "num_of_rotations": 4,
    "settled_letter": 13
}

letter_right_l = {
    1:[[0,0,1],
       [0,0,1],
       [0,1,1]],

    2:[[1,0,0],
       [1,1,1],],

    3:[[1,1,0],
       [1,0,0],
       [1,0,0]],

    4:[[1,1,1],
       [0,0,1],
       [0,0,0]],

    "color": color.ALLOY_ORANGE,
    "num_of_rotations": 4,
    "settled_letter": 14
}

letter_I = {
    1:[[0,1,0],
       [0,1,0],
       [0,1,0],
       [0,1,0]],

    2:[[0,0,0,0],
       [1,1,1,1],
       [0,0,0,0]],

    "color": color.LIGHT_BLUE,
    "num_of_rotations": 2,
    "settled_letter": 15
}

letter_z = {
    1:[[1,1,0],
       [0,1,1]],

    2:[[0,0,1],
       [0,1,1],
       [0,1,0]],

    "color": color.GREEN,
    "num_of_rotations": 2,
    "settled_letter": 16
}

letter_s = {
    1:[[0,1,1],
       [1,1,0]],

    2:[[1,0,0],
       [1,1,0],
       [0,1,0]],

"color": color.RED,
    "num_of_rotations": 2,
    "settled_letter": 17
}

all_letters = [letter_T, letter_o,  letter_left_l, letter_right_l, letter_I, letter_z, letter_s]

def choose_random_letter():
    return choice(all_letters)