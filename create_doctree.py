from __future__ import print_function
from docfly import Docfly
import shutil
 
try:
    shutil.rmtree(r"source\pyguide")
except Exception as e:
    print(e)
     
docfly = Docfly("pyguide", dst="source")
docfly.fly()