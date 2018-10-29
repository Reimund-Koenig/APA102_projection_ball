#!/usr/bin/env python3
from conroller.logmouse import log
from conroller.logmouse import log_levels as lvl
from conroller import mqtt
from conroller import ball
from view import ballView

# Create new threads
thread_ball_controller = ball.Handler(1, "BallController")
thread_ball_view = ballView.Handler(2, "BallView")
thread_mqtt = mqtt.Handler(3,"MQTTConnector")

# Start new Threads
thread_mqtt.start()
thread_ball_controller.start()
thread_ball_view.start()

thread_mqtt.join()
thread_ball_controller.join()
thread_ball_view.join()

log(lvl["info"],"Exiting Main Thread")
