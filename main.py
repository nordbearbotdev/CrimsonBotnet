""" Devoloped by Crimson Coalition """

import functions as s
from functions import color

s.banner(text="Crimson Inc.")

# print(colored( '''
print('''
            
                                         
Crimson never die. Crimson never down.                     

GitHub: https://github.com/CrimsonCoalition
Author's channel: https://t.me/CrimsonCoalition/
Crimson Discord Botnet Version: v.0.1.


[1] Отправка запросов в друзья
[2] Вход в конфу
[3] Выход из конфы
[4] Отправка сообщений
[5] Показать хелп-лист.
[6] История
[7] Выйти
''')
# ''','magenta'))


while True:
	_input = str(input(f"{color.YELLOW}[?] > {color.RESET_ALL}").lower())

	if _input == "1":
		userid = input(f"{color.YELLOW}[?] Введите ID Пользователя, Которому Надо Отправить Запрос В Друзья > {color.RESET_ALL}").lower()
		for tokens in s.tokens():
			s.friend_request(token = tokens , userid = userid , userAgent = s.userAgent() , proxies = s.proxies())
		print(f"{color.GREEN}Операция Закончена. {color.RESET_ALL}")

	elif _input == "2":
		guildid = input(f"{color.YELLOW}[?] Введите ID Сервера, На Который Надо Войти > {color.RESET_ALL}").lower()
		for tokens in s.tokens():
			s.join_guild(token = tokens , guildid = guildid , userAgent = s.userAgent() , proxies = s.proxies())
		print(f"{color.GREEN}Операция Закончена. {color.RESET_ALL}")


	elif _input == "3":
		guildid = input(f"{color.YELLOW}[?] Введите ID Сервера, С Которого Надо Выйти > {color.RESET_ALL}").lower()
		for tokens in s.tokens():
			s.leave_guild(token = tokens , guildid=guildid , userAgent=s.userAgent() , proxies=s.proxies())
		print(f"{color.GREEN}Операция Закончена. {color.RESET_ALL}")


	elif _input == "4":
		channelid = input(f"{color.YELLOW}[?] Введите ID Канала, На который Надо Отпрвавить Сообщение > {color.RESET_ALL}").lower()
		message = input(f"{color.YELLOW}[?] Введите Сообщение > {color.RESET_ALL}").lower()
		for tokens in s.tokens():
			s.send_message(token = tokens , channelid = channelid , message = message , userAgent = s.userAgent() , proxies=s.proxies())
		print(f"{color.GREEN}Операция Закончена. {color.RESET_ALL}")

	elif _input == "5":
		print("Поместите Токены по пути ./files/tokens.txt file.")
		
	elif _input == "6":
		print("")

	elif _input == "7":
		quit()

	else:
		print(f"{color.RED}[-]Неправильная опция. {color.RESET_ALL}")
