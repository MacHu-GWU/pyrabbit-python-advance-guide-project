#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
repeat
"""

from itertools import repeat
import random
import time

if __name__ == "__main__":
    a = list(repeat(random.random(), 3))
    print(a)