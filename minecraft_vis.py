import logging
from termcolor import colored
from gdpc import Block, Editor
from gdpc import geometry as geo
from glm import ivec3
import numpy as np
import time
import itertools

def colour(data):
    harbor,weight = data
    threshold = 12666
    threshold2 = 25333
    if harbor == 1:
        if weight < threshold:
            return "minecraft:yellow_stained_glass"
        elif weight < threshold2:
            return "minecraft:yellow_wool"
        else:
            return "minecraft:yellow_concrete"
    elif harbor == 2:
        if weight < threshold:
            return "minecraft:green_stained_glass"
        elif weight < threshold2:
            return "minecraft:green_wool"
        else:
            return "minecraft:green_concrete"
    elif harbor == 3:
        # blauw
        if weight < threshold:
            return "minecraft:blue_stained_glass"
        elif weight < threshold2:
            return "minecraft:blue_wool"
        else:
            return "minecraft:blue_concrete"
    else:
        return "minecraft:air"

    
# Here, we set up Python's logging system.
# GDPC sometimes logs some errors that it cannot otherwise handle.
logging.basicConfig(format=colored("%(name)s - %(levelname)s - %(message)s", color="yellow"))

# Here we construct an Editor object
ED = Editor(buffering=False)

start = ivec3(121, 113, -12)
end_glob = ivec3(4, 121, -30)

container_length = 10
container_width = 4
container_height = 3

end = ivec3(start.x - container_length, start.y+2, start.z - container_width+1)

geo.placeCuboid(ED, start, end_glob, Block("minecraft:air"))
time.sleep(1)

# data.shape = (20,8,3,4,2)
data = np.load("Results/boat_history_n=50.npy")

bay_offset = container_length + 4
tier_offset = container_height
row_offset = container_width+1

for gen in range(1):
    
    for bay, tier, row in itertools.product(range(8),range(3),range(4)):

        temp_start = ivec3(start.x - bay*bay_offset, start.y + tier*tier_offset, start.z - row*row_offset)
        temp_end = ivec3(end.x - bay*bay_offset, end.y + tier*tier_offset, end.z - row*row_offset)
        geo.placeCuboid(ED, temp_start, temp_end, Block(colour(data[gen,bay,tier,row])))
