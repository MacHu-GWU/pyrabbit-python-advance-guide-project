#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
textwrap提供了以下功能:
1. 字符串按照指定宽度自动换行
2. 字符串等间距增加或取消缩进
"""

from __future__ import print_function
import textwrap

def example_wrap_and_fill():
    text = ("The textwrap module provides two convenience functions, wrap() and "
            "fill(), as well as TextWrapper, the class that does all the work, "
            "and two utility functions, dedent() and indent(). If you’re just "
            "wrapping or filling one or two text strings, the convenience "
            "functions should be good enough; otherwise, you should use an "
            "instance of TextWrapper for efficiency.")
    print("===================================================================")
    print(text)
    print("===================================================================")
    print("\n".join(textwrap.wrap(text, width=80)))
    print("===================================================================")
    print(textwrap.fill(text, width=80))
    
example_wrap_and_fill()

def example_indent_and_dedent():
    text = \
    """
for i in range(10):
\tprint(i)
    """
    print("===================================================================")
    print(text)
    print("===================================================================")
    indented_text = textwrap.indent(text, "\t")
    print(indented_text)
    print("===================================================================")
    dedented_text = textwrap.dedent(indented_text)
    print(dedented_text)
    print("===================================================================")
    
example_indent_and_dedent()
