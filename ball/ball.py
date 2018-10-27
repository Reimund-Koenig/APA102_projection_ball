import globals
import threading
from logmouse import log
from logmouse import log_levels as lvl

class HandleMQTTInput(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        while globals.continue_run:
            # if len(globals.list_input) > 0:
                # print(globals.pop_threadsafe_list_input())
            if globals.mqtt_topics["test"] == "1":
                log(lvl["debug"], "Exit by App")
                globals.set_threadsafe_continue_run(False)