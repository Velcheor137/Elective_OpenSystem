from array import*

#функция считывает второй столбец каждого файла, переводим в float, находим наибольшее 
def bolsh(list):
	result = array('d',[])
	res = array('d',[])
	for name in list:
		with open(name, 'r+') as f:
			for line in f:
				result.append(float((line.split()[1]).replace("D", "E")))
		#
		max = 0
		for o in range(len(result)):
			if max==0:
				max = result[o]
			else:
				if result[o] > result[0-1]:
					max = result[o]
		res.append(max)
	
	return res