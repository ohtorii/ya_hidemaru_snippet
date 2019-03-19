'
'   # before
'   if condition
'
'   # after
'   if(condition){
'       |
'   }
'
Set args = WScript.Arguments
WScript.StdOut.WriteLine args.item(0) & "(" & args.item(1) & "){"
WScript.StdOut.WriteLine "	%|"
WScript.StdOut.Write "}"