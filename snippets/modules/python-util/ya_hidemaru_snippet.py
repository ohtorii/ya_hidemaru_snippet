# -*- coding: utf-8 -*-

import os
import configparser


class _ya_hidemaru(object):
    def __init__(self):
        #コマンドを除いた一行の文字列
        self.line_string=""

        #スニペットモジュールへの絶対パス
        self.module_dir=""

        #internalディレクトリへの絶対パス
        self.internal_dir=""
        
        self.__initialize()
        
    
    def __initialize(self):
        filename = os.environ["YA_HIDEMARU_FILE"]
        config=configparser.ConfigParser()
        config.read(filename,"UTF-16")

        section=config["hidemaru"]
        self.line_string =section["line_string"]
        self.module_dir  =section["module_dir"]
        self.internal_dir=section["internal_dir"]
        
        
        
g_instance=_ya_hidemaru()


def line_string():
    return g_instance.line_string

def module_dir():
    return g_instance.module_dir

def internal_dir():
    return g_instance.internal_dir
