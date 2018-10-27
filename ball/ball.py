#!/usr/bin/env python3
import threading
import globals
from mqtt import Handler


class UserInput(threading.Thread):

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        while globals.continue_run:
            eingabe = input()
            if eingabe == "exit":
                print("exit now")
                globals.set_threadsafe_continue_run(False)
            if eingabe == "p":
                print("text to print: " + globals.mqtt_topics["print"])
            else:
                globals.append_threadsafe_list_input(eingabe)


class HandleUserInput(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        while globals.continue_run:
            if len(globals.list_input) > 0:
                print(globals.pop_threadsafe_list_input())


# Create new threads
thread1 = UserInput(1, "Thread-1")
thread2 = HandleUserInput(2, "Thread-2")
thread3 = Handler(3,"MQTTConnector")


# Start new Threads
thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()

print("Exiting Main Thread")


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
# NUM_LED = 144
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