#
#argv[0]="class"
#argv[1]=class_name
#argv[2]=arg0
#       :
#       :
#argv[N]=argN
#
import sys

g_int   =set((  "char","short","int","long","__int64",
                "u8","s8","u16","s16","s32","u32","s64","u64","s128","u128"
                "uint8","sint8","uint16","sint16","uint32","sint32","uint64","sint64","uint128","sint128",))
g_float =set(("float","f32","float32"))
g_double=set(("double","f64","float64"))
g_scaler=g_int|g_float|g_double;
g_member_prefix = "m_";

def Main():
    head={"class":argv[0], "name":argv[1]}

    #
    #class ClassName{
    #
    print("%(class)s %(name)s{" % head)
    print("public:")


    #
    #ctor
    #
    #ClassName(foo bar, hoge spam){
    #
    if len(argv)%2:
        argv.append(" ")
    s="    %(name)s(%%|" % head;
    n=len(argv)
    for i in range(2,n,2):
        if(2<i):
            s=s+","
        typen_name = argv[i]
        value_name = argv[i+1]
        if typen_name in g_scaler:
            tmp="%s %s" % (typen_name,value_name)
        else:
            tmp="const %s &%s" % (typen_name,value_name)
        s=s+tmp;
    print("%s){" % s)

    #
    #ctor implement.
    #
    for i in range(2,n,2):
        if argv[i] in g_int:
            print("\t\t%s=0;" % argv[i+1])
        elif argv[i] in g_float:
            print("\t\t%s=0.f;" % argv[i+1])
        elif argv[i] in g_double:
            print("\t\t%s=0.0;" % argv[i+1])
        else:
            pass
    print("\t};")

    #
    #dtor
    #
    print(  "\t~%(name)s(){\n"  \
            "\t};"  % head )

    print("protected:");

    #
    #Non copyble.
    #
    print(  "private:\n"\
            "\t%(name)s(const %(name)s&);\n"\
            "\t%(name)s &operator=(const %(name)s&);"  % head )

    #
    #member
    #
    s=""
    index=0
    for i in range(2,n,2):
        typen_name = argv[i]
        value_name = argv[i+1]
        if index:
            s=s+"\n";
        tmp="\t%s %s;" % (typen_name,value_name)
        s=s+tmp;
        index=index+1;
    print(s)

    #
    #finish
    #
    sys.stdout.write("};");

Main()
