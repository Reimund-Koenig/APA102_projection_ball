from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
import numpy as np
from conroller import globals as gc

from conroller import globals as gc

def create_matrix():
    if gc.on_msg("mode") or gc.on_msg("bgcolor1"):
        log(lvl["debug"],"Mode or bgcolor changed -> set background matrix")
        matrix = np.zeros((360, 77))
        y=0
        while y < gc.get_end_led_front():
            x = 170
            while x <= 190:
                matrix[x,y] = gc.get_msg("bgcolor1")
                x+=1
            y += 1
        gc.set_background_matrix(matrix)
    return