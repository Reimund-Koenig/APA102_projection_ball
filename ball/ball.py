#!/usr/bin/env python3
import threading
import paho.mqtt.client as mqtt

MQTT_SERVER = "localhost"
MQTT_PATH = "power"

global continueRun
global list_input

continueRun = True
list_input = []

class MQTTConnector(threading.Thread):

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        global list_input
        global continueRun
        while continueRun:
            mqttc = MyMQTTClass()
            rc = mqttc.run()

            print("rc: " + str(rc))

class MyMQTTClass(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        self.subscribe(MQTT_PATH, 0)
        print("rc: "+str(rc))

    def on_message(self, mqttc, obj, msg):
        print(msg.topic+" "+str(msg.qos)+" "+str(msg.payload))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    #def on_subscribe(self, mqttc, obj, mid, granted_qos):
    #    print("Subscribed: "+str(mid)+" "+str(granted_qos))

    #def on_log(self, mqttc, obj, level, string):
    #    print(string)

    def run(self):
        self.connect(MQTT_SERVER, 1883, 60)
        global continueRun
        rc = 0
        while rc == 0 and continueRun:
            rc = self.loop()
        return rc




class UserInput(threading.Thread):

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        global list_input
        global continueRun
        while continueRun:
            eingabe = input()
            if eingabe == "exit":
                print("exit now")
                continueRun = False
            else:
                print(eingabe)
            list_input.append(eingabe)


class HandleUserInput(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        global list_input
        global continueRun
        while continueRun:
            if len(list_input) > 0:
                print(list_input.pop())


# Create new threads
thread1 = UserInput(1, "Thread-1")
thread2 = HandleUserInput(2, "Thread-2")
thread3 = MQTTConnector(3,"MQTTConnector")


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