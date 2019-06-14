# -*- coding: utf-8 -*-

"""
#Description:GitHub Flavored Markdown(GFM)

=========
Format
=========
table column=1 row=1

=========
Example0
=========
#before
table

#after
|header1|
|:--:|
||

=========
Example1
=========
#before
table 3

#after
header1|header2|header3|
|:--:|:--:|:--:|

=========
Example2
=========
#before
table 3 2

header1|header2|header3|
|:--:|:--:|:--:|
||||
||||
"""
import sys

def Clip(x):
    if x < 1:
        return 1
    return x

def ToInt(s):
    try:
        return int(s)
    except ValueError:
        pass
    return 1

def MakeDefaultTable():
    sys.stdout.write(\
    "|%|header1|\n"
    "|:--:|\n"
    "||")

def MakeHeaderOnlyTable(column_num):
    column_num=Clip(column_num)
    header=[]
    align=[]
    for column in range(1,1+column_num):
        header.append("|header%d"%column)
        align.append("|:--:")

    #close tail.
    header.append("|")
    align.append("|")

    #"|header1|" -> "|%|header1|"
    header[0]="|%|"+header[0][1:]

    sys.stdout.write("".join(header))
    sys.stdout.write("\n")
    sys.stdout.write("".join(align))

def MakeTable(column_num,row_num):
    column_num=Clip(column_num)
    row_num=Clip(row_num)

    MakeHeaderOnlyTable(column_num)
    
    row_list=[]
    for row in range(row_num):
        for column in range(1,column_num+1):
            row_list.append("|")

        #close tail.
        row_list.append("|")
        
        sys.stdout.write("\n")
        sys.stdout.write("".join(row_list))
        
        
        #sys.stdout.write("\n")
        row_list.clear()


def main(argv):
    command_name=argv[0]
    args        =argv[1:]
    n           =len(args)
    if n==0:
        MakeDefaultTable()
        return
    if n==1:
        column_num=ToInt(args[0])
        MakeHeaderOnlyTable(column_num)
        return
    if n==2:
        column_num=ToInt(args[0])
        row_num=ToInt(args[1])
        MakeTable(column_num,row_num)

if __name__ == "__main__":
    main(sys.argv[1:])
