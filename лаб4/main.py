import vk_api, json
import requests

my_token = ''
vk = vk_api.VkApi(token= my_token)

user = vk.method("users.get", {"user_ids": 1})#получаем имя у id1 
one_name = user[0]['first_name']



vk1=vk.get_api()
friendss = []

with vk_api.VkRequestsPool(vk) as pool:
    friends = pool.method('friends.get')

res = vk1.users.get(user_id=friends.result['items'])#получаем идентификаторы друзей, а после получаем информацию о них
for t in res:#берем ФИ человека и записываем в массив
	friendss.append(str(t['last_name'] +  " " + t['first_name']) + " ")


friendss.sort()#сортируем по алфавиту
st = ""
for i in range(len(friendss)):
	st += friendss[i] + "\n"

mess ="Имя пользователя id1 - " + one_name + "\n" + "\n" + "Список друзей: \n" + st
vk1.wall.post(message = mess)#создаем пост на стене

