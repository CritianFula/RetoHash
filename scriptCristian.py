#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Mar 10 10:27:08 2022

@author: cristianfula
"""

import hashlib

x = "c893bad68927b457dbed39460e6afd62"

f = open ('palabras.txt', 'r')

while(True):
    
    hashmd5 = hashlib.md5()
    linea = f.readline().replace("\n", "")
    hashmd5.update(linea.encode("UTF-8"))
    
    if hashmd5.hexdigest() == x:
        
        print("la palabra escondida es", linea)

        
        break
f.close()
