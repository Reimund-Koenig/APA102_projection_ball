from model import globals as g
from threading import Lock
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl

MSG = 0
ON_MSG_FLAG = 1
lock = Lock()

def set_sleep_time(st):
    lock.acquire()
    g.sleep_time = st
    lock.release()

def get_sleep_time():
    return g.sleep_time

def get_num_led():
    return g.NUM_LED

def get_num_x_segments():
    return g.NUM_X_SEGMENTS

def get_end_led_background():
    return g.END_LED_BACKGROUND

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


def fronttext_changed():
    if not g.view_fronttext_change:
        return False
    lock.acquire()
    g.view_fronttext_change = False
    lock.release()
    return True

def get_fronttext_matrix():
    return g.view_fronttext_matrix

def set_fronttext_matrix(matrix):
    log(lvl["debug"],"set front matrix")
    lock.acquire()
    g.view_fronttext_matrix = matrix
    g.view_fronttext_change = True
    lock.release()

def background_changed():
    if not g.view_background_change:
        return False
    lock.acquire()
    g.view_background_change = False
    lock.release()
    return True

def get_background_matrix():
    return g.view_background_matrix

def set_background_matrix(matrix):
    log(lvl["debug"],"set background matrix")
    lock.acquire()
    g.view_background_matrix = matrix
    g.view_background_change = True
    lock.release()

def set_image_to_background_matrix(filename):
    with open(filename) as f:
        content = f.readlines()
    j = 0
    lock.acquire()
    for i, line in enumerate(content):
        g.view_background_matrix[i][j%77] = hex(int(line, 16))
        j += 1
    g.view_background_change = True
    lock.release()
