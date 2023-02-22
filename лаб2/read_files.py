from array import*
import graf

#считывания столбцов из двух файлов
def rf(l1, l2, u):
	f1_1 = array('d',[])
	f1_2 = array('d',[])
	f2_1 = array('d',[])
	f2_2 = array('d',[])


	with open(l1, 'r') as f1:
		for line in f1:
			f1_1.append(float((line.split()[0]).replace("D", "E")))
			f1_2.append(float((line.split()[1]).replace("D", "E")))
		
	with open(l2, 'r') as f1:
		for line in f1:
			f2_1.append(float((line.split()[0]).replace("D", "E")))
			f2_2.append(float((line.split()[1]).replace("D", "E")))

	graf.g(f1_1, f1_2, f2_1, f2_2, u, l1)			


