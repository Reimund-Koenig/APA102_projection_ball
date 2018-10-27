#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from logmouse import log
from logmouse import log_levels as lvl
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
            mqttc.run()

class Connector(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        log(lvl["info"], "on_connect")
        for topic in globals.mqtt_topics:
            log(lvl["info"],"subscribe: " +  topic)
            self.subscribe(topic, 0)

    def on_message(self, mqttc, obj, msg):
        globals.set_threadsafe_topic_msg(msg.topic, msg.payload.decode('ascii'))
        log(lvl["debug"],"on_message: " + msg.topic + " = " + msg.payload.decode('ascii'))

    def on_publish(self, mqttc, obj, mid):
        log(lvl["info"],"mid: "+str(mid))

    #def on_subscribe(self, mqttc, obj, mid, granted_qos):
    #    log(lvl["debug"], "subscribed: "+str(mid)+" "+str(granted_qos))

    #def on_log(self, mqttc, obj, level, string):
    #    log(lvl["debug"],string)

    def run(self):
        self.connect(globals.MQTT_SERVER, 1883, 60)
        rc = 0
        while rc == 0 and globals.continue_run:
            rc = self.loop()
        return rc
