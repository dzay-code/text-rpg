from random import *
from time import sleep
import keyboard as kb
import pyautogui as pg
import time
from data import monsters, monsters_w, items, duel, angl_words, russ_words
import json
import registration
import math

repeat = False
words = False
nums = False
lets = False
escape = False
offic_level = 0
offic_syms = ""
symbols = None


def some():
    if lets:
        print("🔤 Буквы:", " ".join(combo))
    elif words:
        print("📝 Слова:", " ".join(combo))
    elif nums:
        print("🔢 Цифры:", " ".join(combo))


def use_item():

    # использование предметов инвентаря до битвы
    with open("players.json", "r") as file:
        players = json.load(file)
        if players[registration.login_for_enter]["inventory"]:
            print("🎒 Желаете использовать предмет из инвентаря?")
            print("1. ✅ ДА")
            print("2. ❌ НЕТ")
            choice_item = str(input())
            i = 0
            if choice_item == "1":
                print("🔢 Выберите номер предмета который хотите использовать.")
                for key in players[registration.login_for_enter]["inventory"]:
                    i += 1
                    print(f"{i}. {list(players[registration.login_for_enter]["inventory"][key].keys())[0]}: {players[registration.login_for_enter]["inventory"][key][list(players[registration.login_for_enter]["inventory"][key].keys())[0]]}")
                choice_item = int(input())

                if list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Lich":
                    lich_heart = True
                    lich = False

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Destroyer":
                    halberd = True
                    destroyer = False

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Devourer":
                    beelzebub = True
                    devourer = False

                elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Berserk":
                    rage_berserk = True

                del players[registration.login_for_enter]["inventory"][list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1]]
                with open("players.json", "w") as file:
                    json.dump(players, file)

                print(f"✅ Предмет использован.")

    # использование предметов инвентаря до битвы


def more_fight(fight):

    if offic_level == 1:
        monster = randrange(1, 7)
    elif offic_level == 2:
        monster = randrange(1, 13)
    elif offic_level == 3:
        monster = randrange(7, 19)
    elif offic_level == 4:
        monster = randrange(13, 25)
    elif offic_level == 5:
        monster = randrange(19, 32)

    print("Едва вы успели перевести дух после боя, как из темноты появился новый враг.")
    cont()
    print(f"Это был {monsters[monster]["name"]}.")
    cont()

    # лич
    if monster == 23:
        print(monsters[monster]["text"])
        lich = True
        cont()
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
        print(monsters[monster]["text"])
        berserk = True
        cont()
    # берсерк

    if monster in [23, 28, 30, 6]:
        print("💎 С этого монстра может выпасть предмет.")

    print(f"❤️ Жизни: {monsters[monster]["hits"]}")
    print("⏱ Выделенное время в секундах:", monsters[monster]["time"])

    # использование предметов инвентаря до битвы
    use_item()
    # использование предметов инвентаря до битвы

    combo = choices(offic_syms, k=monsters[monster]["letters"])

    # пожиратель
    if beelzebub:
        if str(mode) == "1" or str(mode) == "3":
            combo = combo[:-3]
        elif str(mode) == "2":
            combo = combo[:-1]
    # пожиратель

    if lets:
        print("🔤️ Буквы:", " ".join(combo))
    elif words:
        print("📝 Слова:", " ".join(combo))
    elif nums:
        print("🔢 Цифры:", " ".join(combo))

    # сердце лича
    if lich_heart:
        num = 0
    # сердце лича

    # разрушитель
    if halberd:
        right = 1
    # разрушитель

    fight(combo, need=monster)


def cont():
    kb.wait("enter")
    pg.press("backspace")


ivents = ["🗺️ Поход", "⚔️ Дуэль вечности", "📊 Статистика", "🎖 Достижения", "⚙️ Настройки"]
levels = ["Ученик", "Охотник", "Элитный каратель", "Инквизитор", "Немезида"]

print(f"Добро пожаловать в игру!\nИспользуйте 'enter' чтобы продолжить.")
cont()

ivent = ""


