#!/usr/bin/env python
# -*- coding: utf-8 -*-

from __future__ import print_function
import binascii
import pickle
import pprint

class JsonDict(object):
    """A dictionary container but item can be set and get via ``self.attributes``.
    """
    def __init__(self, d):
        for key, value in d.items():
            self.__setattr__(key, value)
    
    def __setattr__(self, key, value):
        """A customized set attribute method.
         
        customized ``__setattr__`` method can prevent from using reserved method
        name as an attribute name.
         
        if you don't need this feature, just delete this ``__setattr__`` method.
        """
        all_method = [
            method for method in dir(self) if callable(getattr(self, method))]
        if key not in all_method:
            object.__setattr__(self, key, value)
        else:
            raise AttributeError("'%s' is a reserved attribute name!" % key)
        
    def __getitem__(self, key):
        return self.__getattribute__(key)
    
    def __setitem__(self, key, value):
        return self.__setattr__(key, value)
    
    def __str__(self):
        return pprint.pformat(self.__dict__)
    
    def to_dict(self):
        return self.__dict__
    
    def to_bytes(self):
        return pickle.dumps(self.__dict__)
    
    def to_string(self):
        return binascii.b2a_base64(pickle.dumps(self.__dict__)).decode("utf-8")
    
    @staticmethod
    def from_dict(d):
        return JsonDict(d)
    
    @staticmethod
    def from_bytes(b):
        return JsonDict(pickle.loads(b))
    
    @staticmethod
    def from_string(s):
        return JsonDict(pickle.loads(binascii.a2b_base64(s)))
    
if __name__ == "__main__":
    
    def test_JsonDict():
        jd = JsonDict({"a": 1, "b": 2})
        jd["c"] = 3
        jd.d = 4
        print(jd["a"]) # 1
        print(jd.b) # 2
        print(jd["c"]) # 3
        print(jd.d) # 4
        
        try:
            jd.to_dict = 100 # AttributeError
        except Exception as e:
            print(e)
        try:
            jd.to_bytes = 100 # AttributeError
        except Exception as e:
            print(e)
        try:
            jd.to_string = 100 # AttributeError
        except Exception as e:
            print(e)
        
        d = jd.to_dict()
        b = jd.to_bytes()
        s = jd.to_string()
        print(d)
        print(b)
        print(s)
        print(JsonDict.from_dict(d))
        print(JsonDict.from_bytes(b))
        print(JsonDict.from_string(s))
    
    test_JsonDict()