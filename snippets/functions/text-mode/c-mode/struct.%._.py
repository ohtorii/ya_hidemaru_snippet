# -*- coding: utf-8 -*-
"""
# before
struct vector float x float y float z

# after
struct vector{
    float x;
    float y;
    float z;
};

"""
import sys

def Main(argv):
    head={"class":argv[0], "name":argv[1]}
    
    #
    #struct StructName{
    #
    print("%(class)s %(name)s{" % head)
    
    #
    #member
    #
    if len(argv)%2:
        argv.append(" ")
    n=len(argv)
    s=""
    index=0
    for i in range(2,n,2):
        type_name  = argv[i]
        value_name = argv[i+1]
        if index:
            s=s+"\n";
        tmp="\t%s %s;" % (type_name,value_name)
        s=s+tmp;
        index=index+1;
    print(s)

    #
    #finish
    #
    #print("};");
    sys.stdout.write("};");

Main(sys.argv[1:])