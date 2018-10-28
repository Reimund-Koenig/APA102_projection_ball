import threading
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
from apa102_lib.driver import apa102
from conroller import globals as gc

NUM_LED = 77

class HandleMQTTInput(threading.Thread):
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

        while gc.get_run():
            # if len(globals.list_input) > 0:
                # print(globals.pop_threadsafe_list_input())
            if gc.get_msg("test") == 1:
                log(lvl["debug"], "Exit by App")
                gc.set_run(False)
            if gc.on_msg("mode"):
                if gc.get_msg("mode") == "test":
                    log(lvl["debug"], "Activate bgcolor1: " + hex(gc.get_msg("bgcolor1")))
                    strip.clear_strip()
                    i = 0
                    while i < NUM_LED:
                        strip.set_pixel_rgb(i, gc.get_msg("bgcolor1"))
                        i += 1
                    strip.show()
                else:
                    log(lvl["debug"], "Deactivate bgcolor1: " + hex(gc.get_msg("bgcolor1")))
                    strip.clear_strip()
            if gc.on_msg("bgcolor1"):
                    log(lvl["debug"], "Set bgcolor1: " + hex(gc.get_msg("bgcolor1")))
                    i = 0
                    strip.clear_strip()
                    while i < NUM_LED:
                        strip.set_pixel_rgb(i, gc.get_msg("bgcolor1"))
                        i += 1
                    strip.show()


                # Copy the buffer to the Strip (i.e. show the prepared pixels)
            #else:
                # Clear the strip and shut down
        strip.clear_strip()
        strip.cleanup()
