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

        turns_per_second = 50.0
        steps_per_turn = gc.get_num_x_segments()
        steps_per_second = steps_per_turn * turns_per_second
        seconds_per_step = 1.0 / steps_per_second
        log(lvl["debug"], "Wait for: " + str(seconds_per_step) + "  seconds")

        x = 0
        SLEEP_TIME = 0.0059
        NS_TO_SECONDS = 1000*1000*1000
        while gc.get_run():
            starttime = time.time_ns()
            if gc.background_changed():
                background_matrix = gc.get_background_matrix()

            if gc.fronttext_changed:
                front_matrix = gc.get_fronttext_matrix()
            #time_1 = time.time_ns() - starttime
            #starttime = time.time_ns()
            idx = 0
            y = 0
            while idx < NUM_LED:
                if idx < END_LED_BACKGROUND:
                    strip.set_pixel_rgb(idx, int(background_matrix[x,y]))
                else:
                    strip.set_pixel_rgb(idx, int(front_matrix[x,y-END_LED_BACKGROUND]))
                y += 1
                idx += 1

            #time_2 = time.time_ns() - starttime
            #starttime = time.time_ns()

            strip.show()
            #time_3 = time.time_ns() - starttime
            #starttime = time.time_ns()

            x += 1
            if x%steps_per_turn == 0:
                x = 0
            #time_4 = time.time_ns() - starttime
            #print("x: " + str(x) + " - complete: " + str(time_1+time_2+time_3+time_4) + " - time_1: " + str(time_1) + "  - time_2: " + str(time_2) + "  - time_3: " + str(time_3) + "  - time_4: " + str(time_4))
            time.sleep(SLEEP_TIME-((starttime-time.time_ns())/NS_TO_SECONDS));
        # Clear the strip and shut down
        strip.clear_strip()
        strip.cleanup()