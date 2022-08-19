import requests
from .assetsManager import *
from .color import color

def send_message(token : str , channelid : str , message : str , userAgent: str , proxies : str) -> str:
	
	headers = {"content-type": "application/json",	"authorization": token , "User-Agent" : userAgent , "content" : message , "tts" : "false"}
	proxies = {"http" : proxies}
	try:
		x = requests.post(f"https://discordapp.com/api/v7/channels/{channelid}/messages" , headers=headers , proxies=proxies)
	except Exception as err:
		print(f"{color.RED}[-] ОШИБКА: {color.RESET_ALL} {err}")
	if x.status_code == 200:
		print(f"{color.GREEN}[+] Сообщение отправлено успешно!. {color.RESET_ALL}")
	else:
		print(f"{color.RED}[-] Сообщение не было отправлено. {color.RESET_ALL} {x.json()}")
