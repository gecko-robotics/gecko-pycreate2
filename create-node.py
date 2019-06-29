#!/usr/bin/env python3
# -*- coding: utf-8 -*-
##############################################
# The MIT License (MIT)
# Copyright (c) 2019 Kevin Walchko
# see LICENSE for full details
##############################################
from  pycreate2 import Create2
from pygecko.multiprocessing import geckopy

key = "localhost"

def main():
    print("<<< Starting Roomba >>>")
    bot = Create2()
    bot.start()
    bot.safe()
    
    geckopy.init_node()
    rate = geckopy.Rate(10)  # loop rate

    topic = kwargs.get('topic')
    
    s = geckopy.subConnectTCP(key, 'cmd')
    if s is None:
        raise Exception("subscriber is None")
        
    p = geckopy.pubBinderTCP(key,'create2')
    if p is None:
        raise Exception("publisher is None")
    
    print("<<< Starting Loop >>>")
    try:
        while not geckopy.is_shutdown():
            sensors = bot.get_sensors()  # returns all data
            msg = sensors
            p.publish(msg)
            
            msg = s.recv_nb()
            if msg:
                print(msg)
            
            rate.sleep()
    except KeyboardInterrupt:
        print("bye ...")
    
    bot.drive_stop()
    time.sleep(1)
    bot.close()
    pirnt("<<< Exiting >>>")
        

if __name__ == '__main__':
    main()
