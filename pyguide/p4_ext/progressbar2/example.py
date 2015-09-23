#!/usr/bin/python
# -*- coding: utf-8 -*-

from __future__ import print_function

import sys
import time

from progressbar import AnimatedMarker, Bar, BouncingBar, Counter, ETA, \
    FileTransferSpeed, FormatLabel, Percentage, \
    ProgressBar, ReverseBar, RotatingMarker, \
    SimpleProgress, Timer, AdaptiveETA, AdaptiveTransferSpeed

examples = []

def example(fn):
    def wrapped():
        try:
            sys.stdout.write('Running: %s\n' % fn.__name__)
            fn()
            sys.stdout.write('\n')
        except KeyboardInterrupt:
            sys.stdout.write('\nSkipping example.\n\n')

    examples.append(wrapped)
    return wrapped

# @example
# def with_example0():
#     with ProgressBar(maxval=10) as progress:
#         for i in range(10):
#             # do something
#             time.sleep(1)
#             progress.update(i)

# @example
# def with_example1():
#     with ProgressBar(maxval=10, redirect_stdout=True) as p:
#         for i in range(10):
#             # do something
#             p.update(i)
#             time.sleep(1)

# @example
# def example0():
#     pbar = ProgressBar(widgets=[Percentage(), Bar()], maxval=10).start()
#     for i in range(10):
#         # do something
#         time.sleep(1)
#         pbar.update(i + 1)
#     pbar.finish()

# @example
# def example1():
#     widgets = ['Test: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
#                ' ', ETA(), ' ', FileTransferSpeed()]
#     pbar = ProgressBar(widgets=widgets, maxval=1000).start()
#     for i in range(100):
#         # do something
#         pbar.update(10 * i + 1)
#     pbar.finish()

# @example
# def example7():
#     pbar = ProgressBar()  # Progressbar can guess max_value automatically.
#     for i in pbar(range(8)):
#         time.sleep(0.001)
        
if __name__ == '__main__':
    try:
        for example in examples:
            example()
    except KeyboardInterrupt:
        sys.stdout('\nQuitting examples.\n')