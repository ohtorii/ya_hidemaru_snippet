"""
# before
class_ hoge x y z

# after
class hoge(object):
    def __init__(self,x,y,z):
        self._x=x
        self._y=y
        self._z=z
"""
import sys
def Main():
    ClassName = argv[1]
    s1 = "class %s(object):\n" % ClassName
    s2 = "\tdef __init__(self," + ",".join(argv[2:]) + "):\n"
    s3 = ""
    for v in argv[2:]:
        s3=s3+"\t\tself._%s=%s\n" % (v,v)
    s4="\t\t%|"
    sys.stdout.write(s1+s2+s3+s4)

Main()
