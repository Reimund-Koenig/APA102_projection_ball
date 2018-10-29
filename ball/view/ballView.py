import threading
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
from apa102_lib.driver import apa102
from conroller import globals as gc

END_LED_FRONT = 77
NUM_LED = 144


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
        while gc.get_run():
            # some matrix changed?
            if not (gc.background_changed() or gc.fronttext_changed()):
                continue

            strip.clear_strip()
            # load fronttext into view
            log(lvl["debug"], "load new fronttext matrix")
            matrix = gc.get_fronttext_matrix()
            idx = 0
            y = 0
            while idx < END_LED_FRONT:
                strip.set_pixel_rgb(idx, int(matrix[x,y]))
                y += 1
                idx += 1

            # load background into view
            log(lvl["debug"], "load new background matrix")
            matrix = gc.get_background_matrix()
            y = 0
            while idx < NUM_LED:
                strip.set_pixel_rgb(idx, int(matrix[x,y]))
                y += 1
                idx += 1


            strip.show()
            # now sleep till 1/360° is reached >> See mind-plan below

        # Clear the strip and shut down
        strip.clear_strip()
        strip.cleanup()
        # front matrix changed?









        # Initialize the library and the strip
        #strip = apa102.APA102(num_led=NUM_LED, global_brightness=20, mosi=10, sclk=11, order='rgb')
        i = 5
        # Turn off all pixels (sometimes a few light up when the strip gets power)
        #strip.clear_strip()

        # while gc.get_run():
            # if len(globals.list_input) > 0:

        # if len(globals.list_input) > 0:
        # print(globals.pop_threadsafe_list_input())


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
# filename = "images/line.txt"
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