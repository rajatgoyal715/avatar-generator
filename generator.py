# Import libraries
from PIL import Image
import numpy as np
from random import randrange

# Define constants
width, height = 400, 400
num_blocks_width = 5
num_blocks_height = 5
base_color = (240, 240, 240)

print("Width: " + str(width))
print("Height: " + str(height))

# Randomize color
red_component = randrange(256)
green_component = randrange(256)
blue_component = randrange(256)
alpha_component = 1

color = (red_component, green_component, blue_component)
print(color)

# Generate block array
block_array = [[0 for x in range(num_blocks_width)] for y in range(num_blocks_height)] 
for i in range(5):
    for j in range(5):
        choice = randrange(2)
        block_array[i][j] = choice

print(block_array)

# Generate image array
image_array = np.zeros((height, width, 3), dtype=np.uint8)

block_size = int(width / num_blocks_width)
print(block_size)

for i in range(num_blocks_width):
    for j in range(num_blocks_height):
        if block_array[i][j] == 1:
            image_array[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size] = color
        else:
            image_array[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size] = base_color

# Save Image
img = Image.fromarray(image_array, 'RGB')
img.save("image.png")

img.show()
