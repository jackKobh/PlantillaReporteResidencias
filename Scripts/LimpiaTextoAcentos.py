fileIn = open("Introduccion.tex","r")
fileOut = open("salida.tex", "w")

for line in fileIn:
	line = line.replace("á", "\\'a")
	line = line.replace("é", "\\'e")
	line = line.replace("í", "\\'i")
	line = line.replace("ó", "\\'o")
	line = line.replace("ú", "\\'u")
	line = line.replace("ñ", "\\~n")
	line = line.replace("Á", "\\'A")
	line = line.replace("É", "\\'E")
	line = line.replace("Í", "\\'I")
	line = line.replace("Ó", "\\'O")
	line = line.replace("Ú", "\\'U")
	line = line.replace("Ñ", "\\~N")
	line = line.replace("”", "\"")
	line = line.replace("“", "\"")
	line = line.replace("#", "\#")

	
	
	fileOut.write(line)