"""
# before
class hoge x y z __flag

# after
class hoge(object):
    __slots__=("__weakref__","x","y","z","__flag")
    def __init__(self,x,y,z,flag):
        self.x=x
        self.y=y
        self.z=z
        self.__flag=flag
        |
"""
import sys
def Main():
    ClassName = argv[1]
    args=argv[2:]
    strped_arg=[s.lstrip("_") for s in args]
    s1 = "class %s(object):\n" % ClassName
    slots='\t__slots__=("__weakref__"' + "".join([',"%s"'%s for s in args]) + ')\n'
    s2 = "\tdef __init__(self," + ",".join(strped_arg) + "):\n"
    s3 = ""
    for i in range(len(args)):
        s3=s3+"\t\tself.%s=%s\n" % (args[i],strped_arg[i])
    s4="\t\t%|"
    sys.stdout.write(s1+slots+s2+s3+s4)

Main()
