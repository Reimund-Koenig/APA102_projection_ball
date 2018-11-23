from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
import numpy as np
from conroller import globals as gc

from conroller import globals as gc

def create_matrix():
    if gc.on_msg("mode") or gc.on_msg("bgcolor1"):
        log(lvl["debug"],"Mode or bgcolor changed -> set background matrix")
        y_len = gc.get_end_led_background()
        matrix = np.zeros((gc.get_num_x_segments(), y_len))
        y=0
        while y < y_len:
            matrix[1,y] = gc.get_msg("bgcolor1")
            y += 1
        gc.set_background_matrix(matrix)
    if gc.on_msg("control"):
        if gc.get_msg("control") == "next":
            # next
            gc.set_sleep_time(gc.get_sleep_time() + 0.0001)
            log(lvl["debug"],"increase sleep time")

        else:
            # prev
            gc.set_sleep_time(gc.get_sleep_time() - 0.0001)
            log(lvl["debug"],"decrease sleep time")
    return