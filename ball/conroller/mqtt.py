#!/usr/bin/env python3
import paho.mqtt.client as mqtt
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
import threading
from conroller import globals as gc

MQTT_SERVER = "localhost"

class Handler(threading.Thread):

    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        while gc.get_run():
            mqttc = Connector()
            mqttc.run()

class Connector(mqtt.Client):

    def on_connect(self, mqttc, obj, flags, rc):
        log(lvl["info"], "on_connect")
        for topic in gc.get_mqtt_topics():
            log(lvl["info"],"subscribe: " +  topic)
            self.subscribe(topic, 0)

    def on_message(self, mqttc, obj, msg):
        gc.set_msg(msg.topic, msg.payload.decode('ascii'))
        log(lvl["debug"],"on_message: " + msg.topic + " = " + msg.payload.decode('ascii'))

    def on_publish(self, mqttc, obj, mid):
        log(lvl["info"],"mid: "+str(mid))

    #def on_subscribe(self, mqttc, obj, mid, granted_qos):
    #    log(lvl["debug"], "subscribed: "+str(mid)+" "+str(granted_qos))

    #def on_log(self, mqttc, obj, level, string):
    #    log(lvl["debug"],string)

    def run(self):
        self.connect(MQTT_SERVER, 1883, 60)
        rc = 0
        while rc == 0 and gc.get_run():
            rc = self.loop()
        return rc
