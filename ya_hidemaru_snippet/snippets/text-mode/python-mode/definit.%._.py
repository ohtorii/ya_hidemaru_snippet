"""
# before
definit x y z __flag

# after
def __init__(self,x,y,z,flag):
    self.x=x
    self.y=y
    self.z=z
    self__flag=flag
    |
"""
import sys

def Main():
    args=argv[1:]
    strped_arg=[s.lstrip("_") for s in args]
    head = "def __init__(self,";
    body = ",".join(strped_arg)
    tail = "):\n"
    
    s=head+body+tail
    for i in range(len(args)):
        s=s+"\tself.%s=%s\n" % (args[i], strped_arg[i])
    s=s+"\t%|"
    sys.stdout.write(s)

Main()
