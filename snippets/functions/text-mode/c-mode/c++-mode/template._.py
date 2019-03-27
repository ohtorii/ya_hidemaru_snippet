# -*- coding: utf-8 -*-
"""template<>

# before
template foo bar spam

# after
template<typename foo, typename bar, typename spam>
"""
import sys
def Main(argv):
    s="template<"
    for i,v in enumerate(sys.argv[2:]):
        if 0<i:
            s=s+", "
        s=s+"typename "+v
    s=s+"%|>"
    sys.stdout.write(s)
Main(sys.argv[1:])
