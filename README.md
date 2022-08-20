# ***CrimsonBotnet***

> Авторы не несут ответственности за ущерб приченный входе использвания. Данная программа предназначена для тестирования защиты вашего Discord сервера!


![crimson](https://user-images.githubusercontent.com/85753549/185703142-bb72527c-818c-4449-9728-05a3688f0e83.png)


### ***Описание***
***CrimsomBotnet*** - интрумент, который поможет зарейдить Discord беседу или сервер.

### ***Установка***
***Перед установкой проверьте установлены ли у вас Git и Python.***

***1. Склонируйте репозиторий:***

```bash
git clone https://github.com/CrimsonCoalition/CrimsonBotnet/
```

***2. Перейдите в папку с CrimsonBotnet:***

```bash
cd CrimsonBotnet
```
***Установите недостающие модули:***
```bash
pip install requirements.txt # pip3 если у вас MacOS X или Linux 
```

### ***Добавление аккаунтов***

```bash
cd accounts
python add_account.py # либо python3 add_account.py если вы сидите с Linux.
```

***После чего вы увидете следующее***

![Screenshot_33](https://user-images.githubusercontent.com/85753549/185092178-07460436-5b70-491a-8791-83f9d1430f2d.png)

- [1] Добавление аккаунта
- [2] Проверка на валид (проверяет токен аккаунта на работоспособность)

### ***Работа с конфигом***

```bash
cd settings # Переходим в папку с настройками
nano config.py # Открываем и редактируем конфиг с помощью nano.
```
### ***Запуск атаки***
```bash
python main.py
```
