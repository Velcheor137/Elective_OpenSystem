import numpy as np
from array import*
import read_files
import maxi

#функция разделяет список файлов на два массива, с psi и psi2
def r(list):
	#l1 = array('d',[])
	#l2 = array('d',[])

	l1 = np.array_split(list, 2)[1]
	l2 = np.array_split(list, 2)[0]

	u = 0
	for i in range(len(l1)):
		read_files.rf(l1[i], l2[i], u)
		u = u + 1

	maxi.maxi(l2)



	
	


