from matplotlib import pyplot as plt   
from matplotlib import style
import numpy as np

def gg(psi_m, R):
	plt.plot(R, psi_m, marker = 'o')
	plt.title('Лабораторная работа №2')
	plt.ylabel('ось Y')
	plt.xlabel('ось X')
	str1 ="2" + ".png"
	plt.savefig(str1)
	plt.clf()