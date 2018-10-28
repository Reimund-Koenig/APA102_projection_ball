from threading import Lock
lock = Lock()


MSG = 0
ON_MSG_FLAG = 1

global mqtt_topics
# dictionary with msg, on_message
mqtt_topics = {
    "power": ["0",False],
    "mode": ["line",False],
    "info": ["off",False],
    "textcolor": [0xFFFFFF,False],
    "print": ["",False],
    "layer": [1,False],
    "diashow": [1,False],
    "control": ["next",False],
    "test": [0,False],
    "rotatefront": [0,False],
    "rotateback": [0,False],
    "bgcolor1": [0xFFFFFF,False],
    "bgcolor2": [0xFFFFFF,False],
    "bgcolor3": [0xFFFFFF,False],
}

def set_threadsafe_topic_msg(topic, msg):
    lock.acquire()
    # check for color
    if msg.startswith("#"):
        mqtt_topics[topic] = [int(msg[1:], 16), True]
    # check for integer
    elif msg.isdigit():
        mqtt_topics[topic] = [int(msg), True]
    #safe as string
    else:
        mqtt_topics[topic] = [msg, True]
    #log(lvl["debug"],"topic(" + topic + ") = " + msg)
    lock.release()

def get_msg(topic):
    return mqtt_topics[topic][MSG]

def on_msg(topic):
    if not mqtt_topics[topic][ON_MSG_FLAG]:
        return False
    lock.acquire()
    mqtt_topics[topic][ON_MSG_FLAG] = False
    lock.release()
    return True


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