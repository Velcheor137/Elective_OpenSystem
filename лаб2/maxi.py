from array import*
import graf2

#функция ищет максимум  во второй половине psi
def maxi(l1):
	psi = array('d',[])
	p = array('d',[])
	max_two_pol = array('d',[])

	for name in l1:
		with open(name, 'r') as f1:
			for line in f1:
				l = line.split()
				psi.append(float((l[1]).replace("D", "E")))
		max_two_pol.append(max(psi[len(psi)//2:]))
		del psi[:]
		
	for i in range(len(l1)):
		p.append(float(((l1[i].split()[1]).replace(".dat", "")).replace("D", "E")))
	graf2.gg(max_two_pol, p)
	