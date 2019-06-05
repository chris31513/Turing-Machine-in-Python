#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys


class TM(object):

    def __init__(self,json_file,string):
        try:
            
            try:
                
                with open(json_file) as f:
                    self.tm = json.load(f)
                self.string = string
                
            except(FileNotFoundError) as e:
                
                raise Exception('El archivo {} no es un archivo .json'.format(json_file), e)
            
        except Exception as c:
            print(c.args[0])
            


if __name__ == '__main__':
    args = sys.argv
    if(len(args) > 3):
        print('Sólo se necesitan 2 argumentos; el archivo .json con la descripción de la máquina de Turing y la cadena a procesar')
    else:
        TM = TM(args[1],args[0])
        
