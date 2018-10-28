from model import globals as g
from threading import Lock

MSG = 0
ON_MSG_FLAG = 1
lock = Lock()


def get_run():
    return g.run

def set_run(b):
    lock.acquire()
    g.run = b
    lock.release()

def get_msg(topic):
    return g.mqtt_topics[topic][MSG]

def set_msg(topic, msg):
    lock.acquire()
    # check for color
    if msg.startswith("#"):
        g.mqtt_topics[topic] = [int(msg[1:], 16), True]
    # check for integer
    elif msg.isdigit():
        g.mqtt_topics[topic] = [int(msg), True]
    #safe as string
    else:
        g.mqtt_topics[topic] = [msg, True]
    #log(lvl["debug"],"topic(" + topic + ") = " + msg)
    lock.release()

def on_msg(topic):
    if not g.mqtt_topics[topic][ON_MSG_FLAG]:
        return False
    lock.acquire()
    g.mqtt_topics[topic][ON_MSG_FLAG] = False
    lock.release()
    return True

def get_mqtt_topics():
    return g.mqtt_topics

def append_list_input(item):
    lock.acquire()
    g.list_input.append(item)
    lock.release()

def pop_list_input():
    lock.acquire()
    item = g.list_input.pop()
    lock.release()
    return item

def set_background_matrix(filename):
    with open(filename) as f:
        content = f.readlines()
    j = 0
    lock.acquire()
    for i, line in enumerate(content):
        g.view_front_matrix[i][j%77] = hex(int(line, 16))
        j += 1
    lock.release()

def set_front_matrix(matrix):
    lock.acquire()
    g.view_front_matrix = matrix
    lock.release()