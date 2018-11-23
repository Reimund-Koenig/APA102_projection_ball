#################################################################################
#
# Front Controller 
#
#################################################################################
from conroller import globals as gc
from conroller.fronttext import modeDate
from conroller.fronttext import modeClock
from conroller.fronttext import modeText
from conroller.fronttext import modeClockDate

def calculate_front_matrix():
    if gc.get_msg("info") == "date":
        modeDate.create_matrix()
    elif gc.get_msg("info") == "time":
        modeClock.create_matrix()
    elif gc.get_msg("info") == "datetime":
        modeClockDate.create_matrix()
    elif gc.get_msg("info") == "text":
        modeText.create_matrix()