#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2019 Kevin Walchko
# see LICENSE for full details
##############################################
from  pycreate2 import Create2
from pygecko.multiprocessing import geckopy
from pygecko.pycore.mbeacon import BeaconCoreServer
from pygecko.pycore.transport import Ascii
from pygecko.multiprocessing import GeckoSimpleProcess

key = "localhost"


def core():
    # create a geckocore for things to connect to
    print("<<< Starting Core >>>")
    bs = BeaconCoreServer(key=key, handler=Ascii, print=False)
    bs.start()
    bs.run()

def main():

    if True:
        sp = GeckoSimpleProcess()
        sp.start(func=core, name='geckocore', kwargs={})

    print("<<< Starting Roomba >>>")
    port = "/dev/serial/by-id/usb-FTDI_FT231X_USB_UART_DA01NX3Z-if00-port0"
    bot = Create2(port)
    bot.start()
    bot.full()

    geckopy.init_node()
    rate = geckopy.Rate(10)  # loop rate

    # s = geckopy.subBinderUDS(key, 'cmd', "/tmp/cmd")
    s = geckopy.subBinderTCP(key, 'cmd')
    if s is None:
        raise Exception("subscriber is None")

    # p = geckopy.pubBinderUDS(key,'create2',"/tmp/create")
    p = geckopy.pubBinderTCP(key,'create2')
    if p is None:
        raise Exception("publisher is None")

    print("<<< Starting Loop >>>")
    try:
        bot.drive_direct(200,200)
        while not geckopy.is_shutdown():
            sensors = bot.get_sensors()  # returns all data
            batt = 100*sensors.battery_charge / sensors.battery_capacity
            # print(">> batter: {:.1f}".format(batt))
            bot.digit_led_ascii("{:4}".format(int(batt)))
            # bot.digit_led_ascii("80")
            # print(">> ir:", sensors.light_bumper)
            # print(">> ir:", end=" ")
            # for i in range(6):
            #     print("{:.1f}".format(sensors[35 + i]), end=" ")
            # print(" ")
            # msg = sensors
            # p.publish(msg)

            msg = s.recv_nb()
            if msg:
                print(msg)

            rate.sleep()
    except KeyboardInterrupt:
        print("bye ...")

    bot.drive_stop()
    # time.sleep(1)
    # bot.close()
    print("<<< Exiting >>>")


if __name__ == '__main__':
    main()
