from os import listdir

#считывания названия файла и запись нужных названий файлов в список
def listFile():
	files = listdir(".")
	f = []
	for file in files:
		if file.endswith('.dat'):
			f.append(file)

	return f

