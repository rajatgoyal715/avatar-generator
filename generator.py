# Import libraries
from PIL import Image
import numpy as np
from random import randrange
from argparse import ArgumentParser
import sys


# Define constants (Or read constants from user in future)
width, height = 400, 400
num_blocks_width = 5
num_blocks_height = 5

base_color = (240, 240, 240)
output_file_name = "test.png"


# Randomize color
def generateColor():
    red_component = randrange(256)
    green_component = randrange(256)
    blue_component = randrange(256)
    alpha_component = 1

    return (red_component, green_component, blue_component)


def getBlockArray1():
    '''
    Generate block array by randomly selecting the choice for all blocks
    Number of possibilities: 2^(num_blocks_width * num_blocks_height)
    '''
    block_array = [[0 for x in range(num_blocks_width)] for y in range(num_blocks_height)] 
    for i in range(num_blocks_width):
        for j in range(num_blocks_height):
            choice = randrange(2)
            block_array[i][j] = choice

    return block_array


def getBlockArray2():
    '''
    Generate block array using the following algorithm:
    - Fill only first half columns and copy the second half from first half
    - Number of blocks which needs to be randomised:
    num_randomised = ((num_blocks_width+1)/2 * num_blocks_height)
    - Number of blocks which must be filled should lie in this range:
    num_blocks_filled = randrange(1/3 * num_randomised, 2/3 * num_randomised)
    - Run an infinite loop which will pick a number from (0, num_randomised) till count reached num_blocks_filled
    - Maintain a visited array which will check if that block has already been visited(filled)
    '''

    half_num_blocks_width = int((num_blocks_width+1)/2)
    num_randomised = int(half_num_blocks_width * num_blocks_height)
    num_blocks_filled = randrange(int(num_randomised / 3), int(2 * num_randomised / 3))

    visited = [0 for x in range(num_randomised)]
    block_array = [[0 for x in range(num_blocks_width)] for y in range(num_blocks_height)]
    filled_count = 0
    while filled_count < num_blocks_filled:
        while True:
            rand_num = randrange(num_randomised)
            if visited[rand_num] == 0:
                visited[rand_num] = 1
                filled_count = filled_count + 1
                break

    for pos in range(num_randomised):
        # If the position is visited, fill the 2D block array
        if visited[pos] == 1:
            pos_x = int(pos/half_num_blocks_width)
            pos_y = int(pos%half_num_blocks_width)
            block_array[pos_x][pos_y] = 1
            block_array[pos_x][num_blocks_height - pos_y - 1] = 1

    return block_array

def generateImage():
    '''
    Generate image array
    '''
    
    image_array = np.zeros((height, width, 3), dtype=np.uint8)

    block_size_width = int(width / num_blocks_width)
    block_size_height = int(width / num_blocks_height)

    block_array = getBlockArray2()
    
    color = generateColor()

    for i in range(num_blocks_width):
        for j in range(num_blocks_height):
            width_start = i * block_size_width
            width_end = (i+1) * block_size_width
            height_start = j * block_size_height
            height_end = (j+1) * block_size_height
            if block_array[i][j] == 1:
                image_array[width_start:width_end,height_start:height_end] = color
            else:
                image_array[width_start:width_end,height_start:height_end] = base_color

    img = Image.fromarray(image_array, 'RGB')
    img.save(output_file_name)

def readArguments(args):
    parser = ArgumentParser()
    parser.add_argument("-f", "--file", dest="filename", help="Write generated image to this file")

    args = parser.parse_args(args)
    global output_file_name
    output_file_name = args.filename

def main(args):
    readArguments(args)
    generateImage()

if __name__ == "__main__":
    main(sys.argv[1:])
