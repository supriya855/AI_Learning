import numpy as np
image = np.array([[10,20],
                  [80,110]])
brighter = image + 20 # so here the +20 is broadcasted to each element of the image array
print(brighter)
