#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
LEVEL:

CRITICAL    50
ERROR       40
WARNING     30
INFO        20
DEBUG       10
NOTSET      0
"""

from datetime import datetime
import logging

logger = logging.getLogger("example")

# Debug level
logger.setLevel(logging.DEBUG)

# Print screen level
ch = logging.StreamHandler()
ch.setLevel(logging.INFO)
logger.addHandler(ch)

# File and format
fh = logging.FileHandler("%s.log" % datetime.strftime(datetime.now(), "%Y-%m-%d_%H-%M-%S"))
formatter = logging.Formatter("[%(asctime)s][%(name)s][%(levelname)s][%(message)s]")
fh.setFormatter(formatter)
logger.addHandler(fh)

logger.debug("debug")
logger.info("info")