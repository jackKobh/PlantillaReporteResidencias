#!/usr/bin/env python
# -*- coding: utf-8 -*-
import unicodedata
import os
import re
fileIn = open("Introduccion.txt","r")
fileOut = open("salida.txt", "w")

texto = fileIn.read()

# def elimina_tildes(s):
#    return ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
 
# print(elimina_tildes(texto))


patron = re.compile('í+') 

res = patron.sub("\\'i",texto)
# print(res)
fileOut.write(res)
# for line in fileIn:
# 	line = line.replace("á", "\\'a")
# 	line = line.replace("é", "\\'e")
# 	line = line.replace("í", "\\'i")
# 	line = line.replace("ó", "\\'o")
# 	line = line.replace("ú", "\\'u")
# 	line = line.replace("ñ", "\\~n")
# 	line = line.replace("Á", "\\'A")
# 	line = line.replace("É", "\\'E")
# 	line = line.replace("Í", "\\'I")
# 	line = line.replace("Ó", "\\'O")
# 	line = line.replace("Ú", "\\'U")
# 	line = line.replace("Ñ", "\\~N")
# 	line = line.replace("”", "\"")
# 	line = line.replace("“", "\"")
# 	line = line.replace("#", "\#")
# 	line = line.replace("ú", "\\'u")

	
	
# 	fileOut.write(line)