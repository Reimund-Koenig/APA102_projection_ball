#################################################################################
#
# Background Controller
#
#################################################################################

from conroller import globals as gc
from conroller.background import modeLine
from conroller.background import modeSolid
from conroller.background import modeFade2
from conroller.background import modeFade3
from conroller.background import modeDisco
from conroller.background import modeImageView

def calculate_background_matrix():
    if gc.get_msg("mode") == "line":
        modeLine.create_matrix()
    elif gc.get_msg("mode") == "solid":
        modeSolid.create_matrix()
    elif gc.get_msg("mode") == "fade2":
        modeFade2.create_matrix()
    elif gc.get_msg("mode") == "fade3":
        modeFade3.create_matrix()
    elif gc.get_msg("mode") == "disco":
        modeDisco.create_matrix()
    elif gc.get_msg("mode") == "picture":
        modeImageView.create_matrix()