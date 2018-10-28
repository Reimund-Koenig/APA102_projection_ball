from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl

from conroller import globals as gc

def create_matrix():
    # only change by color change or solid is chosen as background
    if gc.on_msg("mode") or gc.on_msg("bgcolor1"):
        log(lvl["debug"], "Set bgcolor1: " + hex(gc.get_msg("bgcolor1")))
        i = 0
        strip.clear_strip()
        while i < NUM_LED:
            strip.set_pixel_rgb(i, gc.get_msg("bgcolor1"))
            i += 1
        strip.show()
    return