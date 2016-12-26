#!/usr/bin/env python

import pyhidapi


def test_func():
    pyhidapi.hid_init()
    devs = pyhidapi.hid_enumerate()
    for dev in devs:
        print('---')
        print(dev.description())