import requests
from .assetsManager import *
from .color import color

def friend_request(token : str , userid : str , userAgent: str , proxies : str) -> str:

	headers = {"content-type": "application/json",	"authorization": token , "User-Agent" : userAgent}
	proxies = {"http" : proxies}
	try:
		x = requests.put(f"https://discordapp.com/api/v7/users/@me/relationships/{userid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(f"{color.RED}[-] ОШИБКА: {color.RESET_ALL} {err}")
	if x.status_code == 204:
		print(f"{color.GREEN}[+] Запрос в друзьях успешно отправлен. {color.RESET_ALL}")
	else:
		print(f"{color.RED}[-] Не получилось отправить запрос в друзья {color.RESET_ALL} {x.json()}")
