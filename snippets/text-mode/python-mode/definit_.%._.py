import sys
def MakeArgs():
    head = "def __init__(self,";
    body = ",".join(argv[1:])
    tail = "):\n"
    return head+body+tail

def Main():
    s=MakeArgs()
    for v in argv[1:]:
        s=s+"\tself.__%s=%s\n" % (v,v)
    s=s+"\t%|"
    sys.stdout.write(s)

Main()
