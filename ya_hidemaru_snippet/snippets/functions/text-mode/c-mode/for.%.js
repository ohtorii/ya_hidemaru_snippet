/*
# before
for i

# after
for(size_t i=0 ; i<| ; ++i){
	
}
*/
var arg0 = WScript.Arguments(0);
var arg1 = WScript.Arguments(1);
WScript.StdOut.Write(arg0 + "(size_t " + arg1 + "=0 ; " + arg1 + "<%| ; ++" + arg1 + "){\n");
WScript.StdOut.Write("\t\n");
WScript.StdOut.Write("}");