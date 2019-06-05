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


    def write_string(self):
        self.cinta = []
        
        for sym in self.string:
            self.cinta.append(sym)
            
        self.cinta.append('_')
        self.cinta.append('_')
        self.trans = self.tm['Transiciones']
        self.q = self.tm['Inicial']
        self.first_sym = self.cinta[0]
        self.l = []
        self.l1 = []
        self.p_string = ""
        self.l1.append(self.q)
        
        for sym in self.cinta:
            self.l1.append(sym)
            
        self.l.append(self.l1)
        

    def read_t(self):
        self.l1 = []
        
        for t in self.trans:
            
            if(self.q == t[0] and self.first_sym == t[1]):
                self.q = t[2]
                self.p_string.append(self.first_sym)
                self.first_sym = t[3]
                
                if(t[4] == 'R'):
                    for sym in self.p_string:
                        self.l1.append(sym)
                    

if __name__ == '__main__':
    args = sys.argv
    if(len(args) > 3):
        print('Sólo se necesitan 2 argumentos; el archivo .json con la descripción de la máquina de Turing y la cadena a procesar')
    else:
        TM = TM(args[1],args[2])
        TM.write_string()
        TM.read_t()
        
