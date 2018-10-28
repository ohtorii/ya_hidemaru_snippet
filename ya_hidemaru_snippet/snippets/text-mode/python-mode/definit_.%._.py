"""
# before
definit_ x y z

# after
def __init__(self,x,y,z):
    self._x=x
    self._y=y
    self._z=z
    |
"""
import sys
def MakeArgs():
    head = "def __init__(self,";
    body = ",".join(argv[1:])
    tail = "):\n"
    return head+body+tail

def Main():
    s=MakeArgs()
    for v in argv[1:]:
        s=s+"\tself._%s=%s\n" % (v,v)
    s=s+"\t%|"
    sys.stdout.write(s)

Main()
