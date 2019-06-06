#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import sys
sys.setrecursionlimit(150000)

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
        self.cinta.append(self.tm['Blanco'])
        self.cinta.append(self.tm['Blanco'])
        
        for sym in self.string:
            self.cinta.append(sym)
            
        self.cinta.append(self.tm['Blanco'])
        self.cinta.append(self.tm['Blanco'])
        self.trans = self.tm['Transiciones']
        self.q = self.tm['Inicial']
        self.first_sym = self.cinta[2]
        self.l = []
        self.l1 = []
        self.a = self.string[1:]
        self.p_string = ""
        self.i = 2
        self.l1.append(self.q)
        
        for sym in self.string:
            self.l1.append(sym)
            
        self.l.append(self.l1)

        
    def read_t(self):
        self.l1 = []
        self.i += 1
        
        for t in self.trans:
            
            if(self.q == t[0] and self.first_sym == t[1]):
                
                if(t[4] == 'R'):
                    self.q = t[2]
                    self.first_sym = self.cinta[self.i]
                    self.p_string += t[3]
                    
                    for sym in self.p_string:
                        self.l1.append(sym)

                    self.l1.append(self.q)

                    for sym in self.a:
                        self.l1.append(sym)

                    self.l.append(self.l1)
                    self.a = self.a[1:]
                    self.read_t()   
                    

                if(t[4] == 'L'):
                    
                    self.q = t[2]
                    self.cinta = []
                    e = ""

                    self.cinta.append(self.tm['Blanco'])
                    self.cinta.append(self.tm['Blanco'])

                    for i in range(0,len(self.p_string)-1):
                        self.l1.append(self.p_string[i])
                        self.cinta.append(self.p_string[i])

                    self.l1.append(self.q)
                    self.l1.append(self.p_string[len(self.p_string)-1])
                    self.cinta.append(self.p_string[len(self.p_string)-1])
                    self.l1.append(t[3])
                    self.cinta.append(t[3])

                    for sym in self.a:
                        self.l1.append(sym)
                        self.cinta.append(sym)
                        e += sym

                    self.a = ""
                    self.a += t[3]
                    self.a += e
                    self.cinta.append(self.tm['Blanco'])
                    self.cinta.append(self.tm['Blanco'])
                    self.l.append(self.l1)
                    self.p_string = self.p_string[:len(self.p_string)-1]
                    self.first_sym = self.cinta[self.i-2]
                    self.i -= 2
                    self.read_t()


    def check(self):
        for sym in self.l[len(self.l)-1]:
            if(sym in self.tm['Finales']):
                return True

        return False
        
                                        
if __name__ == '__main__':
    args = sys.argv
    
    
    if(args[1] == '-help'):
        print("El programa recibe dos argumentos: un archivo .json donde está especificada la MT y una cadena a procesar")
        sys.exit()
    
    if(len(args) > 3):
        print('Sólo se necesitan 2 argumentos; el archivo .json con la descripción de la máquina de Turing y la cadena a procesar')
    else:
        
        TM = TM(args[1],args[2])
        TM.write_string()
        TM.read_t()

        l = []
        s = ""
        print('Las configuraciones son:')
        
        for t in TM.l:
            
            for sym in t:
                
                if(sym in TM.tm['Estados']):
                    
                    s += '|' + sym + "|"

                else:
                        
                    s += sym
                
            l.append(s)
            s = ""

        for con in l:

            print("-> " + con)

        if(TM.check()):
            print("La cadena es aceptada")

        else:

            print("La cadena no es acpetada")
