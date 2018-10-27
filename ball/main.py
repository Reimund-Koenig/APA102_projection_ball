#!/usr/bin/env python3
from logmouse import log
from logmouse import log_levels as lvl
from mqtt import Handler
import ball

# Create new threads
thread2 = ball.HandleMQTTInput(2, "Thread-2")
thread3 = Handler(3,"MQTTConnector")


# Start new Threads
thread2.start()
thread3.start()

thread2.join()
thread3.join()


log(lvl["info"],"Exiting Main Thread")


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