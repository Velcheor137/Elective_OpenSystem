import sqlite3
import re
import copy

def from_file():
	formul = re.compile(r'(?<=@\{)[а-яА-ЯёЁa-zA-Z0-9\-\.\•]+|(?<=\=\s\{)[а-яА-ЯёЁa-zA-Z0-9:\s,\-\.\•]+|[а-яА-ЯёЁa-zA-Z\-\•]+(?=\s+\=\s)|@[а-яА-ЯёЁa-zA-Z0-9\-\.\•]+')
	with open('biblio.bib', encoding="utf8") as bib:
		b = bib.read()
		r = re.findall(formul, b)
	for i in range(len(r)):
		r[i] = r[i].strip()
		r[i] = r[i].rstrip('.')
	return r

def create_bd():
	aut = """CREATE TABLE IF NOT EXISTS author(id INT NOT NULL PRIMARY KEY, name TEXT) """
	jour = """CREATE TABLE IF NOT EXISTS journal(id INT NOT NULL PRIMARY KEY, name TEXT) """
	art = """CREATE TABLE IF NOT EXISTS article(id INT NOT NULL PRIMARY KEY, name TEXT, year INTEGER) """
	ln = """CREATE TABLE IF NOT EXISTS link(article INTEGER, journal INTEGER , author INTEGER) """
	sql.execute(aut)
	sql.execute(jour)
	sql.execute(art)
	sql.execute(ln)

def search_partial_text(src, dst):
    dst_buf = dst
    result = 0
    for char in src:
        if char in dst_buf:
            dst_buf = dst_buf.replace(char, '', 1)
            result += 1
    r1 = int(result / len(src) * 100)
    r2 = int(result / len(dst) * 100)
    return '{}'.format(r1 if r1 < r2 else r2)

def debilism(coll):
	col = coll.copy()
	for i in range(len(col)):
		col[i]=col[i].replace(' ', '')
	index = []
	new_col = []
	for i in range(len(col)):
		if col[i] not in new_col:
			new_col.append(col[i])
		else:
			index.append(i)
	
	for i in sorted(index, reverse=True):
		del coll[i]
	return coll

def analysis(inf):
	collection_aut = []
	collection_jour = []
	collection_art = []
	collection_year = []
	collection_index = []
	for i in range(len(inf)):
		if inf[i] == "Title":
			collection_art.append(inf[i+1])
			collection_index.append(inf[i+1])
		if (inf[i] == "Journal" or inf[i] == "Publisher"):
			collection_jour.append(inf[i+1])
			collection_index.append(inf[i+1])		
		if inf[i] == "Author":
			collection_aut.append(inf[i+1])
			collection_index.append(inf[i+1])
		if inf[i] == "Year":
			collection_year.append(inf[i+1])
	collection_aut = debilism(collection_aut)
	collection_jour = debilism(collection_jour)
	collection_art = debilism(collection_art)
	aut(collection_aut)
	jour(collection_jour)
	art(collection_art, collection_year)
	lin(collection_index)

def id():
	id_art = []
	id_jour = []
	id_aut = []
	quare = """SELECT id FROM article"""
	for i in sql.execute(quare):
		id_art.append(i[0])
	quare = """SELECT id FROM author"""
	for i in sql.execute(quare):
		id_aut.append(i[0])
	quare = """SELECT id FROM journal"""
	for i in sql.execute(quare):
		id_jour.append(i[0])
	return id_art, id_jour, id_aut

def inform():
	inf_art = []
	inf_jour = []
	inf_aut = []
	quare = """SELECT name FROM article"""
	for i in sql.execute(quare):
		inf_art.append(i[0])
	quare = """SELECT name FROM author"""
	for i in sql.execute(quare):
		inf_aut.append(i[0])
	quare = """SELECT name FROM journal"""
	for i in sql.execute(quare):
		inf_jour.append(i[0])
	return inf_art, inf_jour, inf_aut		

def lin(inf):
	id_art, id_jour, id_aut = id()
	inf_art, inf_jour, inf_aut = inform()
	link_ar = [] 
	for i in range(len(inf)):
		for r in range(len(inf_art)):
			if inf[i] == inf_art[r]:
				link_ar.append(r)
				y = 0
				while int(search_partial_text(inf[i+2], inf_jour[y])) <= 90:
					if y == len(inf_jour):
						link_ar.append(9999)
						break 
					else:
						y += 1
				if y != len(inf_jour):
					link_ar.append(y)				

				u = 0
				while int(search_partial_text(inf[i+1], inf_aut[u])) <= 90:
					if u == len(inf_aut):
						link_ar.append(9999)
						break 
					else:
						u += 1
				if u != len(inf_aut):
					link_ar.append(u)	
	for i in range(0, len(link_ar), 3):
		link_arr = link_ar[i:i +3]
		quare = """INSERT INTO link VALUES(?, ?, ?) """
		a = link_arr[0] + 1
		b = link_arr[1] + 1
		d = link_arr[2] + 1
		data_quare = (a, b, d)
		sql.execute(quare, data_quare)
		
def aut(collection_aut):
	count = 1
	for i in collection_aut:
		quare = """ INSERT INTO author VALUES(?, ?)"""
		data_quare = (count, i)
		sql.execute(quare, data_quare)
		count = count + 1

def jour(collection_jour):
	count = 1
	for i in collection_jour:
		quare = """ INSERT INTO journal VALUES(?, ?)"""
		data_quare = (count, i)
		sql.execute(quare, data_quare)
		count = count + 1

def art(collection_art, collection_year):
	count = 1
	for i in range(len(collection_art)):
		quare = """ INSERT INTO article VALUES(?, ?, ?)"""
		data_quare = (count, collection_art[i], collection_year[i])
		sql.execute(quare, data_quare)
		count = count + 1

def req():
	res = []
	aut = input("Введите автора: ")
	if(aut[-1]=="."):
		aut=aut[:-1]
	year = input("Введите год: ")
	jour = input("Введите журнал: ")
	if(jour[-1]=="."):
		jour=jour[:-1]
	quare = """SELECT id FROM author WHERE name = ? """
	data_quare = (aut, )
	sql.execute(quare, data_quare)
	a = sql.fetchone()[0]

	quare = """SELECT id FROM journal WHERE name = ? """
	data_quar = (jour, )
	sql.execute(quare, data_quar)
	j = sql.fetchone()[0]

	quare = """SELECT article FROM link WHERE journal = ? AND author = ? """
	data_qua = (j, a, )
	sql.execute(quare, data_qua)
	ar = sql.fetchall()

	print("Названия: ")
	for i in ar:
		quare = """SELECT name FROM article WHERE id = ? AND year = ? """
		data_qu = (i[0], year, )
		sql.execute(quare, data_qu)
		r = sql.fetchone()[0]
		print(r)


	
inf = from_file()
db = sqlite3.connect('server.db')
sql = db.cursor()
create_bd()
analysis(inf)
#req()
db.commit()
db.close()



