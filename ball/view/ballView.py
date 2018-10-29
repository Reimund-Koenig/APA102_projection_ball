import threading
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
from apa102_lib.driver import apa102
from conroller import globals as gc
import time
import datetime

NUM_LED = gc.get_num_led()
END_LED_FRONT = gc.get_end_led_front()

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

        # 360 steps per turn with 50 turns per second with
        turns_per_second = 50.0
        steps_per_turn = 360.0
        steps_per_second = steps_per_turn * turns_per_second
        seconds_per_step = (1.0) / steps_per_second
        log(lvl["debug"], "Wait for: " + str(seconds_per_step) + "  seconds")

        x = 0
        while gc.get_run():
            starttime = datetime.datetime.now()
            # some matrix changed?
            #if not (gc.background_changed() or gc.fronttext_changed()):
            #    continue

            strip.clear_strip()
            # load fronttext into view
            #log(lvl["debug"], "load new fronttext matrix")
            matrix = gc.get_fronttext_matrix()
            idx = 0
            y = 0
            while idx < END_LED_FRONT:
                strip.set_pixel_rgb(idx, int(matrix[x,y]))
                y += 1
                idx += 1

            # load background into view
            log(lvl["debug"], "load new background matrix (x=" + str(x) + ")")
            matrix = gc.get_background_matrix()
            y = 0
            while idx < NUM_LED:
                strip.set_pixel_rgb(idx, int(matrix[x,y]))
                y += 1
                idx += 1


            strip.show()
            endtime = datetime.datetime.now()
            deltatime = endtime - starttime
            print("normal sleep: " + str(seconds_per_step*1000))
            print("sleep delta: " + str(deltatime.total_seconds()*1000))
            print("sleep time left: " + str((seconds_per_step - deltatime.total_seconds())*1000))
            # now sleep till 1/360° is reached >> See mind-plan below
            x += 1
            if x%360 == 0:
                x = 0
            time.sleep(seconds_per_step)

        # Clear the strip and shut down
        strip.clear_strip()
        strip.cleanup()