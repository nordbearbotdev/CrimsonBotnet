import requests
from .assetsManager import *
from .color import color

def leave_guild(token : str , guildid : str , userAgent: str , proxies : str) -> str:

	headers = {"content-type": "false",	"authorization": token , "User-Agent" : userAgent}
	proxies = {"http" : proxies}
	try:
		x = requests.delete(f"https://discordapp.com/api/v7/invite/{guildid}" , headers=headers , proxies=proxies)
	except Exception as err:
		print(f"{color.RED}[-] ERROR: {color.RESET_ALL} {err}")
	if x.status_code == 204:
		print(f"{color.GREEN}[+] Успешно вышли с сервера. {color.RESET_ALL}")
	else:
		print(f"{color.RED}[-] Не получилось выйти с сервера. {color.RESET_ALL} {x.json()}")
