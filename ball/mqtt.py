#!/usr/bin/env python3
import paho.mqtt.client as mqtt
import threading
import globals

class Handler(threading.Thread):

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        while globals.continue_run:
            mqttc = Connector()
            rc = mqttc.run()

            print("rc: " + str(rc))

class Connector(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        for packet in globals.mqtt_topics:
            self.subscribe(packet, 0)

    def on_message(self, mqttc, obj, msg):
        globals.set_threadsafe_packet_msg(msg.payload.decode('ascii'))

    def on_publish(self, mqttc, obj, mid):
        print("mid: "+str(mid))

    #def on_subscribe(self, mqttc, obj, mid, granted_qos):
    #    print("Subscribed: "+str(mid)+" "+str(granted_qos))

    #def on_log(self, mqttc, obj, level, string):
    #    print(string)

    def run(self):
        self.connect(globals.MQTT_SERVER, 1883, 60)
        rc = 0
        while rc == 0 and globals.continue_run:
            rc = self.loop()
        return rc
