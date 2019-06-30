#!/usr/bin/env python
# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2019 Kevin Walchko
# see LICENSE for full details
##############################################
# This is just a simple check to see if the pycreate2 driver is working
# without worrying about gecko

from  pycreate2 import Create2
import time

# Create a Create2.
port = "/dev/serial/by-id/usb-FTDI_FT231X_USB_UART_DA01NX3Z-if00-port0"
bot = Create2(port)

# Start the Create 2
bot.start()

# Put the Create2 into 'safe' mode so we can drive it
# This will still provide some protection
# bot.safe()

# You are responsible for handling issues, no protection/safety in
# this mode ... becareful
bot.full()

bot.drive_direct(100, 100)
time.sleep(2)

# Stop the bot
bot.drive_stop()

for _ in range(10):
    # query some sensors
    sensors = bot.get_sensors()  # returns all data
    print(sensors)
    time.sleep(0.25)

# Close the connection
# bot.close()
