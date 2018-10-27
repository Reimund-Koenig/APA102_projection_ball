#!/usr/bin/env python3
from logmouse import log
from logmouse import log_levels as lvl
from mqtt import Handler
import ball
from apa102_lib.driver import apa102


NUM_LED = 144

strip = apa102.APA102(num_led=NUM_LED, global_brightness=20, mosi=10, sclk=11, order='rbg')

# Turn off all pixels (sometimes a few light up when the strip gets power)
strip.clear_strip()
i=0
while i<NUM_LED:
    strip.set_pixel_rgb(i, 0xFF0000)  # Red
    i+=1
# Copy the buffer to the Strip (i.e. show the prepared pixels)
strip.show()

# Create new threads
thread2 = ball.HandleMQTTInput(2, "Thread-2", strip)
thread3 = Handler(3,"MQTTConnector")


# Start new Threads
thread2.start()
thread3.start()

thread2.join()
thread3.join()

log(lvl["info"],"Exiting Main Thread")

# Clear the strip and shut down
strip.clear_strip()
strip.cleanup()