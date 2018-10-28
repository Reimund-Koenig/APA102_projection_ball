import threading

NUM_LED = 77


class HandleMQTTInput(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        # Initialize the library and the strip
        #strip = apa102.APA102(num_led=NUM_LED, global_brightness=20, mosi=10, sclk=11, order='rgb')
        i = 5
        # Turn off all pixels (sometimes a few light up when the strip gets power)
        #strip.clear_strip()

        # while gc.get_run():
            # if len(globals.list_input) > 0:


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