#!/usr/bin/env python
import sys
import os.path
from compilationengine import CompilationEngine


def main_of_analizer(jackfilename):

    #getting jack file name    
    (jfilename, jextension) = os.path.splitext(jackfilename)
    jackxml = jfilename + ".xml" #just to be consistent with the book
      
    compiler = CompilationEngine(jackfilename, jackxml)





def mainf_(fileName):
    if os.path.isfile(fileName):
        main_of_analizer(fileName)
    else:
        print 'The file : %s is not exsist' % fileName


f1='C:\XXX_Python\Jack_Parser_4.9\Jack_code\Main.jack'
f2='C:\XXX_Python\Jack_Parser_4.9\Jack_code\SquareGame.jack'
f3='C:\XXX_Python\Jack_Parser_4.9\Jack_code\Square.jack'
f4='C:\XXX_Python\Jack_Parser_4.9\Jack_code\Dictionary.jack'
f5='C:\XXX_Python\Jack_Parser_4.9\Jack_code\MainArray.jack'
mainf_(f1)
mainf_(f2)
mainf_(f3)
#mainf_(f4)
mainf_(f5)
