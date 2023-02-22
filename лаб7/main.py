from selenium import webdriver
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def find_all_indexes(input_str, search_str): 
	l1 = [] 
	length = len(input_str) 
	index = 0 
	while index < length: 
		i = input_str.find(search_str, index) 
		if i == -1: 
			return l1 
		l1.append(i) 
		index = i + 1 
	return l1


def title(html):
	p = '</h3>'
	indexes = find_all_indexes(html, p)
	t = ""
	ty=[]
	
	for i in indexes:
		booll = 1
		while booll:
			if html[i] != '>':
				i = i - 1
				t+=(html[i])

			else:
				booll = 0
				t = t[::-1]
				t = t.replace('>', '', 1)
				ty.append(t)
				t = ""
				
	del ty[-1]
	return(ty)

def price(html):
	p = 'itemprop="price" content="'
	indexes = find_all_indexes(html, p)
	t = ""
	ty=[]
	for i in indexes:
		booll = 1
		i +=26
		while booll:
			if html[i] != '"':
				t +=(html[i])
				i+=1
			else:
				booll = 0
				ty.append(t)
				t = ""
	return(ty)

def text(html):
	p = 'iva-item-text-Ge6dR iva-item-description-FDgK4 text-text-LurtD text-size-s-BxGpL">'
	indexes = find_all_indexes(html, p)
	t = ""
	ty=[]
	for i in indexes:
		booll = 1
		i += 82
		while booll:
			if html[i] != "<":
				t+=(html[i])
				i+=1
			else:
				booll = 0
				ty.append(t)
				t = ""
	return(ty)




value = "Ноутбук"
pag = [1, 2, 3]
driver = webdriver.Chrome()
try:
	driver.get('https://avito.ru')
	form_word = driver.find_element(By.ID,"downshift-input")
	form_word.clear()
	form_word.send_keys(value)
	form_word.send_keys(Keys.ENTER)
	with open('result.txt', "a", encoding='utf-8') as file:
		for i in pag:
			print("страница")
			source = driver.page_source
			titl = title(source)
			pric = price(source)
			tex = text(source)
			file.write(str(i) + " страница" + "\n")
			for i in range(len(titl)):
				file.write("//"+titl[i]+". Цена: " + pric[i] + " Руб.//\n" + tex[i] + "\n" + "\n")
			(driver.find_element(By.XPATH, "//span[@data-marker='pagination-button/next'][contains(.,'След. →')]")).click()
	time.sleep(5)

except Exception as ex:
	print(ex)
finally:
	driver.close()
	driver.quit()
