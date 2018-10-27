from threading import Lock
lock = Lock()

global mqtt_topics
mqtt_topics = {
    "power": "0",
    "mode": "line",
    "info": "off",
    "textcolor": "#FFFFFF",
    "print": "",
    "layer": "1",
    "diashow": "1",
    "control": "",
    "test": "0",
    "rotatefront": "0",
    "rotateback": "0",
    "bgcolor1": "#FFFFFF",
    "bgcolor2": "#FFFFFF",
    "bgcolor3": "#FFFFFF"
}

def set_threadsafe_topic_msg(topic, msg):
    lock.acquire()
    mqtt_topics[topic] = msg
    #log(lvl["debug"],"topic(" + topic + ") = " + msg)
    lock.release()

global MQTT_SERVER
MQTT_SERVER = "localhost"

global continue_run
global list_input
list_input = []


global COMMAND_LIST
COMMAND_LIST = []

continue_run = True

def set_threadsafe_continue_run(b):
    global continue_run
    lock.acquire()
    continue_run = b
    lock.release()


def append_threadsafe_list_input(item):
    global list_input
    lock.acquire()
    list_input.append(item)
    lock.release()

def pop_threadsafe_list_input():
    global list_input
    lock.acquire()
    item = list_input.pop()
    lock.release()
    return item