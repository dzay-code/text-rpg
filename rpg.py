from random import *
from time import sleep
import keyboard as kb
import pyautogui as pg
import time
from data import monsters, monsters_w, items, duel, angl_words, russ_words, weather_effects
import json
import registration
import math

words = False
nums = False
lets = False
escape = False
offic_level = 0
offic_syms = ""
symbols = None
buff_krit = False
buff_time = False
debuff_krit = False
krit = 10
evasion_hero = 10
evasion_monster = 10
use_escape = False
win = False
player_hp = 100
right = 0
time_for_rage = 0
camp_krit = False
camp_evasion = False


lich = False
lich_heart = False

destroyer = False
halberd = False

devourer = False
hunger = False

berserk = False

vasilisk = False
vasilisk_orb = False

faceless = False

# для ачивок
use_lich_heart = False
use_halberd = False
use_hunger = False
use_rage_berserk = False
use_vasilisk_orb = False
use_robe = False
# для ачивок

get_rage_berserk = False
get_lich_heart = False
get_hunger = False
get_halberd = False
get_vasilisk_orb = False
get_robe = False


def submodes():
    # подрежимы
    global lets, words, nums
    global monsters
    global symbols

    print("⚙️ Выберите режим:")
    print("1. 🔤 Буквы")
    print("2. 📝 Слова")
    print("3. 🔢 Цифры")

    mode = "/"
    while mode not in "123":
        mode = str(input())
        if mode == "" or len(mode) != 1:
            mode = "/"

    if str(mode) == "1" or str(mode) == "2":
        print("🌐 Выберите язык:")
        print("1. Русский")
        print("2. Английский")

        lang = "/"
        while lang not in "12":
            lang = str(input())
            if lang == "" or len(lang) != 1:
                lang = "/"

    if str(mode) == "1":
        if str(lang) == "1":
            symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
        if str(lang) == "2":
            symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        lets = True

    if str(mode) == "2":

        if str(lang) == "1":
            symbols = russ_words
        if str(lang) == "2":
            symbols = angl_words

        words = True
        monsters = monsters_w

    if str(mode) == "3":
        symbols = "0123456789"
        nums = True

        mode_and_lang = [mode, "nothing"]
        return mode_and_lang

    mode_and_lang = [mode, lang]
    return mode_and_lang


def identify_monster(level):
    # определение монстра
    monster = None
    if level == 1:
        monster = randrange(1, 7)
    elif level == 2:
        monster = randrange(6, 13)
    elif level == 3:
        monster = randrange(12, 19)
    elif level == 4:
        monster = randrange(18, 25)
    elif level == 5:
        monster = randrange(31, 32)
    return monster


def show_combo(combo):
    # показ комбо
    if lets:
        print("🔤 Буквы:", " ".join(combo))
    elif words:
        print("📝 Слова:", " ".join(combo))
    elif nums:
        print("🔢 Цифры:", " ".join(combo))


def use_item():
    # использование предметов инвентаря до битвы
    global lich_heart, hunger, halberd, krit, vasilisk_orb
    global evasion_hero
    global use_lich_heart, use_halberd, use_hunger, use_rage_berserk, use_vasilisk_orb, use_robe

    with open("players.json", "r") as file:
        players = json.load(file)
        if players[registration.login_for_enter]["inventory"]:
            print("🎒 Желаете использовать предмет из инвентаря?")
            print("1. ✅ Открыть инвентарь")
            print("2. ❌ Нет")

            choice_item = "/"
            while choice_item not in "12":
                choice_item = str(input())
                if choice_item == "" or len(choice_item) != 1:
                    choice_item = "/"

            choice_item = str(choice_item)

            i = 0
            if choice_item == "1":
                print("🔢 Выберите номер предмета который хотите использовать.")
                for key in players[registration.login_for_enter]["inventory"]:
                    i += 1
                    print(f"{i}. {list(players[registration.login_for_enter]["inventory"][key].keys())[0]}: {players[registration.login_for_enter]["inventory"][key][list(players[registration.login_for_enter]["inventory"][key].keys())[0]]}")

                print("99. 🔙 Назад")

                need_range = ""
                for i in range(1, len(players[registration.login_for_enter]["inventory"]) + 1):
                    need_range += str(i)

                choice_item = "//"
                while choice_item not in need_range:
                    choice_item = str(input())
                    if choice_item == "99":
                        return
                    if choice_item == "" or len(choice_item) != 1:
                        choice_item = "/"

                choice_item = int(choice_item)

                if list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Lich":
                    if player_hp == 100:
                        print("⚠️ У вас максимальный запас здоровья.")
                        use_item()
                    else:
                        player_hp = 100
                        use_lich_heart = True

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Destroyer":
                    halberd = True
                    use_halberd = True

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Devourer":
                    hunger = True
                    use_hunger = True

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Berserk":
                    krit += 15
                    use_rage_berserk = True

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Vasilisk":
                    vasilisk_orb = True
                    use_vasilisk_orb = True

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Faceless":
                    evasion_hero += 15
                    use_robe = True

                del players[registration.login_for_enter]["inventory"][list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1]]
                with open("players.json", "w") as file:
                    json.dump(players, file)

                print(f"✅ Предмет использован.")


def more_fight(fight, time_for_rage, mode, level_up, buff=False, debuff=False):
    global evasion_monster, player_hp
    global lich, destroyer, devourer, berserk, vasilisk, faceless
    # продолжение похода

    monster = identify_monster(offic_level)

    if not level_up:
        print("Едва вы успели перевести дух после боя, как из темноты появился новый враг.")
        cont()
    else:
        print("Здешние чудовища сильнее прежних. Да начнется бой.")
        cont()

    print(f"Это {monsters[monster]["name"]}.")
    cont()

    # лич
    if monster == 23:
        lich = True
    # лич

    # разрушитель
    if monster == 28:
        destroyer = True
    # разрушитель

    # пожиратель
    if monster == 30:
        devourer = True
    # пожиратель

    # берсерк
    if monster == 6:
        berserk = True
    # берсерк

    # василиск
    if monster == 22:
        vasilisk = True
    # василиск

    # безликий
    if monster == 11:
        faceless = True
        evasion_monster += 30
    # безликий

    if monster in [6, 23, 11]:
        print(f"⚠ {monsters[monster]["text"]}")

    if monster in [23, 28, 30, 6, 22]:
        print("💎 С этого монстра может выпасть предмет.")

    # использование предметов инвентаря до битвы
    use_item()
    # использование предметов инвентаря до битвы

    combo = choices(offic_syms, k=monsters[monster]["letters"])

    # пожиратель
    if hunger or buff != False:
        if str(mode) == "1" or str(mode) == "3":
            combo = combo[:-3]
        elif str(mode) == "2":
            combo = combo[:-1]
    # пожиратель

    if debuff != False:
        if str(mode) == "1" or str(mode) == "3":
            combo.extend(choices(symbols, k=3))

        elif str(mode) == "2":
            combo.extend(choices(symbols, k=1))

    # сердце лича
    if lich_heart:
        player_hp = 100
    # сердце лича

    # разрушитель
    if halberd:
        right = 1
    # разрушитель

    # василиск
    if vasilisk_orb:
        time_for_rage -= 1
    # василиск

    print(f"❤️ HP: {player_hp}/100")
    print("⏱ Выделенное время в секундах:", monsters[monster]["time"] - time_for_rage)
    cont()

    show_combo(combo)

    if buff == True:
        fight(combo, need=monster, buff=True)
    elif debuff == True:
        fight(combo, need=monster, debuff=True)
    else:
        fight(combo, need=monster)


