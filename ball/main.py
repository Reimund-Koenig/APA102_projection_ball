#!/usr/bin/env python3
from logmouse import log
from logmouse import log_levels as lvl
from mqtt import Handler
import ball

# Create new threads
thread2 = ball.HandleMQTTInput(2, "Thread-2")
thread3 = Handler(3,"MQTTConnector")


# Start new Threads
thread2.start()
thread3.start()

thread2.join()
thread3.join()


log(lvl["info"],"Exiting Main Thread")
