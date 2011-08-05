import sys
def Main():
    s="%s<" % argv[0]
    for i,v in enumerate(argv[1:]):
        if 0<i:
            s=s+", "
        s=s+"typename "+v
    s=s+">\n%|"
    sys.stdout.write(s)
Main()
