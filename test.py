import numpy as np
current_harbor = 0
only_harbors = np.empty((8, 3, 4))
only_harbors[0, 0, 0] = 0
only_harbors[0, 1, 0] = 1
# First check
unloading_time = 0


for i in range(only_harbors.shape[1]-1,-1,-1):
    # set value to 0 if harbor is empty
    print(only_harbors[:, i] == 1)
    unloading_time += len(np.where(only_harbors[:, i] == current_harbor))
