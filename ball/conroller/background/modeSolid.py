from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
import numpy as np
from conroller import globals as gc

def create_matrix():
    # only change by color change or solid is chosen as background
    if gc.on_msg("mode") or gc.on_msg("bgcolor1"):
        log(lvl["debug"],"Mode or bgcolor changed -> set background matrix")
        matrix = np.full((gc.get_num_x_segments(), gc.get_num_led()), gc.get_msg("bgcolor1"))
        gc.set_background_matrix(matrix)
    return