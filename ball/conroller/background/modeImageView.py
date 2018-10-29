from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl

from conroller import globals as gc

def create_matrix():
    if gc.on_msg("mode"):
        log(lvl["critical"], "NOT IMPLEMENTED YET!")
    return



## from imageLoader
#def __init__(self):
def init(self):
    # load ball background file names (*.bb)
    self.file_names = glob.glob('../model/images/*.bb')
    self.position = 0

def load_next_image(self):
    self.position += 1
    return self.file_names[self.position]

def load_prev_image(self):
    self.position -= 1
    gc.set_background_matrix(self.file_names[self.position])

def load_line_image(self):
    self.position += 1
    gc.set_background_matrix(self.file_names[self.position])

def load_image_into_matrix(self):
    gc.set_background_matrix('../model/images/list.bb')