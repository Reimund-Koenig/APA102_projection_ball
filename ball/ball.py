import globals
import threading
from logmouse import log
from logmouse import log_levels as lvl
from apa102_lib.driver import apa102

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

        while globals.continue_run:
            # if len(globals.list_input) > 0:
                # print(globals.pop_threadsafe_list_input())
            if globals.get_msg("test") == 1:
                log(lvl["debug"], "Exit by App")
                globals.set_threadsafe_continue_run(False)
            if globals.on_msg("mode"):
                if globals.get_msg("mode") == "test":
                    log(lvl["debug"], "Activate bgcolor1: " + hex(globals.get_msg("bgcolor1")))
                    strip.clear_strip()
                    i = 0
                    while i < NUM_LED:
                        strip.set_pixel_rgb(i, globals.get_msg("bgcolor1"))
                        i += 1
                    strip.show()
                else:
                    log(lvl["debug"], "Deactivate bgcolor1: " + hex(globals.get_msg("bgcolor1")))
                    strip.clear_strip()
            if globals.on_msg("bgcolor1"):
                    log(lvl["debug"], "Set bgcolor1: " + hex(globals.get_msg("bgcolor1")))
                    i = 0
                    strip.clear_strip()
                    while i < NUM_LED:
                        strip.set_pixel_rgb(i, globals.get_msg("bgcolor1"))
                        i += 1
                    strip.show()


                # Copy the buffer to the Strip (i.e. show the prepared pixels)
            #else:
                # Clear the strip and shut down
        strip.clear_strip()
        strip.cleanup()

        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # .

        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        # .
        #
        # filename = "pics/line.txt"
        # content = ""
        # pixel = 0
        #
        # with open(filename) as f:
        #     content = f.readlines()
        #
        # turnsPerSecond = 50
        # stepsPerTurn = 360
        # oneMicrosecond = seconds / 1000000.0
        # turn_rate = 1.0/turnsPerSecond                      # 50 Hz = 0,02 seconds per round
        #
        # # 360 vertical pixes * 50 turns = 18000 color changes per second = 1/18000 = 0.00005555555
        # step_rate = 1.0/(stepsPerTurn * turnsPerSecond)
        # while 1:
        #     nextTurn = time.time() + turn_rate  # 1267919090.35663390159606933594
        #
        #     # show LEDs for one turn
        #     for idx, line in enumerate(content):
        #         color = hex(int(line, 16))
        #         strip.set_pixel_rgb(pixel, color)
        #         if idx % 76 == 0:
        #             while time.time() < nextSwitchTime:
        #                 time.sleep(oneMicrosecond)
        #             nextSwitchTime = time.time + step_rate
        #
        #     # wait for next turn
        #     while time.time < turn_rate:
        #         time.sleep(oneMicrosecond)