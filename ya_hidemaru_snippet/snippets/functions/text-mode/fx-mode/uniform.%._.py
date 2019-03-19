#
#argv[0]="uniform"
#argv[1]=type
#argv[2]=name
#       :
#       :
#argv[N]=argN
#
import sys

_g_name=""

#'\tstring UIWidget = "";\n'
_g_type1 =  '%(type)s %(name)s<\n'              \
            '\tstring UIName   = "";\n'         \
            '\t%(type)s UIMin     = %(min)s;\n' \
            '\t%(type)s UIMax     = %(max)s;\n' \
            '\t%(type)s UIStep    = %(step)s;\n'\
            '> = %(default)s;';

_g_type_n = '%(type)s %(name)s<\n'              \
            '\tstring UIName   = "";\n'         \
            '> = %(default)s;';

_g_type_bool =  '%(type)s %(name)s<\n'              \
                '\tstring UIName   = "";\n'         \
                '> = %(default)s;';

_g_type_rgb =   '%(type)s %(name)s<\n'              \
                '\tstring UIName   = "";\n'         \
                '\tstring UIObject = "%(obj)s";\n'  \
                '\tstring UIWidget = "Color";\n'    \
                '> = %(default)s;';



def f_float():
    a = {   "type"      :"float",
            "name"      :_g_name,
            "min"       :"0.0",
            "max"       :"1.0",
            "step"      :"0.01",
            "default"   :"0.0",
        }
    sys.stdout.write(_g_type1%a)

def f_float3():
    a = {   "type"      :"float3",
            "name"      :_g_name,
            "default"   :"{0.0, 0.0, 0.0}",
        }
    sys.stdout.write(_g_type_n%a)

def f_float4():
    a = {   "type"      :"float4",
            "name"      :_g_name,
            "default"   :"{0.0, 0.0, 0.0, 0.0}",
        }
    sys.stdout.write(_g_type_n%a)

def f_int():
    a = {   "type"      :"int",
            "name"      :_g_name,
            "min"       :"0",
            "max"       :"100",
            "step"      :"1",
            "default"   :"0",
        }
    sys.stdout.write(_g_type1%a)

def f_int3():
    a = {   "type"      :"int3",
            "name"      :_g_name,
            "default"   :"{0, 0, 0}",
        }
    sys.stdout.write(_g_type_n%a)

def f_int4():
    a = {   "type"      :"int4",
            "name"      :_g_name,
            "default"   :"{0, 0, 0, 0}",
        }
    sys.stdout.write(_g_type_n%a)

def f_bool():
    a = {   "type"      :"int4",
            "name"      :_g_name,
            "default"   :"false",
        }
    sys.stdout.write(_g_type_bool%a)

def f_rgb():
    a = {   "type"      :"float3",
            "name"      :_g_name,
            "obj"       : "RGB",
            "default"   :"{1.0, 1.0, 1.0}",
        }
    sys.stdout.write(_g_type_rgb%a)

def f_rgba():
    a = {   "type"      :"float4",
            "name"      :_g_name,
            "obj"       : "RGBA",
            "default"   :"{1.0, 1.0, 1.0, 1.0}",
        }
    sys.stdout.write(_g_type_rgb%a)

_g_jump_tbl={
    "float":f_float,
    "float3":f_float3,
    "float4":f_float4,
    "int":f_int,
    "int3":f_int3,
    "int4":f_int4,
    "bool":f_bool,
    "rgb":f_rgb,
    "rgba":f_rgba,
};

def Main():
    global _g_name

    _g_name="%|"
    try:
        _g_name = argv[2]
    except IndexError:
        pass

    uniform_type = argv[1].lower()
    func = _g_jump_tbl[uniform_type]
    func()


Main()
