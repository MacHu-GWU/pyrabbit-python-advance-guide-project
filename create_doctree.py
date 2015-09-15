from __future__ import print_function
from docfly import Docfly
import os

try:
    os.remove(r"source\pyguide")
except Exception as e:
    print(e)
    
docfly = Docfly("pyguide")
docfly.dst = r"source"
docfly.fly()