#запись результата в файл result.txt
def res(m, l): 
	with open('result.txt', 'w') as f:
		for line in range(len(m)):
			f.write(str(m[line]) + " " + str(l[line]) + '\n')
