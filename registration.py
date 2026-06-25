import os
import pyautogui as pg
import time
import random
import json
from io import UnsupportedOperation
from data import achievements, duel

hello = "Добро пожаловать"
est = False

login_for_enter = ""
pass_for_enter = ""

close_registr = False

last_user_really = False


files = os.listdir(os.getcwd())
if "last_user.json" not in files:
    with open("last_user.json", "w") as file:
        file.write("{}")


with open("last_user.json", "r") as file:
    last_user = json.load(file)

    if last_user:
        last_user_really = True


def enter():
    global est
    global login_for_enter
    global pass_for_enter

    login = pg.prompt("Введите логин:")
    password = pg.prompt("Введите пароль:")

    files = os.listdir(os.getcwd())
    if "players.json" not in files:
        with open("players.json", "w") as file:
            file.write("{}")

    if "last_user.json" not in files:
        with open("last_user.json", "w") as file:
            file.write("{}")

    with open("players.json", "r") as file:
        players = json.load(file)
        if login in players.keys() and players[login]["password"] == str(password):
            est = True
    if est:
        pg.alert(hello + "\nВы успешно авторизовались!", "Программа", button="Продолжить")
        login_for_enter = login
        pass_for_enter = password

        last_user_info = {
            "login": login,
            "password": password
        }

        with open("last_user.json", "w") as file:
            json.dump(last_user_info, file)

    else:
        pg.alert("Такого аккаунта не существует!\nПовторите попытку!", "Программа", button="ОК")


def security_test(parolchik):
    vopros = pg.confirm("Хотите узнать сколько времени понадобится чтобы взломать ваш пароль?", "Программа", ("Да", "Нет"))
    if vopros == "Да":
        pg.alert("", "Программа", "Начать тест")
        start = time.time()

        otgadka = []
        for i in range(len(parolchik)):
            sym = random.choice(chars)
            while sym != parolchik[i]:
                sym = random.choice(chars)
            otgadka.append(sym)
        end = time.time()
        vremya = end - start
        pg.alert("Время за которое удалось взломать ваш пароль:\n" + str(vremya), "Программа", button="Выход")


chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZабвгдеёжзийклмнопрстуфхцчшщъыьэюяАБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ0123456789!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

if last_user_really:
    choice = pg.confirm("Здравствуйте!\nЧто вы хотели бы сделать?", "Программа", ("Зарегистрироваться", "Войти", "Продолжить"))
else:
    choice = pg.confirm("Здравствуйте!\nЧто вы хотели бы сделать?", "Программа", ("Зарегистрироваться", "Войти"))

if choice == "Войти":
    while est is False:
        enter()
elif choice == "Зарегистрироваться":
    login = pg.prompt("Введите логин:")
    while " " in login:
        login = pg.prompt("Логин не может содержать пробелов!\nПовторите попытку!")
    while len(login) < 4:
        login = pg.prompt("Длина логина не может быть менее 4 символов!\nПовторите попытку!")
    while len(login) > 10:
        login = pg.prompt("Длина логина не может превышать 10 символов!\nПовторите попытку!")

    avtomatom = pg.confirm("Желаете создать надёжный пароль автоматически или придумать его сами?", "Программа", ("Автоматически", "Я сам"))
    if avtomatom == "Автоматически":
        parol = random.choice(chars[:25])
        parol += random.choice(chars[26:51])
        parol += random.choice(chars[52:84])
        parol += random.choice(chars[85:117])
        parol += random.choice(chars[118:127])
        parol += random.choice(chars[128:])
        parol += random.choice(chars[52:84])
        parol += random.choice(chars[85:117])
        parol += random.choice(chars[26:51])
        parol += random.choice(chars[128:])
        pg.prompt("Ваш пароль:", "Программа", default=parol)
        data[os.getlogin()] = (login, parol)
    else:
        password = pg.prompt("Введите пароль:")

        while " " in password:
            password = pg.prompt("Пароль не может содержать пробелов!\nПовторите попытку!")
        while len(password) < 4:
            password = pg.prompt("Длина пароля не может быть менее 4 символов!\nПовторите попытку!")
        while len(password) > 10:
            password = pg.prompt("Длина пароля не может превышать 10 символов!\nПовторите попытку!")

        repeat = pg.prompt("Повторите пароль:")

        files = os.listdir(os.getcwd())
        if "players.json" not in files:
            with open("players.json", "w") as file:
                file.write("{}")

        if password == repeat:
            with open("players.json", "r") as file:
                players = json.load(file)
                if login not in players.keys():
                    pg.alert(hello + "\nВы успешно зарегистрировались!", "Программа", button="Продолжить")
                else:
                    pg.alert("\nАккаунт уже существует!", "Программа", button="Продолжить")
                    close_registr = True
        else:
            with open("players.json", "r") as file:
                players = json.load(file)
                while repeat != password:
                    repeat = pg.prompt("Пароли не совпадают!")
                if login not in players.keys():
                    pg.alert(hello + "\nВы успешно зарегистрировались!", "Программа", button="Продолжить")
                else:
                    pg.alert("\nАккаунт уже существует!", "Программа", button="Продолжить")
                    close_registr = True

        if not close_registr:
            login_for_enter = login
            pass_for_enter = password

            files = os.listdir(os.getcwd())
            if "players.json" not in files:
                with open("players.json", "w") as file:
                    file.write("{}")

            with open("players.json", "r") as file:
                players = json.load(file)

            players[login] = {

                "password": password,
                "best_win_monster": "0",
                "count_kill_monster": "0",
                "count_death": "0",
                "coins": "0",

                "duel": duel,
                "achievements": achievements,

                "inventory": {}
            }

            with open("players.json", "w") as file:
                json.dump(players, file)

elif choice == "Продолжить":
    try:
        with open("last_user.json", "r") as file:
            last_user = json.load(file)

            if last_user:
                login_for_enter = last_user["login"]
                pass_for_enter = last_user["password"]
                est = True

    except UnsupportedOperation:
        pass

    except FileNotFoundError:
        pass
