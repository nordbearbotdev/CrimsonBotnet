from .color import color

try:
    import pyfiglet
except ImportError:
    print(
        f"{color.RED}[-] Пожалуйста, установите модуль pyfiglet{color.RESET_ALL}. Пропишите в консоли: pip install pyfiglet"
    )
    quit()


def banner(text: str) -> str:
    banner = pyfiglet.figlet_format(text, font="slant")
    return print(banner)
