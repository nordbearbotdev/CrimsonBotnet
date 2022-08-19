import requests
from .assetsManager import *
from .color import color

def join_guild(token : str , guildid : str , userAgent: str , proxies : str) -> str:

	headers = {"content-type": "false",	"authorization": token , "User-Agent" : userAgent}
	proxies = {"http" : proxies}
	try:
		x = requests.post(f"https://discordapp.com/api/v7/invite/{guildid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(f"{color.RED}[-] ERROR: {color.RESET_ALL} {err}")
	if x.status_code == 204:
		print(f"{color.GREEN}[+] Успешное присоединение к серверу. {color.RESET_ALL}")
	else:
		print(f"{color.RED}[-] Не получилось присоединится к серверу. {color.RESET_ALL} {x.json()}")
