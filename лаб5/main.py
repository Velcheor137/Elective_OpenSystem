import re
import os

#Author. Title. BookTitle. Type: Editor' Journal // Number : Edition .-
#Address .- Publisher : School: Year .- Volume .- Chapter .- Pages .- 
#Numpages .- Series .- Note .- Nite .- File .- Addendum .-
def Article(mas):
	y = "y."
	p = "p. "
	vol = "vol. "
	s = ""

	if("Language" in mas):
		i = mas.index("Language")
		if(mas[i-1] == "russian"):
			y = "год. "
			p = "с. "
			vol = "вып. "

	if("Author" in mas):
		i = mas.index("Author")
		s +=mas[i-1] + " "
	if("Title" in mas):
		i = mas.index("Title")
		s +=mas[i-1] + " // "
	if("Journal" in mas):
		i = mas.index("Journal")
		s +=mas[i-1] + " "
	if("Year" in mas):
		i = mas.index("Year")
		s +=y + mas[i-1] + " .- "
	if("Pages" in mas):
		i = mas.index("Pages")
		s +=p + mas[i-1] + " .- "
	if("Volume" in mas):
		i = mas.index("Volume")
		s +=vol + mas[i-1] + " .- "
	if("Address" in mas):
		i = mas.index("Address")
		s +=mas[i-1] + ".- "
	if("File" in mas):
		i = mas.index("File")
		s +=":" + mas[i-1] + " .- "
	if("Owner" in mas):
		i = mas.index("Owner")
		s +=mas[i-1] + ""

	s = s.replace(' ', '', 1)
	with open('res.bib', 'a', encoding="utf8") as file:
		file.write(s+'\n'+'\n')

def Book(mas):
	y = "y."
	p = "p. "
	vol = "vol. "
	s = ""

	if("Language" in mas):
		i = mas.index("Language")
		if(mas[i-1] == "russian"):
			y = "год. "
			p = "с. "
			vol = "вып. "

	if("Author" in mas):
		i = mas.index("Author")
		s +=mas[i-1] + " "
	if("Title" in mas):
		i = mas.index("Title")
		s +=mas[i-1] + " // "
	if("Publisher" in mas):
		i = mas.index("Publisher")
		s +=mas[i-1] + " "
	if("Year" in mas):
		i = mas.index("Year")
		s +=y + mas[i-1] + " .- "
	if("Pages" in mas):
		i = mas.index("Pages")
		s +=p + mas[i-1] + " .- "
	if("Volume" in mas):
		i = mas.index("Volume")
		s +=vol + mas[i-1] + " .- "
	if("Address" in mas):
		i = mas.index("Address")
		s +=mas[i-1] + ".- "
	s = s.replace(' ', '', 1)
	with open('res.bib', 'a', encoding="utf8") as file:
		file.write(s+'\n'+'\n')

def Conference(mas):
	y = "y."
	p = "p. "
	vol = "vol. "
	s = ""

	if("Language" in mas):
		i = mas.index("Language")
		if(mas[i-1] == "russian"):
			y = "год. "
			p = "с. "
			vol = "вып. "

	if("Author" in mas):
		i = mas.index("Author")
		s +=mas[i-1] + " "
	if("Title" in mas):
		i = mas.index("Title")
		s +=mas[i-1] + " // "
	if("BookTitle" in mas):
		i = mas.index("BookTitle")
		s +=mas[i-1] + ".- "
	if("Year" in mas):
		i = mas.index("Year")
		s +=y + mas[i-1] + " .- "
	if("Address" in mas):
		i = mas.index("Address")
		s +=mas[i-1] + ".- "
	if("Pages" in mas):
		i = mas.index("Pages")
		s +=p + mas[i-1] + " .- "
	s = s.replace(' ', '', 1)
	with open('res.bib', 'a', encoding="utf8") as file:
		file.write(s+'\n'+'\n')

def PhdThesis(mas):
	y = "y."
	p = "p. "
	vol = "vol. "
	s = ""

	if("Language" in mas):
		i = mas.index("Language")
		if(mas[i-1] == "russian"):
			y = "год. "
			p = "с. "
			vol = "вып. "

	if("Author" in mas):
		i = mas.index("Author")
		s +=mas[i-1] + " "
	if("Title" in mas):
		i = mas.index("Title")
		s +=mas[i-1] + " // "
	if("School" in mas):
		i = mas.index("School")
		s +=mas[i-1] + " .- "
	if("Year" in mas):
		i = mas.index("Year")
		s +=y + mas[i-1] + " .- "
	if("Address" in mas):
		i = mas.index("Address")
		s +=mas[i-1] + ".- "
	if("Type" in mas):
		i = mas.index("Type")
		s +=mas[i-1] + ".- "
	if("Number" in mas):
		i = mas.index("Number")
		s +=mas[i-1] + ""
	s = s.replace(' ', '', 1)
	with open('res.bib', 'a', encoding="utf8") as file:
		file.write(s+'\n'+'\n')

def Booklet(mas):
	s = ""
	if("Title" in mas):
		i = mas.index("Title")
		s +=mas[i-1] + " // "
	s = s.replace(' ', '', 1)
	with open('res.bib', 'a', encoding="utf8") as file:
		file.write(s+'\n'+'\n')



formul = re.compile(r'(?<=@\{)[а-яА-ЯёЁa-zA-Z0-9\-\.\•]+|(?<=\=\s\{)[а-яА-ЯёЁa-zA-Z0-9:\s,\-\.\•]+|[а-яА-ЯёЁa-zA-Z\-\•]+(?=\s+\=\s)|@[а-яА-ЯёЁa-zA-Z0-9\-\.\•]+')
with open('biblio.bib', encoding="utf8") as bib:
	b = bib.read()
	r = re.findall(formul, b)
	print(r)
	mas = []


	for i in reversed(r):
		if (i.find("@") == 0):
			if(i == "@Article"):
				Article(mas)
			elif(i == "@Book"):
				Book(mas)
			elif(i == "@Conference"):
				Conference(mas)
			elif(i == "@PhdThesis"):
				PhdThesis(mas)
			else:
				Booklet(mas)
			mas.clear()
		else:
			mas.append(i)
		









