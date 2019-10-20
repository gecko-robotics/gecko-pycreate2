from collections import namedtuple

class create_st(namedtuple('create_st', 'bumps_wheeldrops cliff bumper encoder timestamp')):
    """
    Create2 key sensors
    """
    __slots__ = ()

    def __new__(cls, bw, c, b, e, ts=None):
        # cls.id = GeckoMsgFlags.create
        cls.id = 100
        if ts:
            return cls.__bases__[0].__new__(cls, bw, c, b, e, ts)
        else:
            return cls.__bases__[0].__new__(cls, bw, c, b, e, time.time())

class battery_st(namedtuple('battery_st', 'charge capacity voltage current timestamp')):
    """
    Create2 battery
    """
    __slots__ = ()

    def __new__(cls, c, w, v, a, ts=None):
        # cls.id = GeckoMsgFlags.create
        cls.id = 101
        if ts:
            return cls.__bases__[0].__new__(cls, c, w, v, a, ts)
        else:
            return cls.__bases__[0].__new__(cls, c, w, v, a, time.time())
