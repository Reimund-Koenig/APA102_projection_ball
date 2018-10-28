from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl

from conroller import globals as gc

def create_matrix():
    if gc.on_msg("mode"):
        log(lvl["critical"], "NOT IMPLEMENTED YET!")
    return