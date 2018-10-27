import globals
import threading
from logmouse import log
from logmouse import log_levels as lvl


class HandleMQTTInput(threading.Thread):
    def __init__(self, id, name, strip):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        # Initialize the library and the strip


        while globals.continue_run:
            # if len(globals.list_input) > 0:
                # print(globals.pop_threadsafe_list_input())
            if globals.mqtt_topics["test"] == "1":
                log(lvl["debug"], "Exit by App")
                globals.set_threadsafe_continue_run(False)
            #if globals.mqtt_topics["mode"] == "test":
            #    print("test")
            #else:
            #    print("test2")

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