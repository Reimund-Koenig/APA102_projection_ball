import threading
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
from apa102_lib.driver import apa102
from conroller import globals as gc
import time

NUM_LED = gc.get_num_led()
END_LED_BACKGROUND = gc.get_end_led_background()


class Handler(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        # Initialize the library and the strip
        strip = apa102.APA102(num_led=NUM_LED, global_brightness=20, mosi=10, sclk=11, order='rgb')

        # Turn off all pixels (sometimes a few light up when the strip gets power)
        strip.clear_strip()

        x = 0
        steps_per_turn = gc.get_num_x_segments()
        while gc.get_run():
            ####################################################################
            # view
            if gc.background_changed():
                background_matrix = gc.get_background_matrix()

            if gc.fronttext_changed:
                front_matrix = gc.get_fronttext_matrix()

            idx = 0
            y = 0
            while idx < NUM_LED:
                if idx < END_LED_BACKGROUND:
                    strip.set_pixel_rgb(idx, int(background_matrix[x,y]))
                else:
                    strip.set_pixel_rgb(idx, int(front_matrix[x,y-END_LED_BACKGROUND]))
                y += 1
                idx += 1

            strip.show()

            x += 1
            if x%steps_per_turn == 0:
                x = 0

            #print("Sleep: " + str(gc.get_sleep_time()))
            time.sleep(gc.get_sleep_time())
            
        # Clear the strip and shut down
        strip.clear_strip()
        strip.cleanup()