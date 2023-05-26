
# MODA PROJECT: Optimizing container configuration for container ship
### Ruben Ahrens, s3677532 & Lucas de Wolff, s3672980 & Shaoxuan Zhang, s3426505
In this project, we present an optimized container loading plan for a cargo ship with specific dimensions of 8 bays, 4 rows, and 3 tiers. Our solution aims to minimize ship instability and unloading time while carrying up to 96 containers destined for three harbors. To achieve this, we employ NSGA-III, a genetic algorithm designed for multi-objective optimization. By exploring the Pareto front, our approach generates stable and efficient solutions. Our findings offer practical applications and improved container loading strategies for cargo ships.

The following files are relevant:
- `CargoOpt_Pymoo.ipynb`
  - Contains the main algorithm for optimizing the container configuration of the cargo ship. The data used is saved in `.ipynp` format in the `Data/` folder in the same was as the results are saved in their respective folder.
- `minecraft_vis.py`
  - Contains the algorithm for rendering the container configuration in minecraft. To run the code, GDPC has to be installed in python and GDMC-HTTP in minecraft: https://github.com/avdstaaij/gdpc
  - By default, the code works only when the `boat_world` is imported.
- `Minecraft/boat_world`
  - This folder contains the minecraft world where the ship is built. This world must be [loaded](https://help.minecraft.net/hc/en-us/articles/360053272471-Sideloading-Worlds-into-Minecraft-Java-Edition) into the local game.
- `ship_empty.schem`
  - The schematics file of the boat, the schematics file can be loaded into a minecraft world with the [WorldEdit](https://en.wikipedia.org/wiki/WorldEdit) (the worldedit mod may conflict with the GDPC mod, therefore it is advised to load the world `boat_world` to avoid using worldedit)