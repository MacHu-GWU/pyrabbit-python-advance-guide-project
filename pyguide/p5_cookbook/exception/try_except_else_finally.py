#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
强大的异常处理机制是Python的特色之一。用好异常处理是写出安全和稳定的代码的重要
技能。异常处理相关的关键字有:

try: 异常处理主代码块。

except: 尝试捕获一个异常。可以使用 ``except SomeException:`` 指定这个异常, 也可以
直接使用 ``except:`` 捕获任何异常。同时你可以使用 ``as`` 关键字, 进行
``except SomeException as e:`` 然后对 ``e`` 这个异常对象进行处理。注: 
``exception Exception:`` 能捕获任意异常。

else: 当没有任何一个except捕获到该异常时, 执行else中的代码, 当然你也可以直接将
这部分代码放到try语句下。但是这样做能够更清晰地标识出**有可能发生异常的部分**和
**肯定安全的部分**。

finally: 不管异常有没有被捕获, 在离开try代码块之前这部分都会被执行。

Reference: https://docs.python.org/2/tutorial/errors.html
"""

from __future__ import print_function

d = {"a": 1}

def raise_AttributeError():
    """抛出 ``AttributeError``。
    """
    d.a
    
def raise_KeyError():
    """抛出 ``KeyError``。
    """
    d["b"]

def raise_TypeError():
    """抛出 ``TypeError``。
    """
    d + 1

def example1():
    """假如你想这样处理异常:
    
    直接跳过什么都不做::
    
        try:
            raise_TypeError()
        except:
            pass # skip it
    """
    try:
        raise_TypeError()
    except:
        pass # skip it

def example2():
    """假如你想这样处理异常:
    
    1. 尝试鉴定几种可能的异常, e1, e2, ...
    2. if e1, 则执行a1(action 1), if e2, then a2, ...
    3. 如果都不是, 你希望**抛出这个异常**
    
    方法1::
    
        try:
            raise_TypeError()
        except AttributeError as e:
            pass # do something
        except KeyError as e:
            pass # do something
            
    或者使用这个也是一样的::
    
        try:
            raise_TypeError()
        except AttributeError as e:
            pass # do something
        except KeyError as e:
            pass # do something
        except:
            raise # raise the most recent exception
            
    在第三步的时候你如果想什么都不做, 则使用下面的代码::
    
        try:
            raise_TypeError()
        except AttributeError as e:
            pass # do something
        except KeyError as e:
            pass # do something
        except:
            pass
    """
    try:
        raise_TypeError()
    except AttributeError as e:
        pass # do something
    except KeyError as e:
        pass # do something
    except:
        raise # raise the most recent exception

if __name__ == "__main__":
    example1()
    example2()