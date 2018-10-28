"""template<>

# before
te foo bar spam

# after
template<typename foo, typename bar, typename spam>
"""
import sys
def Main():
    s="template<"
    for i,v in enumerate(argv[1:]):
        if 0<i:
            s=s+", "
        s=s+"typename "+v
    s=s+"%|>"
    sys.stdout.write(s)
Main()
