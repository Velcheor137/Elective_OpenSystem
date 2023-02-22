from matplotlib import pyplot as plt   
from matplotlib import style

#постройка графиков для 1 части задания
def g(f1_1, f1_2, f2_1, f2_2, u, l1):
	plt.plot(f1_1, f1_2, 'b')
	plt.plot(f2_1, f2_2, '--')
	plt.title('R = ' + str(float(((l1.split()[1]).replace(".dat", "")).replace("D", "E"))))
	plt.ylabel('ось Y')
	plt.xlabel('ось X')
	str1 ="1." + str(u) + ".png"
	plt.savefig(str1)
	plt.clf()