def death():
    global get_rage_berserk, get_lich_heart, get_hunger, get_halberd, get_vasilisk_orb, get_robe
    global win, halberd, hunger

    win = False
    halberd = False
    hunger = False

    print("💀 Вы погибли!")

    with open("players.json", "r") as file:
        players = json.load(file)
        players[registration.login_for_enter]["count_death"] = str(int(players[registration.login_for_enter]["count_death"]) + 1)

        if get_rage_berserk or get_lich_heart or get_hunger or get_halberd or get_vasilisk_orb or get_robe:
            print("⚠️ Все найденные в этом походе артефакты были утеряны.")

        # удаление предметов при смерти
        # лич
        if get_lich_heart:
            del players[registration.login_for_enter]["inventory"]["Lich"]
            get_lich_heart = False
        # лич

        # разрушитель
        if get_halberd:
            del players[registration.login_for_enter]["inventory"]["Destroyer"]
            get_halberd = False
        # разрушитель

        # пожиратель
        if get_hunger:
            del players[registration.login_for_enter]["inventory"]["Devourer"]
            get_hunger = False
        # пожиратель

        # берсерк
        if get_rage_berserk:
            del players[registration.login_for_enter]["inventory"]["Berserk"]
            get_rage_berserk = False

        # берсерк

        # василиск
        if get_vasilisk_orb:
            del players[registration.login_for_enter]["inventory"]["Vasilisk"]
            get_vasilisk_orb = False
        # василиск

        # безликий
        if get_robe:
            del players[registration.login_for_enter]["inventory"]["Faceless"]
            get_robe = False
        # безликий
        # удаление предметов при смерти

    with open("players.json", "w") as file:
        json.dump(players, file)


def cont():
    # нажатие enter для продолжения
    kb.wait("enter")
    pg.press("backspace")


ivents = ["🗺️ Поход", "⚔️ Дуэль вечности", "🧠 Власть чисел", "📊 Статистика", "🎖 Достижения", "⚙️ Настройки"]
levels = ["📖 Ученик", "🩸 Охотник", "⚔️ Элитный каратель", "⛓️️️ Инквизитор", "💀 Немезида"]

print(f"Добро пожаловать в игру!\nИспользуйте 'enter' чтобы продолжить.")
cont()

ivent = ""


def menu():
    # меню
    global ivent
    print()
    print("📋 Меню:")
    for i in range(1, len(ivents) + 1):
        print(str(i) + ". " + ivents[i - 1])
    ivent = "/"
    while ivent not in "123456":
        ivent = str(input())
        if ivent == "" or len(ivent) != 1:
            ivent = "/"


menu()


