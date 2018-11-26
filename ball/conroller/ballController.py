import threading
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
from conroller import globals as gc
import time
import RPi.GPIO as GPIO

NS_TO_SECONDS = 1000*1000*1000
NS_DELAY_TIME = (1000 * 1000 * 10)
NS_ONE_SEC = (1000 * 1000 * 1000)

class Handler(threading.Thread):
    def __init__(self, id, name):
        threading.Thread.__init__(self)
        self.threadID = id
        self.name = name

    # @staticmethod
    def run(self):
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        t1 = time.time_ns() + NS_ONE_SEC
        t2 = t1
        hz = 0
        turn = False
        steps_per_turn = gc.get_num_x_segments()
        while gc.get_run():

            #################################################################################
            #
            # test stuff
            #
            #################################################################################
            if gc.get_msg("test") == 1:
                log(lvl["debug"], "Exit by App")
                gc.set_run(False)
            ####################################################################
            #  frequency
            t0 = time.time_ns()
            if t0 > t1:
                if not hz == 0:
                    steps_per_second = steps_per_turn * hz
                    seconds_per_step = 1.0 / steps_per_second
                    gc.set_sleep_time(seconds_per_step)
                t1 = t0 + NS_ONE_SEC
                hz = 0
            if GPIO.input(4) and t0 > t2:
                # disconnected
                if not turn:
                    # print("disconnected")
                    turn = True
            else:
                # connected
                if turn:
                    # print("connected")
                    turn = False
                    hz = hz + 1
                    t2 = t0 + NS_DELAY_TIME

