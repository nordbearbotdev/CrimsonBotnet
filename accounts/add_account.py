import string
import discord
from rich.prompt import Prompt, Confirm
import os
import random
from rich.console import Console
import glob

console = Console()

menu_sessions_settings = console.input('''[bold white]
[1] - add account
[2] - checking accounts for validity
>> ''')