def main():
    if str(ivent) == "1":
        back = False

        def hike_menu():
            # меню похода
            nonlocal back
            print()
            print("📋 Меню: Поход")
            print("1. ⚔️ Начать поход")
            print("2. 📜 Руководство")
            print("3. 🔙 Назад")

            choice_want_hike = "/"
            while choice_want_hike not in "123":
                choice_want_hike = str(input())
                if choice_want_hike == "" or len(choice_want_hike) != 1:
                    choice_want_hike = "/"

            if choice_want_hike == "1":
                # начать поход
                back = False
            elif choice_want_hike == "2":
                # руководство
                print("Путь охотника начинается здесь.")
                print("Исследуйте опасный мир, бросайте вызов легендарным чудовищам, собирайте могущественные артефакты и пройдите путь от Ученика до Немезиды.")
                print("Но помните: чем глубже вы проникаете в неизведанные земли, тем страшнее становятся их обитатели.")
                hike_menu()
            elif choice_want_hike == "3":
                # назад
                back = True

        hike_menu()

        def hike():
            # поход
            global lets, words, nums
            global offic_level, offic_syms
            global monsters
            global symbols
            global lich_heart, hunger, halberd, vasilisk_orb
            global lich, destroyer, devourer, berserk, vasilisk, faceless
            global buff_krit, buff_time, debuff_krit
            global escape
            global krit, evasion_hero, evasion_monster
            global get_rage_berserk, get_lich_heart, get_hunger, get_halberd, get_vasilisk_orb, get_robe
            global win, right, time_for_rage
            global player_hp, krit, evasion_hero, evasion_monster
            global camp_krit, camp_evasion

            player_hp = 100
            win = False
            escape_fight = False
            sum_win = 0
            level_up = False
            krit = 10
            evasion_hero = 10
            evasion_monster = 10

            right = 0
            rage = False
            time_for_rage = 0
            lets_for_change = False

            # ачивки
            win_berserk = False
            win_beast = False
            win_titan = False
            win_leviathan = False
            win_devourer = False
            # ачивки

            get_rage_berserk = False
            get_lich_heart = False
            get_hunger = False
            get_halberd = False
            get_vasilisk_orb = False
            get_robe = False

            mode, lang = submodes()

            # выбор уровня
            print("Выберите сложность:")
            for i in range(1, len(levels) + 1):
                print(str(i) + ". " + levels[i - 1])

            level = "/"
            while level not in "12345":
                level = str(input())
                if level == "" or len(level) != 1:
                    level = "/"
            level = int(level)

            offic_level = level
            offic_syms = symbols

            sleep(1)
            print("Вы отправились в поход в неизведанный лес, полный опасностей.")
            cont()

            monster = identify_monster(level)

            print("Продвигаясь всё глубже в чащу, вы неожиданно столкнулись с жутким монстром.")
            cont()
            print(f"Это был {monsters[monster]["name"]}.")
            cont()

            # погода
            weather = choice(list(weather_effects.keys()))

            if weather == "🌫️ Туман":
                krit -= 7
                evasion_hero += 7

            elif weather == "☀️ Ясно":
                krit += 7
                evasion_hero -= 7

            elif weather == "💨 Сильный ветер":
                evasion_hero += 15
                evasion_monster += 15

            print(f"Погода: {weather}")
            print(weather_effects[weather])
            # погода

            cont()

            # лич
            if monster == 23:
                lich = True
            # лич

            # разрушитель
            if monster == 28:
                destroyer = True
            # разрушитель

            # пожиратель
            if monster == 30:
                devourer = True
            # пожиратель

            # берсерк
            if monster == 6:
                berserk = True
            # берсерк

            # василиск
            if monster == 22:
                vasilisk = True
            # василиск

            # безликий
            if monster == 11:
                faceless = True
                evasion_monster += 30
            # безликий

            if monster in [6, 23, 11]:
                print(monsters[monster]["text"])

            if monster in [23, 28, 30, 6, 22]:
                print("💎 С этого монстра может выпасть предмет.")

            print("Вы вынуждены сражаться дабы выжить!")
            cont()
            print("Приготовьтесь!")
            cont()

            if lets:
                print("Введите указанную комбинацию клавиш вовремя, иначе получите урон.")
            elif words:
                print("Введите указанные слова вовремя, иначе получите урон.")
            elif nums:
                print("Введите указанную комбинацию цифр вовремя, иначе получите урон.")

            cont()

            # использование предметов инвентаря до битвы
            use_item()
            # использование предметов инвентаря до битвы

            combo = choices(symbols, k=monsters[monster]["letters"])

            # пожиратель
            if hunger:
                if str(mode) == "1" or str(mode) == "3":
                    combo = combo[:-3]
                elif str(mode) == "2":
                    combo = combo[:-1]
            # пожиратель

            # разрушитель
            if halberd:
                right = 1
            # разрушитель

            # василиск
            if vasilisk_orb:
                time_for_rage -= 1
                vasilisk_orb = False
            # василиск

            print(f"❤️ HP: {player_hp}/100")
            print("⏱ Выделенное время в секундах:", monsters[monster]["time"] - time_for_rage)
            cont()
            show_combo(combo)

            def fight(arg, need="nothing", buff=False, debuff=False):
                global win, right, time_for_rage
                nonlocal rage, monster
                global escape
                global lich_heart, berserk, hunger, halberd, lich, destroyer, devourer, vasilisk_orb, vasilisk, faceless
                nonlocal mode, lang
                global symbols, lets, words, nums, monsters
                global debuff_krit
                nonlocal sum_win
                global evasion_hero, evasion_monster
                nonlocal win_berserk, win_beast, win_titan, win_leviathan, win_devourer
                global use_escape
                global get_rage_berserk, get_lich_heart, get_hunger, get_halberd, get_vasilisk_orb, get_rob
                global player_hp
                nonlocal lets_for_change

                if need != "nothing":
                    monster = need

                combo = arg
                change_regime = False
                monster_dodged = False
                hero_dodged = False
                time_for_compare = monsters[monster]["time"]

                start = time.time()

                input_combo = input()

                end = time.time()

                if "".join(input_combo.lower().split()) == "".join(combo).lower() and (end - start) <= time_for_compare - time_for_rage:
                    # крит и засчитывание удара и уклонение
                    if randrange(1, 101) <= evasion_monster:
                        print("❌ Монстр уклонился!")
                        monster_dodged = True
                    else:
                        if randrange(1, 101) <= krit:
                            print("💥 Критический удар!")
                            right += 2
                        else:
                            right += 1

                    if right >= monsters[monster]["combos"]:
                        # победа
                        print("✅ Вы победили!")
                        sum_win += 1
                        win = True
                        if halberd:
                            right = 1
                        else:
                            right = 0
                        time_for_rage = 0

                        # награда(монеты)
                        with open("players.json", "r") as file:
                            players = json.load(file)
                            if monster in range(1, 11):
                                coins = choice(range(5, 11))
                                players[registration.login_for_enter]["coins"] = str(int(players[registration.login_for_enter]["coins"]) + coins)
                            elif monster in range(11, 21):
                                coins = choice(range(10, 21))
                                players[registration.login_for_enter]["coins"] = str(int(players[registration.login_for_enter]["coins"]) + coins)
                            elif monster in range(21, 32):
                                coins = choice(range(15, 26))
                                players[registration.login_for_enter]["coins"] = str(int(players[registration.login_for_enter]["coins"]) + coins)

                            print(f"+{coins} 🪙")

                            # награда(предметы)
                            # лич
                            if lich:
                                print("🎁 Бессмертный лич повержен. Вы получаете Сердце лича.")
                                players[registration.login_for_enter]["inventory"]["Lich"] = {"Сердце лича": items["Сердце лича"]}
                                lich = False
                                get_lich_heart = True
                            # лич

                            # разрушитель
                            if destroyer:
                                print("🎁 Разрушитель небес повержен. Вы получаете Алебарда Разрушителя.")
                                players[registration.login_for_enter]["inventory"]["Destroyer"] = {"Алебарда Разрушителя": items["Алебарда Разрушителя"]}
                                destroyer = False
                                get_halberd = True
                            # разрушитель

                            # пожиратель
                            if devourer:
                                print("🎁 Пожиратель миров повержен. Вы получаете Голод Бездны.")
                                players[registration.login_for_enter]["inventory"]["Devourer"] = {"Голод Бездны": items["Голод Бездны"]}
                                devourer = False
                                get_hunger = True
                            # пожиратель

                            # берсерк
                            if berserk:
                                if randrange(1, 5) == 1:
                                    print("🎁 Берсерк повержен. Вы получаете Ярость берсерка.")
                                    players[registration.login_for_enter]["inventory"]["Berserk"] = {"Ярость берсерка": items["Ярость берсерка"]}
                                    get_rage_berserk = True
                                berserk = False
                            # берсерк

                            # василиск
                            if vasilisk:
                                print("🎁 Изначальный Василиск повержен. Вы получаете Око Василиска.")
                                players[registration.login_for_enter]["inventory"]["Vasilisk"] = {"Око Василиска": items["Око Василиска"]}
                                vasilisk = False
                                get_vasilisk_orb = True
                            # василиск

                            # безликий
                            if faceless:
                                if randrange(1, 5) == 1:
                                    print("🎁 Безликий повержен. Вы получаете Одеяние Безликого.")
                                    players[registration.login_for_enter]["inventory"]["Faceless"] = {"Одеяние Безликого": items["Одеяние Безликого"]}
                                    get_robe = True
                                faceless = False
                                evasion_monster -= 30
                            # безликий

                            # ачивки
                            if monster == 6:
                                win_berserk = True
                            elif monster == 12:
                                win_beast = True
                            elif monster == 18:
                                win_titan = True
                            elif monster == 24:
                                win_leviathan = True
                            elif monster == 30:
                                win_devourer = True
                            # ачивки

                            if monster > int(players[registration.login_for_enter]["best_win_monster"].split()[0]):
                                players[registration.login_for_enter]["best_win_monster"] = str(monster) + " " + monsters[monster]["name"]

                            players[registration.login_for_enter]["count_kill_monster"] = str(int(players[registration.login_for_enter]["count_kill_monster"]) + 1)

                        with open("players.json", "w") as file:
                            json.dump(players, file)

                        return "win"

                    else:
                        # ранение монстра
                        if not monster_dodged:
                            print("✅ Вы успешно ранили монстра")
                            cont()
                            if right + 1 == monsters[monster]["combos"]:
                                # ярость
                                if not berserk:
                                    # обычный монстр
                                    if randrange(1, 101) <= 30:
                                        print("⚡ Монстр в бешенстве!")
                                        print("⌛ Время уменьшено!")
                                        rage = True
                                        time_for_rage += 1
                                        need = time_for_compare - time_for_rage
                                        print("⏱ Выделенное время в секундах:", need)
                                else:
                                    # берсерк
                                    if randrange(1, 101) <= 50:
                                        print("⚡ Берсерк в ярости!")
                                        print("⌛ Время уменьшено!")
                                        rage = True
                                        time_for_rage += 1
                                        need = time_for_compare - time_for_rage
                                        print("⏱ Выделенное время в секундах:", need)

                                cont()

                        # разраб
                        if monster == 31:
                            if randrange(1, 3) == 1:
                                change_regime = True
                                print("⚠️ Апостол разработчика изменяет правила испытания.")

                                available_modes = ["russ_lets", "angl_lets", "russ_words", "angl_words", "nums"]

                                # отбор доступных режимов
                                if str(mode) == "1":
                                    if str(lang) == "1":
                                        del available_modes[0]

                                    if str(lang) == "2":
                                        del available_modes[1]

                                    lets = True

                                if str(mode) == "2":

                                    if str(lang) == "1":
                                        del available_modes[2]

                                    if str(lang) == "2":
                                        del available_modes[3]

                                if str(mode) == "3":

                                    del available_modes[4]

                                # отбор доступных режимов

                                change_mode = choice(available_modes)

                                if change_mode == "russ_lets":
                                    print("Следующий режим: Русские буквы.")
                                    symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                    lets = True

                                if change_mode == "angl_lets":
                                    print("Следующий режим: Английские буквы.")
                                    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                    lets = True

                                if change_mode == "russ_words":
                                    print("Следующий режим: Русские слова.")
                                    symbols = russ_words
                                    words = True
                                    monsters = monsters_w

                                if change_mode == "angl_words":
                                    print("Следующий режим: Английские слова.")
                                    symbols = angl_words
                                    words = True
                                    monsters = monsters_w

                                if change_mode == "nums":
                                    print("Следующий режим: Цифры.")
                                    symbols = "0123456789"
                                    nums = True

                                cont()

                                if change_mode in ["russ_words", "angl_words"]:
                                    combo = choices(symbols, k=monsters[monster]["letters"])
                                    time_for_compare = monsters_w[monster]["time"]
                                else:
                                    combo = choices(symbols, k=monsters[monster]["lets_for_change"])
                                    time_for_compare = monsters[monster]["time_for_change"]
                                    lets_for_change = True

                                print("⏱ Выделенное время в секундах:", time_for_compare)
                            # разраб

                        if monster != 31 or not change_regime:
                            combo = choices(symbols, k=monsters[monster]["letters"])

                        # пожиратель
                        if hunger or buff == True:
                            if str(mode) == "1" or str(mode) == "3":
                                combo = combo[:-3]
                            elif str(mode) == "2":
                                combo = combo[:-1]
                        # пожиратель

                        if debuff == True:

                            if str(mode) == "1" or str(mode) == "3":
                                combo.extend(choices(symbols, k=3))

                            elif str(mode) == "2":
                                combo.extend(choices(symbols, k=1))

                        show_combo(combo)

                        cont()

                        if buff:
                            fight(combo, buff=True)
                        if debuff:
                            fight(combo, debuff=True)
                        if not buff and not debuff:
                            fight(combo)
                else:
                    # неверный ответ
                    if randrange(1, 101) <= evasion_hero:
                        print("🛡️ Вы уклонились!")
                        hero_dodged = True
                        cont()

                    if not hero_dodged:
                        if escape_fight:

                            death()

                            return "lose"

                        if "".join(input_combo.lower().split()) != "".join(combo).lower():
                            print("❌ Неверный ответ")
                        elif (end - start) > monsters[monster]["time"]:
                            print("⌛ Вы превысили допустимое время")

                        min_damage, max_damage = [int(el) for el in monsters[monster]["damage"].split("-")]
                        damage = choice(range(min_damage, max_damage + 1))

                        if player_hp - damage > 0:
                            # ранение
                            player_hp -= damage
                            print("💔 Вас ранили!")
                            cont()

                            print(f"❤️ HP: {player_hp}/100")

                            print("Сосредоточьтесь!")
                            cont()

                            if lets_for_change:
                                combo = choices(symbols, k=monsters[monster]["lets_for_change"])
                            else:
                                combo = choices(symbols, k=monsters[monster]["letters"])

                            # пожиратель
                            if hunger or buff == True:
                                if str(mode) == "1" or str(mode) == "3":
                                    combo = combo[:-3]
                                elif str(mode) == "2":
                                    combo = combo[:-1]
                            # пожиратель

                            if debuff == True:
                                if str(mode) == "1" or str(mode) == "3":
                                    combo.extend(choices(symbols, k=3))

                                elif str(mode) == "2":
                                    combo.extend(choices(symbols, k=1))

                            show_combo(combo)

                            if buff:
                                fight(combo, buff=True)
                            if debuff:
                                fight(combo, debuff=True)
                            if not buff and not debuff:
                                fight(combo)
                        else:
                            if randrange(1, 11) == 1:
                                # бегство
                                print("🏃‍♂️ В последний момент вы вырвались из боя и спаслись бегством.")
                                right = 0
                                escape = True
                                use_escape = True
                                return "escape"
                            else:
                                # смерть

                                death()

                                return "lose"
                    else:
                        combo = choices(symbols, k=monsters[monster]["letters"])

                        # пожиратель
                        if hunger or buff == True:
                            if str(mode) == "1" or str(mode) == "3":
                                combo = combo[:-3]
                            elif str(mode) == "2":
                                combo = combo[:-1]
                        # пожиратель

                        if debuff == True:
                            if str(mode) == "1" or str(mode) == "3":
                                combo.extend(choices(symbols, k=3))

                            elif str(mode) == "2":
                                combo.extend(choices(symbols, k=1))

                        show_combo(combo)

                        if buff:
                            fight(combo, buff=True)
                        if debuff:
                            fight(combo, debuff=True)
                        if not buff and not debuff:
                            fight(combo)

            result = fight(combo)

            if win:
                result = "win"
            else:
                result = "lose"

            while True:
                # продолжение похода
                if result == "win" or escape:
                    escape = False
                    print("❓ Хотите продолжить поход?")
                    print("1. ✅ Продолжить")
                    print("2. ❌ Отступить")

                    answ = "/"
                    while answ not in "12":
                        answ = str(input())
                        if answ == "" or len(answ) != 1:
                            answ = "/"

                    if str(answ) == "1":
                        # поход продолжается
                        print("⚔️ Поход продолжается.")
                        cont()
                        buff_combo = False
                        debuff_combo = False
                        back_dealer = False

                        if choice(range(1, 6)) == 1:
                            # торговец
                            print("⚖️ Из темноты доносится звон весов и скрип тяжелой повозки. Вы встречаете бродячего торговца.")
                            cont()
                            print("1. 🤝 Торговаться")
                            print("2. 👣 Идти дальше")

                            choice_dealer = "/"
                            while choice_dealer not in "12":
                                choice_dealer = str(input())
                                if choice_dealer == "" or len(choice_dealer) != 1:
                                    choice_dealer = "/"

                            def dealer():
                                global krit, player_hp
                                nonlocal back_dealer, choice_dealer

                                if back_dealer:
                                    print("1. 🤝 Торговаться")
                                    print("2. 👣 Идти дальше")

                                    choice_dealer = "/"
                                    while choice_dealer not in "12":
                                        choice_dealer = str(input())
                                        if choice_dealer == "" or len(choice_dealer) != 1:
                                            choice_dealer = "/"

                                if choice_dealer == "2":
                                    print("Вы продолжаете поход...")
                                    return
                                elif choice_dealer == "1":
                                    with open("players.json", "r") as file:
                                        players = json.load(file)

                                        print(f"🪙 Монеты: {players[registration.login_for_enter]["coins"]}")
                                        print("🛒 Ассортимент:")
                                        print("    1. 🧪️ Капля жизни - 60 🪙(восстанавливает 20 HP)")
                                        print("    2. ⚡ Зелье ярости - 45 🪙(+5% к шансу крита на этот поход)")
                                        print("    3. ⚡ Зелье проворности - 45 🪙(+5% к шансу уклонения на этот поход)")
                                        print("    4. ⬅️ Назад")
                                        choice_buy = str(input("    "))

                                        if choice_buy == "1":

                                            if int(players[registration.login_for_enter]["coins"]) >= 60:
                                                if player_hp < 100:
                                                    print("💰 Приобретено")
                                                    player_hp += 20
                                                    if player_hp > 100:
                                                        player_hp = 100
                                                    players[registration.login_for_enter]["coins"] = str(int(players[registration.login_for_enter]["coins"]) - 60)
                                                    return
                                                else:
                                                    print("⚠️ У вас максимальный запас здоровья.")
                                                    dealer()

                                            else:
                                                print("⚠️ Недостаточно монет")
                                                dealer()

                                        elif choice_buy == "2":
                                            if int(players[registration.login_for_enter]["coins"]) >= 45:
                                                print("💰 Приобретено")
                                                krit += 5
                                                players[registration.login_for_enter]["coins"] = str(int(players[registration.login_for_enter]["coins"]) - 45)
                                                return

                                            else:
                                                print("⚠️ Недостаточно монет")
                                                dealer()

                                        elif choice_buy == "3":
                                            if int(players[registration.login_for_enter]["coins"]) >= 45:
                                                print("💰 Приобретено")
                                                evasion_hero += 5
                                                players[registration.login_for_enter]["coins"] = str(int(players[registration.login_for_enter]["coins"]) - 45)
                                                return

                                            else:
                                                print("⚠️ Недостаточно монет")
                                                dealer()

                                        elif choice_buy == "4":
                                            back_dealer = True
                                            dealer()

                                    with open("players.json", "w") as file:
                                        json.dump(players, file)

                            dealer()

                        else:
                            if choice(range(1, 101)) <= 15:
                                # алтарь
                                print("🔮 Перед вами из тьмы материализуется Древний Монолит.")
                                print("Исход прикосновения к нему неизвестен.")
                                print("1. ✋ Рискнуть")
                                print("2. ↩️ Пройти мимо")

                                choice_monolit = "/"
                                while choice_monolit not in "12":
                                    choice_monolit = str(input())
                                    if choice_monolit == "" or len(choice_monolit) != 1:
                                        choice_monolit = "/"

                                if choice_monolit == "1":

                                    if choice(range(1, 3)) == 1:
                                        # бафф
                                        print("✨ Руны на камне вспыхивают мягким, благородным светом.")
                                        buffs = ["+1 жизней героя", "+1 секунда", "-1 жизней врага", "уменьшение длины комбинации", "увеличение шанса крита", "увеличение шанса уклонения"]

                                        random_buff = choice(range(1, 101))

                                        if random_buff in range(1, 11):
                                            # +20 хп
                                            player_hp += 20
                                            if player_hp > 100:
                                                player_hp = 100
                                            print("✨ Монолит восстонавливает вам 20 HP.")

                                        elif random_buff in range(11, 21):
                                            # -1 жизней врага
                                            right += 1
                                            print("⚡ Энергия Монолита ослабляет врагов в этом лесу: здоровье следующего противника уменьшено на 1.")

                                        elif random_buff in range(21, 46):
                                            # увеличение шанса крита
                                            krit += 5
                                            print("✨ Энергия Монолита обостряет ваши чувства: шанс критического удара увеличен.")

                                        elif random_buff in range(46, 61):
                                            # +1 секунда
                                            time_for_rage -= 1
                                            print("✨ Монолит дарует вам секунду превосходства (+1 секунда к таймеру).")

                                        elif random_buff in range(61, 76):
                                            # уменьшение длины комбинации
                                            print("✨ Длина комбинаций уменьшена.")
                                            buff_combo = True

                                        elif random_buff in range(76, 101):
                                            # увеличение шанса уклонения
                                            print("✨ Энергия Монолита обостряет ваши чувства: шанс уклонения увеличен.")
                                            evasion_hero += 5

                                    else:
                                        # дебафф
                                        print("⚡ Руны на камне искажаются и наливаются зловещим багровым.")
                                        debuffs = ["-1 жизней героя", "-1 секунда", "+1 жизней врага", "увеличение длины комбинации", "уменьшение шанса крита", "уменьшение шанса уклонения"]
                                        random_debuff = choice(range(1, 101))
                                        if random_debuff in range(1, 11):
                                            # -20 хп
                                            print("⚡ Энергия Монолита забирает ваши силы: вы теряете 20 HP.")
                                            player_hp -= 20
                                            if player_hp <= 0:

                                                death()

                                                return "lose"

                                        elif random_debuff in range(11, 21):
                                            # +1 жизней врага
                                            right -= 1
                                            print("⚡ Энергия Монолита подпитывает монстров в этом лесу: здоровье следующего врага увеличено на 1.")

                                        elif random_debuff in range(21, 46):
                                            # уменьшение шанса крита
                                            print("⚡ Древний камень туманит ваш разум: шанс критического удара уменьшен.")
                                            krit -= 5

                                        elif random_debuff in range(46, 61):
                                            # -1 секунда
                                            time_for_rage += 1
                                            print("⚡ Монолит сковывает ваши движения: время для ввода уменьшено на 1 секунду.")

                                        elif random_debuff in range(61, 76):
                                            # увеличение длины комбинации
                                            print("⚡ Длина комбинаций увеличена.")
                                            debuff_combo = True

                                        elif random_debuff in range(76, 101):
                                            # увеличение шанса уклонения
                                            print("⚡ Монолит сковывает ваши движения: шанс уклонения уменьшен.")
                                            evasion_hero -= 5

                                elif choice_monolit == "2":
                                    print("Вы оставляете Древний Монолит позади. Его тусклый свет медленно растворяется во тьме...")

                                cont()

                        # смена уровня сложности
                        if sum_win >= 6:
                            print("⚠️ Внимание!")
                            print(f"❓ Готовы ли вы продвинуться глубже и поднять Уровень Сложности до '{levels[level]}'?")
                            print("1. 🔥 Повысить сложность")
                            print("2. 🛡️ Остаться на текущей")

                            level_up_answ = "/"
                            while level_up_answ not in "12":
                                level_up_answ = str(input())
                                if level_up_answ == "" or len(level_up_answ) != 1:
                                    level_up_answ = "/"

                            if level_up_answ == "1":
                                offic_level = offic_level + 1
                                level = level + 1
                                level_up = True
                                sum_win = 0

                                print("❓ Желаете сделать привал перед тем, как отправиться дальше?")
                                print("1. 🏕️ Да, сделать привал")
                                print("2. 👣 Нет, продолжить путь")

                                choice_camp = "/"
                                while choice_camp not in "12":
                                    choice_camp = str(input())
                                    if choice_camp == "" or len(choice_camp) != 1:
                                        choice_camp = "/"

                                if choice_camp == "2":
                                    print("🗺️ Вы углубляетесь в неизведанные земли.")

                                elif choice_camp == "1":
                                    # привал
                                    if camp_krit:
                                        krit -= 5
                                        camp_krit = False
                                    if camp_evasion:
                                        evasion_hero -= 5
                                        camp_evasion = False

                                    print()
                                    print("🏕️ Привал")
                                    print()
                                    print("1. 🍖 Поесть (+20 HP)")
                                    print("2. 🗡️ Заточить оружие (+5% к шансу крита до следующего привала)")
                                    print("3. 🥷 Собраться духом (+5% к уклонению до следующего привала)")
                                    print("4. 👣 Продолжить путь")

                                    choice_camp = "/"
                                    while choice_camp not in "1234":
                                        choice_camp = str(input())
                                        if choice_camp == "" or len(choice_camp) != 1:
                                            choice_camp = "/"

                                    if choice_camp == "1":
                                        player_hp += 20
                                        if player_hp > 100:
                                            player_hp = 100
                                        print("🍖 Вы подкрепились и восстановили 20 HP.")
                                        print("⚔️ Вы продолжаете путь...")

                                    elif choice_camp == "2":
                                        krit += 5
                                        camp_krit = True
                                        print("🗡️ Вы заточили оружие. Шанс критического удара увеличен до следующего привала.")
                                        print("⚔️ Вы продолжаете путь...")

                                    elif choice_camp == "3":
                                        evasion_hero += 5
                                        camp_evasion = True
                                        print("🥷 Вы собрались духом. Шанс уклонения увеличен до следующего привала.")
                                        print("⚔️ Вы продолжаете путь...")

                                    elif choice_camp == "4":
                                        print("🗺️ Вы углубляетесь в неизведанные земли.")

                            elif level_up_answ == "2":
                                print("🛡️ Безопасность превыше всего. Сложность не изменена.")
                                print("Вы продолжаете зачистку текущей зоны. Наберитесь сил перед новым вызовом.")
                                sum_win = 0
                                cont()

                        if buff_combo:
                            more_fight(fight, time_for_rage, mode, level_up, buff=True)
                        elif debuff_combo:
                            more_fight(fight, time_for_rage, mode, level_up, debuff=True)
                        else:
                            more_fight(fight, time_for_rage, mode, level_up)

                        level_up = False

                        if not win and not escape:
                            break

                    else:
                        # уход из похода
                        if escape:
                            chance = 3
                        else:
                            chance = 6

                        if randrange(1, chance) == 1:
                            print("⚠ На пути назад вам не повезло встретить монстра.")
                            cont()

                            monster = identify_monster(level)

                            print(f"Это был {monsters[monster]["name"]}.")
                            cont()

                            if escape:
                                print("⚠️ Вы ранены после недавнего бегства. Ещё один удар - и всё закончится.")
                                escape_fight = True
                                cont()

                            print("⏱ Выделенное время в секундах:", monsters[monster]["time"])

                            combo = choices(symbols, k=monsters[monster]["letters"])

                            show_combo(combo)

                            result_escape = fight(combo)
                            if win:
                                print("Монстр повержен! Вы благополучно возвращаетесь в лагерь.")
                                halberd = False
                                hunger = False

                        else:
                            print("🏃 Вы решили не испытывать судьбу и завершили поход.")
                            halberd = False
                            hunger = False

                        break

                else:
                    break

            # ачивки
            with open("players.json", "r") as file:
                players = json.load(file)

                if int(players[registration.login_for_enter]["count_kill_monster"]) > 0:
                    players[registration.login_for_enter]["achievements"]["убить_первого_монстра"]["status"] = True

                if use_escape:
                    players[registration.login_for_enter]["achievements"]["впервые_спастись_бегством"]["status"] = True

                if int(players[registration.login_for_enter]["count_death"]) > 0:
                    players[registration.login_for_enter]["achievements"]["погибнуть_впервые"]["status"] = True

                if int(players[registration.login_for_enter]["count_death"]) >= 10:
                    players[registration.login_for_enter]["achievements"]["погибнуть_10_раз"]["status"] = True

                if players[registration.login_for_enter]["inventory"]:
                    players[registration.login_for_enter]["achievements"]["получить_первый_предмет"]["status"] = True

                if set(list(players[registration.login_for_enter]["inventory"].keys())) == set(["Lich", "Devourer", "Destroyer", "Berserk", "Vasilisk", "Faceless"]):
                    players[registration.login_for_enter]["achievements"]["собрать_все_предметы"]["status"] = True

                if rage and result == "win":
                    players[registration.login_for_enter]["achievements"]["пережить_ярость_монстра"]["status"] = True

                if use_lich_heart or use_hunger or use_halberd or use_rage_berserk or use_vasilisk_orb or use_robe:
                    players[registration.login_for_enter]["achievements"]["использовать_первый_предмет"]["status"] = True

                if result == "win" and (player_hp == 100):
                    players[registration.login_for_enter]["achievements"]["победить_монстра_без_урона"]["status"] = True

                # титулы
                if win_berserk:
                    players[registration.login_for_enter]["achievements"]["достичь_ранга_ученик"]["status"] = True

                if win_beast:
                    players[registration.login_for_enter]["achievements"]["достичь_ранга_охотник"]["status"] = True

                if win_titan:
                    players[registration.login_for_enter]["achievements"]["достичь_ранга_элитный_каратель"]["status"] = True

                if win_leviathan:
                    players[registration.login_for_enter]["achievements"]["достичь_ранга_инквизитор"]["status"] = True

                if win_devourer:
                    players[registration.login_for_enter]["achievements"]["достичь_ранга_немезида"]["status"] = True
                # титулы

            with open("players.json", "w") as file:
                json.dump(players, file)
            # ачивки

        if not back:
            hike()
        menu()
        main()

    elif str(ivent) == "2":
        # дуэль
        def ques():

            global lets, words, nums
            global offic_syms
            global monsters
            global lich, destroyer, devourer, berserk
            global symbols

            seria = 0
            alls_seria = []

            print()
            print("📋 Меню: Дуэль вечности")
            print("1. ⚔️ В бой!")
            print("2. 📜 Руководство")
            print("3. 🏆 Рекорд")
            print("4. 🔙 Назад")

            choice_want = "/"
            while choice_want not in "1234":
                choice_want = str(input())
                if choice_want == "" or len(choice_want) != 1:
                    choice_want = "/"

            if choice_want == "4":
                # назад
                menu()
                main()

            if choice_want == "2":
                # руководство
                print("В этом режиме вы сами выбираете противника.")
                print("После этого начнётся бесконечная дуэль:")
                print("вам нужно вводить комбинации снова и снова.")
                print()
                print("У вас есть несколько жизней.")
                print("Каждая ошибка или нехватка времени отнимает одну жизнь.")
                print()
                print("Бой продолжается, пока у вас не закончатся все жизни.")
                print()
                print("С каждым успешным вводом счётчик растёт.")
                print()
                print("Ваша цель — набрать как можно больше успешных вводов подряд.")
                print("В конце вы увидите:")
                print("- общее количество успешных вводов")
                print("- лучшую серию подряд")
                print()
                print("Удачи.")
                ques()

            elif choice_want == "3":
                # рекорд
                print()
                with open("players.json", "r") as file:
                    players = json.load(file)
                    for key in players[registration.login_for_enter]["duel"]:
                        if players[registration.login_for_enter]["duel"][key]["right_duel"] != "0" and players[registration.login_for_enter]["duel"][key]["best_seria_duel"] != "0":
                            print(f"{key}: Количество успешных вводов - {players[registration.login_for_enter]["duel"][key]["right_duel"]}, Лучшая серия - {players[registration.login_for_enter]["duel"][key]["best_seria_duel"]}")

                ques()

            elif choice_want == "1":
                # дуэль бой
                mode, lang = submodes()

                print("Выберите уровень монстра (1–31):")

                need_range = ""
                for i in range(1, 32):
                    need_range += str(i)

                monster = "/"
                while monster not in need_range:
                    monster = str(input())
                    if monster == "" or len(monster) != 1:
                        monster = "/"

                monster = int(monster)

                print(f"Ваш противник - {monsters[monster]["name"]}")

                right = 0
                rage = False
                time_for_rage = 0
                player_hp = 100

                # берсерк
                if monster == 6:
                    print(monsters[monster]["text"])
                    berserk = True
                    cont()
                # берсерк

                print(f"❤️ HP: {player_hp}/100")

                cont()

                print("⏱ Выделенное время в секундах:", monsters[monster]["time"] - time_for_rage)
                cont()

                combo = choices(symbols, k=monsters[monster]["letters"])

                show_combo(combo)

                cont()

                def duel(arg):
                    nonlocal right, rage, time_for_rage, monster
                    global berserk
                    nonlocal seria, alls_seria
                    global monsters
                    global lets, words, nums, symbols
                    nonlocal player_hp

                    need_cont = False
                    combo = arg
                    change_regime = False
                    time_for_compare = monsters[monster]["time"]

                    start = time.time()

                    input_combo = input()

                    end = time.time()

                    if "".join(input_combo.lower().split()) == "".join(combo).lower() and (end - start) <= monsters[monster]["time"] - time_for_rage:
                        # успех
                        right += 1
                        time_for_rage = 0

                        print("✅ Успешный ввод")
                        seria += 1

                        if right % 5 == 0:
                            # ярость
                            if not berserk:
                                # монстр
                                if randrange(1, 101) <= 30:
                                    print("⚡ Монстр в бешенстве!")
                                    print("⌛ Время на следующий ввод уменьшено.")
                                    rage = True
                                    need_cont = True
                                    time_for_rage = 1

                            else:
                                # берсерк
                                if randrange(1, 101) <= 50:
                                    print("⚡ Берсерк в ярости!")
                                    print("⌛ Время на следующий ввод уменьшено.")
                                    rage = True
                                    need_cont = True
                                    time_for_rage = 1

                        # разраб
                        if monster == 31:
                            if randrange(1, 3) == 1:
                                change_regime = True
                                print("⚠️ Апостол разработчика изменяет правила испытания.")

                                available_modes = ["russ_lets", "angl_lets", "russ_words", "angl_words", "nums"]

                                # отбор доступных режимов
                                if str(mode) == "1":
                                    if str(lang) == "1":
                                        del available_modes[0]

                                    if str(lang) == "2":
                                        del available_modes[1]

                                    lets = True

                                if str(mode) == "2":

                                    if str(lang) == "1":
                                        del available_modes[2]

                                    if str(lang) == "2":
                                        del available_modes[3]

                                if str(mode) == "3":

                                    del available_modes[4]

                                # отбор доступных режимов

                                change_mode = choice(available_modes)

                                if change_mode == "russ_lets":
                                    print("Следующий режим: Русские буквы.")
                                    symbols = "АБВГДЕЁЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"
                                    lets = True

                                if change_mode == "angl_lets":
                                    print("Следующий режим: Английские буквы.")
                                    symbols = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
                                    lets = True

                                if change_mode == "russ_words":
                                    print("Следующий режим: Русские слова.")
                                    symbols = russ_words
                                    words = True
                                    monsters = monsters_w

                                if change_mode == "angl_words":
                                    print("Следующий режим: Английские слова.")
                                    symbols = angl_words
                                    words = True
                                    monsters = monsters_w

                                if change_mode == "nums":
                                    print("Следующий режим: Цифры.")
                                    symbols = "0123456789"
                                    nums = True

                                cont()

                                if change_mode in ["russ_words", "angl_words"]:
                                    combo = choices(symbols, k=monsters[monster]["letters"])
                                    time_for_compare = monsters_w[monster]["time"]
                                else:
                                    combo = choices(symbols, k=monsters[monster]["lets_for_change"])
                                    time_for_compare = monsters[monster]["time"]
                            # разраб

                        if monster != 31 or not change_regime:
                            combo = choices(symbols, k=monsters[monster]["letters"])

                        if need_cont:
                            cont()

                        show_combo(combo)

                        if need_cont:
                            cont()

                        duel(combo)

                    else:
                        # ранение героя
                        min_damage, max_damage = [int(el) for el in monsters[monster]["damage"].split("-")]
                        damage = choice(range(min_damage, max_damage + 1))

                        if player_hp - damage > 0:
                            if "".join(input_combo.lower().split()) != "".join(combo).lower():
                                print("❌ Неверный ответ")
                            elif (end - start) > monsters[monster]["time"] - time_for_rage:
                                print("⌛ Вы превысили допустимое время")

                            alls_seria.append(seria)
                            seria = 0

                            print("💔 Вас ранили!")
                            cont()

                            player_hp -= damage

                            print(f"❤️ HP: {player_hp}/100")

                            combo = choices(symbols, k=monsters[monster]["letters"])

                            cont()

                            show_combo(combo)

                            duel(combo)

                        else:
                            # смерть
                            print("💀 Вы погибли!")

                            with open("players.json", "r") as file:
                                players = json.load(file)

                                if alls_seria:
                                    need_seria = max(alls_seria)
                                else:
                                    need_seria = seria

                                if right >= int(players[registration.login_for_enter]["duel"][monsters[monster]["name"]]["right_duel"]):
                                    players[registration.login_for_enter]["duel"][monsters[monster]["name"]]["right_duel"] = str(right)

                                if need_seria >= int(players[registration.login_for_enter]["duel"][monsters[monster]["name"]]["best_seria_duel"]):
                                    players[registration.login_for_enter]["duel"][monsters[monster]["name"]]["best_seria_duel"] = str(need_seria)

                            with open("players.json", "w") as file:
                                json.dump(players, file)

                            main()

                duel(combo)

        ques()

    elif str(ivent) == "3":
        # власть чисел
        pass

    elif str(ivent) == "4":
        # статистика
        print()
        print("Статистика:\n")

        with open("players.json", "r") as file:
            players = json.load(file)
            # титулы
            if players[registration.login_for_enter]["achievements"]["достичь_ранга_ученик"]["status"] == True:
                titul = "📖 Ученик"

            if players[registration.login_for_enter]["achievements"]["достичь_ранга_охотник"]["status"] == True:
                titul = "🩸 Охотник"

            if players[registration.login_for_enter]["achievements"]["достичь_ранга_элитный_каратель"]["status"] == True:
                titul = "⚔️ Элитный каратель"

            if players[registration.login_for_enter]["achievements"]["достичь_ранга_инквизитор"]["status"] == True:
                titul = "⛓️ Инквизитор"

            if players[registration.login_for_enter]["achievements"]["достичь_ранга_немезида"]["status"] == True:
                titul = "💀 Немезида"
            # титулы

        print(f"Титул: {titul}")

        with open("players.json", "r") as file:
            players = json.load(file)
            if players[registration.login_for_enter]["best_win_monster"].split()[-1] == "0":
                print("⚠ Вы ещё не одолели ни одного монстра.")

            else:
                imya = players[registration.login_for_enter]["best_win_monster"].split()[1:]

                if len(imya) > 1:
                    imya = " ".join(imya)
                else:
                    imya = players[registration.login_for_enter]["best_win_monster"].split()[-1]

                print(f"👑 Сильнейший монстр побежденный вами: {imya}.")

            print(f"⚔️ Количество убитых монстров: {players[registration.login_for_enter]["count_kill_monster"]}")
            print(f"💀 Количество смертей: {players[registration.login_for_enter]["count_death"]}")
            try:
                print(f"📊 K/D: {round(int(players[registration.login_for_enter]["count_kill_monster"]) / int(players[registration.login_for_enter]["count_death"]), 2)}")
            except ZeroDivisionError:
                print("⚠ K/D не может быть рассчитан, так как у вас 0 смертей.")

            if players[registration.login_for_enter]["inventory"]:
                print()
                print("🎒 Инвентарь:")
                for key in players[registration.login_for_enter]["inventory"]:
                    print(f"{list(players[registration.login_for_enter]["inventory"][key].keys())[0]}: {players[registration.login_for_enter]["inventory"][key][list(players[registration.login_for_enter]["inventory"][key].keys())[0]]}")
                print()
            else:
                print("⚠ Инвентарь пуст.")

            print(f"🪙 Монеты: {players[registration.login_for_enter]["coins"]}")

        menu()
        main()

    elif str(ivent) == "5":
        # достижения
        print()
        print("Достижения:\n")
        with open("players.json", "r") as file:
            players = json.load(file)
            for key in players[registration.login_for_enter]["achievements"]:
                print(f"🥇 {players[registration.login_for_enter]["achievements"][key]["achiev"]}")
                print(f"{players[registration.login_for_enter]["achievements"][key]["text"]}")

                if players[registration.login_for_enter]["achievements"][key]["status"] == False:
                    print("❌ Не получено")
                else:
                    print("✅ Получено")

                print()

        menu()
        main()

    elif str(ivent) == "6":
        # настройки
        settings = ["🗑️ Удалить аккаунт"]
        for i in range(1, len(settings) + 1):
            print(f"{i}. {settings[i - 1]}")

        print("2. 🔙 Назад")

        choice_settings = "/"
        while choice_settings not in "12":
            choice_settings = str(input())
            if choice_settings == "" or len(choice_settings) != 1:
                choice_settings = "/"

        if str(choice_settings) == "1":
            print("✅ Аккаунт удален.")

            with open("players.json", "r") as file:
                players = json.load(file)
                del players[registration.login_for_enter]

            with open("players.json", "w") as file:
                json.dump(players, file)

            with open("last_user.json", "w") as file:
                file.write("{}")

            return

        elif str(choice_settings) == "2":
            menu()
            main()


main()
