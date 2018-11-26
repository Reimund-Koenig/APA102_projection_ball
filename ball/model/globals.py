import numpy as np

END_LED_BACKGROUND = 65
NUM_LED = 144
NUM_X_SEGMENTS = 36

global run
run = True

global sleep_time
sleep_time = 0.006

global list_input
list_input = []

global view_background_matrix
view_background_matrix =  np.zeros( (NUM_X_SEGMENTS, END_LED_BACKGROUND), dtype=np.int32 )

global view_background_change
view_background_change = True

global view_fronttext_matrix
view_fronttext_matrix =  np.zeros( (NUM_X_SEGMENTS, NUM_LED-END_LED_BACKGROUND), dtype=np.int32 )

global view_fronttext_change
view_fronttext_change = True

global mqtt_topics
# dictionary with msg, on_message
mqtt_topics = {
    "power": ["0",False],
    "mode": ["line",False],
    "info": ["off",False],
    "textcolor": [0xFFFFFF,False],
    "print": ["",False],
    "layer": [1,False],
    "diashow": [1,False],
    "control": ["next",False],
    "test": [0,False],
    "rotatefront": [0,False],
    "rotateback": [0,False],
    "bgcolor1": [0xFFFFFF,False],
    "bgcolor2": [0xFFFFFF,False],
    "bgcolor3": [0xFFFFFF,False],
}