def menu():
    global ivent
    print()
    print("📋 Меню:")
    for i in range(1, len(ivents) + 1):
        print(str(i) + ". " + ivents[i - 1])
    ivent = input()


menu()


def main():
    if str(ivent) == "1":
        def hike():
            global lets, words, nums
            global offic_level, offic_syms
            global monsters
            global symbols
            # global lich_heart, halberd, beelzebub
            # global lich, destroyer, devourer, berserk

            win = False
            escape_fight = False

            # предметы
            lich = False
            lich_heart = False

            destroyer = False
            halberd = False

            devourer = False
            beelzebub = False

            berserk = False
            rage_berserk = False
            # предметы

            right = 0
            rage = False
            time_for_rage = 0
            num = 1
            win_berserk = False

            # разделение

            print("⚙️ Выберите режим:")
            print("1. 🔤 Буквы")
            print("2. 📝 Слова")
            print("3. 🔢 Цифры")
            mode = input()

            if str(mode) == "1" or str(mode) == "2":
                print("🌐 Выберите язык:")
                print("1. Русский")
                print("2. Английский")
                lang = input()

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

            print("Выберите сложность:")
            for i in range(1, len(levels) + 1):
                print(str(i) + ". " + levels[i - 1])
            level = int(input())

            offic_level = level
            offic_syms = symbols
            # разделение

            sleep(1)
            print("Вы отправились в поход в густой лес, где обитают страшные твари.")
            cont()
            if level == 1:
                monster = randrange(1, 7)
            elif level == 2:
                monster = randrange(1, 13)
            elif level == 3:
                monster = randrange(7, 19)
            elif level == 4:
                monster = randrange(13, 25)
            elif level == 5:
                monster = randrange(19, 32)

            print("Пробираясь через тёмный лес, вы внезапно наткнулись на жуткого монстра.")
            cont()
            print(f"Это был {monsters[monster]["name"]}.")
            cont()

            # лич
            if monster == 23:
                print(monsters[monster]["text"])
                lich = True
                cont()
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
                print(monsters[monster]["text"])
                berserk = True
                cont()
            # берсерк

            if monster in [23, 28, 30, 6]:
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

            print(f"❤️ Жизни: {monsters[monster]["hits"]}")

            cont()
            print("Так что будьте осторожны.")
            cont()
            print("⏱ Выделенное время в секундах:", monsters[monster]["time"] - time_for_rage)

            # использование предметов инвентаря до битвы
            with open("players.json", "r") as file:
                players = json.load(file)
                if players[registration.login_for_enter]["inventory"]:
                    print("🎒 Желаете использовать предмет из инвентаря?")
                    print("1. ✅ ДА")
                    print("2. ❌ НЕТ")
                    choice_item = str(input())
                    i = 0
                    if choice_item == "1":
                        print("🔢 Выберите номер предмета который хотите использовать.")
                        for key in players[registration.login_for_enter]["inventory"]:
                            i += 1
                            print(f"{i}. {list(players[registration.login_for_enter]["inventory"][key].keys())[0]}: {players[registration.login_for_enter]["inventory"][key][list(players[registration.login_for_enter]["inventory"][key].keys())[0]]}")
                        choice_item = int(input())

                        if list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Lich":
                            lich_heart = True
                            lich = False

                        elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Destroyer":
                            halberd = True
                            destroyer = False

                        elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Devourer":
                            beelzebub = True
                            devourer = False

                        elif list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1] == "Berserk":
                            rage_berserk = True

                        del players[registration.login_for_enter]["inventory"][list(players[registration.login_for_enter]["inventory"].keys())[choice_item - 1]]
                        with open("players.json", "w") as file:
                            json.dump(players, file)

                        print(f"✅ Предмет использован.")
            # использование предметов инвентаря до битвы

            combo = choices(symbols, k=monsters[monster]["letters"])

            # пожиратель
            if beelzebub:
                if str(mode) == "1" or str(mode) == "3":
                    combo = combo[:-3]
                elif str(mode) == "2":
                    combo = combo[:-1]
            # пожиратель

            if lets:
                print("🔤 Буквы:", " ".join(combo))
            elif words:
                print("📝 Слова:", " ".join(combo))
            elif nums:
                print("🔢 Цифры:", " ".join(combo))

            # сердце лича
            if lich_heart:
                num = 0
            # сердце лича

            # разрушитель
            if halberd:
                right = 1
            # разрушитель

            def fight(arg, need=1):
                nonlocal num
                global repeat
                global win
                nonlocal right, rage, time_for_rage, monster, win_berserk
                global escape
                nonlocal lich_heart, rage_berserk, berserk, beelzebub, halberd
                nonlocal mode, lang
                global symbols, lets, words, nums, monsters

                if need != 1:
                    monster = need

                combo = arg
                change_regime = False
                time_for_compare = monsters[monster]["time"]

                start = time.time()

                input_combo = input()

                end = time.time()

                if "".join(input_combo.lower().split()) == "".join(combo).lower() and (end - start) <= time_for_compare - time_for_rage:

                    # берсерк
                    if rage_berserk:
                        if randrange(1, 101) <= 15:
                            print("💥 Критический удар!")
                            right += 2
                        else:
                            right += 1
                    # берсерк

                    else:
                        if randrange(1, 11) == 1:
                            print("💥 Критический удар!")
                            right += 2
                        else:
                            right += 1

                    if right >= monsters[monster]["combos"]:
                        print("✅ Вы победили!")
                        win = True
                        right = 0

                        # лич
                        if lich:
                            print("🎁 Бессмертный лич повержен. Вы получаете Сердце лича.")
                            with open("players.json", "r") as file:
                                players = json.load(file)
                            players[registration.login_for_enter]["inventory"]["Lich"] = {"Сердце лича": items["Сердце лича"]}
                            with open("players.json", "w") as file:
                                json.dump(players, file)
                        # лич

                        # разрушитель
                        if destroyer:
                            print("🎁 Разрушитель небес повержен. Вы получаете Алебарда Разрушителя.")
                            with open("players.json", "r") as file:
                                players = json.load(file)
                            players[registration.login_for_enter]["inventory"]["Destroyer"] = {"Алебарда Разрушителя": items["Алебарда Разрушителя"]}
                            with open("players.json", "w") as file:
                                json.dump(players, file)
                        # разрушитель

                        # пожиратель
                        if devourer:
                            print("🎁 Пожиратель миров повержен. Вы получаете Вельзевул.")
                            with open("players.json", "r") as file:
                                players = json.load(file)
                            players[registration.login_for_enter]["inventory"]["Devourer"] = {"Вельзевул": items["Вельзевул"]}
                            with open("players.json", "w") as file:
                                json.dump(players, file)
                        # пожиратель

                        # берсерк
                        if berserk:
                            win_berserk = True
                            if randrange(1, 5) == 1:
                                print("🎁 Берсерк повержен. Вы получаете Ярость берсерка.")
                                with open("players.json", "r") as file:
                                    players = json.load(file)
                                players[registration.login_for_enter]["inventory"]["Berserk"] = {"Ярость берсерка": items["Ярость берсерка"]}
                                with open("players.json", "w") as file:
                                    json.dump(players, file)
                        # берсерк

                        with open("players.json", "r") as file:
                            players = json.load(file)
                            if monster > int(players[registration.login_for_enter]["best_win_monster"].split()[0]):
                                players[registration.login_for_enter]["best_win_monster"] = str(monster) + " " + monsters[monster]["name"]

                        with open("players.json", "w") as file:
                            json.dump(players, file)

                        with open("players.json", "r") as file:
                            players = json.load(file)
                            players[registration.login_for_enter]["count_kill_monster"] = str(int(players[registration.login_for_enter]["count_kill_monster"]) + 1)

                        with open("players.json", "w") as file:
                            json.dump(players, file)

                        return "win"
                    else:
                        print("✅ Вы успешно ранили монстра")
                        cont()
                        if right + 1 == monsters[monster]["combos"]:
                            if not berserk:
                                if randrange(1, 101) <= 30:
                                    print("⚡ Монстр в ярости!")
                                    print("⌛ Время уменьшено!")
                                    rage = True
                                    time_for_rage = 1
                                    need = time_for_compare - time_for_rage
                                    print("⏱ Выделенное время в секундах:", need)
                            else:
                                if randrange(1, 101) <= 50:
                                    print("⚡ Берсерк в бешенстве!")
                                    print("⌛ Время уменьшено!")
                                    rage = True
                                    time_for_rage = 1
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

                                print("⏱ Выделенное время в секундах:", time_for_compare)

                        if monster != 31 or not change_regime:
                            combo = choices(symbols, k=monsters[monster]["letters"])

                        # пожиратель
                        if beelzebub:
                            if str(mode) == "1" or str(mode) == "3":
                                combo = combo[:-3]
                            elif str(mode) == "2":
                                combo = combo[:-1]
                        # пожиратель

                        if lets:
                            print("🔤 Буквы:", " ".join(combo))
                        elif words:
                            print("📝 Слова:", " ".join(combo))
                        elif nums:
                            print("🔢 Цифры:", " ".join(combo))

                        cont()

                        fight(combo)
                else:
                    if escape_fight:
                        print("💀 Вы погибли!")
                        print("Игра окончена.")

                        with open("players.json", "r") as file:
                            players = json.load(file)
                            players[registration.login_for_enter]["count_death"] = str(int(players[registration.login_for_enter]["count_death"]) + 1)

                        with open("players.json", "w") as file:
                            json.dump(players, file)

                        return "lose"

                    if "".join(input_combo.lower().split()) != "".join(combo).lower():
                        print("❌ Неверный ответ")
                    elif (end - start) > monsters[monster]["time"]:
                        print("⌛ Вы превысили допустимое время")

                    if num < monsters[monster]["hits"]:

                        print("💔 Вас ранили!")
                        cont()

                        print(f"❤️ Жизни: {monsters[monster]["hits"] - num}")

                        print("Сосредоточьтесь!")
                        cont()

                        combo = choices(symbols, k=monsters[monster]["letters"])

                        # пожиратель
                        if beelzebub:
                            if str(mode) == "1" or str(mode) == "3":
                                combo = combo[:-3]
                            elif str(mode) == "2":
                                combo = combo[:-1]
                        # пожиратель

                        if lets:
                            print("🔤 Буквы:", " ".join(combo))
                        elif words:
                            print("📝 Слова:", " ".join(combo))
                        elif nums:
                            print("🔢 Цифры:", " ".join(combo))

                        num += 1
                        repeat = True
                        fight(combo)
                    else:
                        if randrange(1, 11) == 1:
                            print("🏃‍♂️ В последний момент вы вырвались из боя и спаслись бегством.")
                            escape = True
                            return "escape"
                        else:
                            print("💀 Вы погибли!")
                            print("Игра окончена.")

                            with open("players.json", "r") as file:
                                players = json.load(file)
                                players[registration.login_for_enter]["count_death"] = str(int(players[registration.login_for_enter]["count_death"]) + 1)

                            with open("players.json", "w") as file:
                                json.dump(players, file)

                            return "lose"

            result = fight(combo)

            if win:
                result = "win"

            while True:
                if result == "win" or (result == "win" and repeat == True) or escape:
                    print("❓ Хотите продолжить поход?")
                    print("1. ✅ ДА")
                    print("2. ❌ НЕТ")
                    answ = input()
                    repeat = False
                    if str(answ) == "1":
                        more_fight(fight)
                    else:
                        if escape:
                            chance = 3
                        else:
                            chance = 6

                        if randrange(1, chance) == 1:
                            print("⚠ На пути назад вам не повезло встретить монстра.")
                            cont()

                            if level == 1:
                                monster = randrange(1, 7)
                            elif level == 2:
                                monster = randrange(1, 13)
                            elif level == 3:
                                monster = randrange(7, 19)
                            elif level == 4:
                                monster = randrange(13, 25)
                            elif level == 5:
                                monster = randrange(19, 32)

                            print(f"Это был {monsters[monster]["name"]}.")
                            cont()

                            if escape:
                                print("⚠️ Вы ранены после недавнего бегства. Ещё один удар - и всё закончится.")
                                escape_fight = True
                                cont()

                            print("⏱ Выделенное время в секундах:", monsters[monster]["time"])

                            combo = choices(symbols, k=monsters[monster]["letters"])
                            if lets:
                                print("🔤 Буквы:", " ".join(combo))
                            elif words:
                                print("📝 Слова:", " ".join(combo))
                            elif nums:
                                print("🔢 Цифры:", " ".join(combo))

                            fight(combo)

                        else:
                            print("🏃 Вы решили не испытывать судьбу и завершили поход.")

                        break

                else:
                    break

            # ачивки
            with open("players.json", "r") as file:
                players = json.load(file)

                if win_berserk:
                    players[registration.login_for_enter]["achievements"]["достичь_ранга_ученик"]["status"] = True

                if int(players[registration.login_for_enter]["count_kill_monster"]) > 0:
                    players[registration.login_for_enter]["achievements"]["убить_первого_монстра"]["status"] = True

                if escape:
                    players[registration.login_for_enter]["achievements"]["впервые_спастись_бегством"]["status"] = True

                if int(players[registration.login_for_enter]["count_death"]) > 0:
                    players[registration.login_for_enter]["achievements"]["погибнуть_впервые"]["status"] = True

                if int(players[registration.login_for_enter]["count_death"]) >= 10:
                    players[registration.login_for_enter]["achievements"]["погибнуть_10_раз"]["status"] = True

                if players[registration.login_for_enter]["inventory"]:
                    players[registration.login_for_enter]["achievements"]["получить_первый_предмет"]["status"] = True

                if set(list(players[registration.login_for_enter]["inventory"].keys())) == set(["Lich", "Devourer", "Destroyer", "Berserk"]):
                    players[registration.login_for_enter]["achievements"]["собрать_все_предметы"]["status"] = True

                if rage and result == "win":
                    players[registration.login_for_enter]["achievements"]["пережить_ярость_монстра"]["status"] = True

                if lich_heart or beelzebub or halberd or rage_berserk:
                    players[registration.login_for_enter]["achievements"]["использовать_первый_предмет"]["status"] = True

                if result == "win" and (num == 1 or num == 0):
                    players[registration.login_for_enter]["achievements"]["победить_монстра_без_урона"]["status"] = True

            with open("players.json", "w") as file:
                json.dump(players, file)
            # ачивки

        hike()
        menu()
        main()

    elif str(ivent) == "2":

        def ques():

            global lets, words, nums
            global offic_syms
            global monsters
            global lich, destroyer, devourer, berserk
            global symbols

            seria = 0
            alls_seria = []

            lich = False
            lich_heart = False

            destroyer = False
            halberd = False

            devourer = False
            beelzebub = False

            berserk = False
            rage_berserk = False

            print()
            print("📋 Меню: Дуэль вечности")
            print("1. ⚔️ В бой!")
            print("2. 📖 Правила")
            print("3. 🏆 Рекорд")
            print("4. 🔙 Назад")

            choice_want = str(input())

            if choice_want == "4":
                menu()
                main()

            if choice_want == "2":
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
                print()
                with open("players.json", "r") as file:
                    players = json.load(file)
                    for key in players[registration.login_for_enter]["duel"]:
                        if players[registration.login_for_enter]["duel"][key]["right_duel"] != "0" and players[registration.login_for_enter]["duel"][key]["best_seria_duel"] != "0":
                            print(f"{key}: Количество успешных вводов - {players[registration.login_for_enter]["duel"][key]["right_duel"]}, Лучшая серия - {players[registration.login_for_enter]["duel"][key]["best_seria_duel"]}")

                ques()

            elif choice_want == "1":

                print("⚙️ Выберите режим:")
                print("1. 🔤 Буквы")
                print("2. 📝 Слова")
                print("3. 🔢 Цифры")
                mode = input()

                if str(mode) == "1" or str(mode) == "2":
                    print("🌐 Выберите язык:")
                    print("1. Русский")
                    print("2. Английский")
                    lang = input()

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

                print("Выберите уровень монстра (1–31):")
                monster = int(input())
                print(f"Ваш противник - {monsters[monster]["name"]}")

                # берсерк
                if monster == 6:
                    print(monsters[monster]["text"])
                    berserk = True
                    cont()
                # берсерк

                right = 0
                rage = False
                time_for_rage = 0
                num = 1

                print(f"❤️ Жизни: {monsters[monster]["hits"]}")

                cont()

                print("⏱ Выделенное время в секундах:", monsters[monster]["time"] - time_for_rage)
                cont()

                combo = choices(symbols, k=monsters[monster]["letters"])

                if lets:
                    print("🔤 Буквы:", " ".join(combo))
                elif words:
                    print("📝 Слова:", " ".join(combo))
                elif nums:
                    print("🔢 Цифры:", " ".join(combo))

                cont()

                def duel(arg):
                    nonlocal num
                    nonlocal right, rage, time_for_rage, monster
                    global berserk
                    nonlocal seria, alls_seria
                    global monsters
                    global lets, words, nums, symbols

                    need_cont = False
                    combo = arg
                    change_regime = False
                    time_for_compare = monsters[monster]["time"]

                    start = time.time()

                    input_combo = input()

                    end = time.time()

                    if "".join(input_combo.lower().split()) == "".join(combo).lower() and (end - start) <= monsters[monster]["time"] - time_for_rage:
                        right += 1
                        time_for_rage = 0

                        print("✅ Успешный ввод")
                        seria += 1

                        if right % 5 == 0:
                            if not berserk:
                                if randrange(1, 101) <= 30:
                                    print("⚡ Монстр в ярости!")
                                    print("⌛ Время на следующий ввод уменьшено.")
                                    rage = True
                                    need_cont = True
                                    time_for_rage = 1

                            else:
                                if randrange(1, 101) <= 50:
                                    print("⚡ Берсерк в бешенстве!")
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

                        if monster != 31 or not change_regime:
                            combo = choices(symbols, k=monsters[monster]["letters"])

                        if need_cont:
                            cont()

                        if lets:
                            print("🔤 Буквы:", " ".join(combo))
                        elif words:
                            print("📝 Слова:", " ".join(combo))
                        elif nums:
                            print("🔢 Цифры:", " ".join(combo))

                        if need_cont:
                            cont()

                        duel(combo)

                    else:

                        if "".join(input_combo.lower().split()) != "".join(combo).lower():
                            print("❌ Неверный ответ")
                        elif (end - start) > monsters[monster]["time"] - time_for_rage:
                            print("⌛ Вы превысили допустимое время")

                        if num == monsters[monster]["hits"]:
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

                        else:
                            alls_seria.append(seria)
                            seria = 0

                            print("💔 Вас ранили!")
                            cont()

                            print(f"❤️ Жизни: {monsters[monster]["hits"] - num}")

                            combo = choices(symbols, k=monsters[monster]["letters"])

                            cont()

                            if lets:
                                print("🔤 Буквы:", " ".join(combo))
                            elif words:
                                print("📝 Слова:", " ".join(combo))
                            elif nums:
                                print("🔢 Цифры:", " ".join(combo))

                            num += 1
                            duel(combo)

                duel(combo)

        ques()

    elif str(ivent) == "3":
        print()
        print("Статистика:\n")
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
                print("⚠ K/D не может быть рассчитан, так как у вас 0 убийств и 0 смертей.")

            if players[registration.login_for_enter]["inventory"]:
                print("🎒 Инвентарь:")
                for key in players[registration.login_for_enter]["inventory"]:
                    print(f"{list(players[registration.login_for_enter]["inventory"][key].keys())[0]}: {players[registration.login_for_enter]["inventory"][key][list(players[registration.login_for_enter]["inventory"][key].keys())[0]]}")
            else:
                print("⚠ Инвентарь пуст.")

        menu()
        main()

    elif str(ivent) == "4":
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

    elif str(ivent) == "5":
        settings = ["🗑️ Удалить аккаунт"]
        for i in range(1, len(settings) + 1):
            print(f"{i}. {settings[i - 1]}")

        print("2. 🔙 Назад")

        choice_settings = input()

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
