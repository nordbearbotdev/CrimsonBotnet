from rich.console import Console
import sys

from settings.settings import MenuSettings
from settings.settings_session import SessionsRead

console = Console()

session_list = SessionsRead()
list_function = MenuSettings()

console.print('''[bold]
GitHub: https://github.com/CrimsonCoalition
Author's channel: 
Version: v.0.1.''')


def botnet_main():

    menu_function={}

    console.print(f'[bold white]botnet accounts >> {len(session_list.sessions)}')
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
                classes(session_list.sessions)

    except KeyboardInterrupt:
        console.print('\n[blue]<https://github.com/CrimsonCoalition>[/]')
        sys.exit()

    except:
        botnet_main()

botnet_main()
