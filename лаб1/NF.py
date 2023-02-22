from array import*

#переводим числа из названий файла в float
def NF(list):
	result = array('d',[])
	for i in range(len(list)):
		list[i] = ((list[i].split()[1]).replace(".dat", "")).replace("D", "E")
		result.append(float(list[i]))
	return result