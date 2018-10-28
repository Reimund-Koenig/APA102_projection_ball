import threading
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
from apa102_lib.driver import apa102
from conroller import globals as gc
from conroller.background import bgController
from conroller.fronttext import frontController

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

            #################################################################################
            #
            # test stuff
            #
            #################################################################################

            if gc.get_msg("test") == 1:
                log(lvl["debug"], "Exit by App")
                gc.set_run(False)

            #################################################################################
            #
            # workflow
            #
            #################################################################################

            if gc.get_msg("layer") == 0:
                # is the message new?
                if gc.on_msg("layer"):
                    log(lvl["debug"], "Deactivate Stripe")
                    strip.clear_strip()
                continue
            else:
                if gc.get_msg("layer") == 1 or gc.get_msg("layer") == 3:
                    #   background handling
                    bgController.calculate_background_matrix()
                if gc.get_msg("layer") == 2 or gc.get_msg("layer") == 3:
                    # front handling
                    frontController.calculate_front_matrix()

            # here the matrix should be finished





            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
            # textcolor
            # ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

        # Clear the strip and shut down
        strip.clear_strip()
        strip.cleanup()
