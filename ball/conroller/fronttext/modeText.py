from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
import numpy as np
from conroller import globals as gc

def create_matrix():
    if gc.on_msg("info") or gc.on_msg("textcolor"):
        log(lvl["debug"], "Mode or front changed -> set front matrix " + str(gc.get_msg("textcolor")))
        matrix = np.full((360, 77), gc.get_msg("textcolor"))
        gc.set_fronttext_matrix(matrix)
    return