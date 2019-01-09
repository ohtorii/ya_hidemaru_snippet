"""
#   # before
class vector float x float y float z

#   # after
/// <summary>
/// Summary description for vector
/// </summary>
public class vector{
    public vector(float x,float y,float z){
        |
    }
    private float x;
    private float y;
    private float z;
}

#
#memo
#
argv[0]="class"
argv[1]=class_name
argv[2]=arg0
       :
       :
argv[N]=argN
"""
import sys

def Main():
    head={"class":argv[0], "name":argv[1]}

    #
    #class ClassName{
    #
    print(("/// <summary>\n"                        +
          "/// Summary description for %(name)s\n"  +
          "/// </summary>\n"                        +
          "public %(class)s %(name)s{")             % head)


    #
    #ctor
    #
    #ClassName(foo bar, hoge spam){
    #
    if len(argv)%2:
        argv.append(" ")
    s="    public %(name)s(" % head;
    n=len(argv)
    for i in range(2,n,2):
        if(2<i):
            s=s+","
        typen_name = argv[i]
        value_name = argv[i+1]
        tmp="%s %s" % (typen_name,value_name)
        s=s+tmp;
    
    print(("%s){\n" +
          "\t\t%%|\n"   +
          "\t}"     ) % s );


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
        tmp="\tprivate %s %s;" % (typen_name,value_name)
        s=s+tmp;
        index=index+1;
    print(s)

    #
    #finish
    #
    #print("};");
    sys.stdout.write("}");

Main()
