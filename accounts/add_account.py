import string
import discord
from rich.prompt import Prompt, Confirm
import os
import random
from rich.console import Console
import glob

console = Console()

menu_sessions_settings = console.input(colored( '''



   _____      _                             _____              
  / ____|    (_)                           |_   _|             
 | |     _ __ _ _ __ ___  ___  ___  _ __     | |  _ __   ___   
 | |    | '__| | '_ ` _ \/ __|/ _ \| '_ \    | | | '_ \ / __|  
 | |____| |  | | | | | | \__ \ (_) | | | |  _| |_| | | | (__ _ 
  \_____|_|  |_|_| |_| |_|___/\___/|_| |_| |_____|_| |_|\___(_)
                                                               
                                                                                                            
                                by Crimson Coalition                                                               


[1] - Добавить токен.
[2] - Проверить токены на валидность.
>> 

''','magenta'))

