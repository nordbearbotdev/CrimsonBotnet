from rich.console import Console
import sys

from settings.settings import MenuSettings
from accounts.settings_account import AccountsRead

console = Console()

account_list = AccountsRead()
list_function = MenuSettings()

console.print('''[bold]


   _____      _                             _____              
  / ____|    (_)                           |_   _|             
 | |     _ __ _ _ __ ___  ___  ___  _ __     | |  _ __   ___   
 | |    | '__| | '_ ` _ \/ __|/ _ \| '_ \    | | | '_ \ / __|  
 | |____| |  | | | | | | \__ \ (_) | | | |  _| |_| | | | (__ _ 
  \_____|_|  |_|_| |_| |_|___/\___/|_| |_| |_____|_| |_|\___(_)
                                                               
                                          Crimson never die. Crimson never down.                     

GitHub: https://github.com/CrimsonCoalition
Author's channel: 
BadCord Version: v.0.1.''')


def botnet_main():

    menu_function={}

    console.print(f'[bold white]Кол-во ботнет аккаунтов: >> {len(account_list.accounts)}')
    for num_function, function in enumerate(
            list_function.menu_botnet,
            start=1
        ):

        menu_function[num_function]=function
        console.print(f'[bold white][{num_function}] {function.__doc__}')

    try:
        menu = int(console.input('>> '))

        for num, classes in menu_function.items():
            if num == menu:
                classes(account_list.accounts)

    except KeyboardInterrupt:
        console.print('\n[blue]<https://github.com/CrimsonCoalition>[/]')
        sys.exit()

    except:
        botnet_main()

botnet_main()
