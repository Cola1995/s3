import os,sys


Path=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

sys.path.append(Path)
from ccc import test1
test1.Ca()