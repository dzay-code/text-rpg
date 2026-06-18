# режимы букв и цифр
monsters = {
    1: {"name": "Слизень", "letters": 3, "time": 5, "hits": 5, "combos": 3},
    2: {"name": "Змей Детёныш", "letters": 4, "time": 5, "hits": 5, "combos": 3},
    3: {"name": "Гнилой волк", "letters": 5, "time": 6, "hits": 5, "combos": 3},
    4: {"name": "Пещерный паук", "letters": 6, "time": 6, "hits": 5, "combos": 3},
    5: {"name": "Костяной воин", "letters": 8, "time": 7, "hits": 5, "combos": 3},
    6: {"name": "Берсерк", "letters": 9, "time": 8, "hits": 5, "combos": 3, "text": "Он обладает повышенным шансом впасть в ё   ярость."},

    7: {"name": "Проклятый рыцарь", "letters": 10, "time": 9, "hits": 4, "combos": 3},
    8: {"name": "Грозовой Змей", "letters": 11, "time": 10, "hits": 4, "combos": 3},
    9: {"name": "Кровавый шаман", "letters": 12, "time": 10, "hits": 4, "combos": 3},
    10: {"name": "Демон", "letters": 13, "time": 11, "hits": 4, "combos": 2},
    11: {"name": "Безликий", "letters": 14, "time": 14, "hits": 4, "combos": 2},
    12: {"name": "Адский зверь", "letters": 15, "time": 15, "hits": 3, "combos": 2},

    13: {"name": "Пожиратель плоти", "letters": 16, "time": 16, "hits": 3, "combos": 2},
    14: {"name": "Костяной гигант", "letters": 17, "time": 17, "hits": 3, "combos": 2},
    15: {"name": "Чернокнижник бездны", "letters": 18, "time": 18, "hits": 3, "combos": 2},
    16: {"name": "Осквернённый паладин", "letters": 19, "time": 19, "hits": 3, "combos": 2},
    17: {"name": "Древний дракон", "letters": 20, "time": 20, "hits": 2, "combos": 2},
    18: {"name": "Титан Бездны", "letters": 21, "time": 22, "hits": 2, "combos": 2},

    19: {"name": "Архидемон", "letters": 22, "time": 23, "hits": 2, "combos": 2},
    20: {"name": "Палач душ", "letters": 23, "time": 24, "hits": 1, "combos": 2},
    21: {"name": "Лорд Погибели", "letters": 24, "time": 26, "hits": 1, "combos": 2},
    22: {"name": "Первородная Чума", "letters": 25, "time": 27, "hits": 1, "combos": 2},
    23: {"name": "Бессмертный лич", "letters": 26, "time": 28, "hits": 1, "combos": 5, "text": "Его живучесть крайне высока."},
    24: {"name": "Лорд Стихий", "letters": 27, "time": 29, "hits": 1, "combos": 2},

    25: {"name": "Истинный Левиафан", "letters": 28, "time": 29, "hits": 1, "combos": 2},
    26: {"name": "Владыка Бездны", "letters": 30, "time": 32, "hits": 1, "combos": 2},
    27: {"name": "Владыка Хаоса", "letters": 32, "time": 34, "hits": 1, "combos": 2},
    28: {"name": "Разрушитель небес", "letters": 34, "time": 36, "hits": 1, "combos": 2},
    29: {"name": "Конец времён", "letters": 36, "time": 38, "hits": 1, "combos": 2},
    30: {"name": "Пожиратель миров", "letters": 40, "time": 42, "hits": 1, "combos": 2},

    31: {"name": "Апостол разработчика", "letters": 26, "time": 28, "hits": 1, "combos": 10, "lets_for_change": 10, "time_for_change": 21}
}


base_length = 31
base_time = 33
base_hits = 2
base_combos = 3
# режимы букв и цифр


# режим слов
monsters_w = {
    1: {"name": "Слизень", "letters": 2, "time": 5, "hits": 5, "combos": 2},
    2: {"name": "Змей Детёныш", "letters": 2, "time": 5, "hits": 5, "combos": 3},
    3: {"name": "Гнилой волк", "letters": 3, "time": 7, "hits": 5, "combos": 3},
    4: {"name": "Пещерный паук", "letters": 3, "time": 6, "hits": 5, "combos": 3},
    5: {"name": "Костяной воин", "letters": 4, "time": 9, "hits": 5, "combos": 3},
    6: {"name": "Берсерк", "letters": 5, "time": 11, "hits": 5, "combos": 3, "text": "Он обладает повышенным шансом впасть в ярость."},

    7: {"name": "Проклятый рыцарь", "letters": 5, "time": 11, "hits": 4, "combos": 4},
    8: {"name": "Грозовой Змей", "letters": 5, "time": 11, "hits": 4, "combos": 3},
    9: {"name": "Кровавый шаман", "letters": 5, "time": 11, "hits": 4, "combos": 5},
    10: {"name": "Демон", "letters": 6, "time": 13, "hits": 4, "combos": 3},
    11: {"name": "Безликий", "letters": 6, "time": 13, "hits": 3, "combos": 4},
    12: {"name": "Адский зверь", "letters": 7, "time": 15, "hits": 3, "combos": 4},

    13: {"name": "Пожиратель плоти", "letters": 6, "time": 13, "hits": 3, "combos": 5},
    14: {"name": "Костяной гигант", "letters": 5, "time": 11, "hits": 4, "combos": 4},
    15: {"name": "Чернокнижник бездны", "letters": 5, "time": 11, "hits": 4, "combos": 3},
    16: {"name": "Осквернённый паладин", "letters": 8, "time": 17, "hits": 3, "combos": 4},
    17: {"name": "Древний дракон", "letters": 8, "time": 17, "hits": 3, "combos": 5},
    18: {"name": "Титан Бездны", "letters": 8, "time": 16, "hits": 3, "combos": 5},

    19: {"name": "Архидемон", "letters": 9, "time": 19, "hits": 3, "combos": 4},
    20: {"name": "Палач душ", "letters": 8, "time": 16, "hits": 3, "combos": 3},
    21: {"name": "Лорд Погибели", "letters": 10, "time": 21, "hits": 3, "combos": 3},
    22: {"name": "Первородная Чума", "letters": 10, "time": 21, "hits": 2, "combos": 4},
    23: {"name": "Бессмертный лич", "letters": 10, "time": 21, "hits": 3, "combos": 7, "text": "Его живучесть крайне высока."},
    24: {"name": "Истинный Левиафан", "letters": 10, "time": 20, "hits": 2, "combos": 4},

    25: {"name": "Лорд Стихий", "letters": 11, "time": 23, "hits": 2, "combos": 4},
    26: {"name": "Владыка Бездны", "letters": 11, "time": 23, "hits": 2, "combos": 4},
    27: {"name": "Владыка Хаоса", "letters": 11, "time": 23, "hits": 2, "combos": 4},
    28: {"name": "Разрушитель небес", "letters": 12, "time": 25, "hits": 1, "combos": 5},
    29: {"name": "Конец времён", "letters": 13, "time": 27, "hits": 1, "combos": 5},
    30: {"name": "Пожиратель миров", "letters": 15, "time": 31, "hits": 1, "combos": 6},

    31: {"name": "Апостол разработчика", "letters": 10, "time": 21, "hits": 1, "combos": 10, "lets_for_change": 26, "time_for_change": 28}
}


base_length_w = 11
base_time_w = 22
base_hits_w = 2
base_combos_w = 5
# режим слов


items = {
    "Ярость берсерка": "Источник ярости берсерка. При использовании наполняет владельца яростью, увеличивая шанс критического удара в бою.",
    "Сердце лича": "Тёмный магический кристалл, вырванный из сущности древнего лича. Сохраняет остатки его бессмертной силы. При использовании дарует владельцу одну дополнительную жизнь против любого монстра.",
    "Алебарда Разрушителя": "Оружие, в котором заключена мощь Разрушителя небес, его прежнего владельца. При использовании уменьшает максимальное количество жизней врага на 1.",
    "Вельзевул": "Древний клинок, некогда принадлежавший Пожирателю Миров. При использовании в режимах букв и цифр он пожирает 3 символа из комбинации, а в режиме слов - 1 слово из последовательности."
}


achievements = {

    "убить_первого_монстра": {
        "text": "Победите своего первого монстра.",
        "achiev": "Первая кровь",
        "status": False
    },

    "впервые_спастись_бегством": {
        "text": "Впервые спаситесь бегством из боя.",
        "achiev": "Выживший",
        "status": False
    },

    "спастись_бегством_10_раз": {
        "text": "Спаситесь бегством 10 раз.",
        "achiev": "Неуловимый",
        "status": False
    },

    "погибнуть_впервые": {
        "text": "Погибните впервые.",
        "achiev": "Цена ошибки",
        "status": False
    },

    "погибнуть_10_раз": {
        "text": "Погибните 10 раз.",
        "achiev": "Побеждён, но не сломлен",
        "status": False
    },

    "получить_первый_предмет": {
        "text": "Получите свой первый предмет.",
        "achiev": "Первая добыча",
        "status": False
    },

    "собрать_все_предметы": {
        "text": "Соберите все доступные предметы.",
        "achiev": "Коллекционер реликвий",
        "status": False
    },

    "победить_монстра_без_урона": {
        "text": "Победите монстра, не получив урона.",
        "achiev": "Недосягаемый",
        "status": False
    },

    "пережить_ярость_монстра": {
        "text": "Переживите первую ярость монстра.",
        "achiev": "Хладнокровие",
        "status": False
    },

    "использовать_первый_предмет": {
        "text": "Используйте предмет из инвентаря.",
        "achiev": "Сила артефакта",
        "status": False
    },


    # титулы
    "достичь_ранга_ученик": {
        "text": "Победите Берсерка и докажите, что способны пережить свою первую настоящую охоту.",
        "achiev": "Ученик",
        "status": False
    },

    "достичь_ранга_охотник": {
        "text": "Одолейте Адского зверя и заслужите право называться настоящим охотником.",
        "achiev": "Охотник",
        "status": False
    },

    "достичь_ранга_элитный_каратель": {
        "text": "Сразите Титана Бездны - исполина, чьи шаги сотрясают землю, а появление предвещает гибель целых поселений.",
        "achiev": "Элитный каратель",
        "status": False
    },

    "достичь_ранга_инквизитор": {
        "text": "Победите Истинного Левиафана - древнего владыку глубин, чьё пробуждение веками считалось предвестником конца света.",
        "achiev": "Инквизитор",
        "status": False
    },

    "достичь_ранга_немезида": {
        "text": "Уничтожьте Пожирателя Миров - существо, перед которым меркнут даже легенды. После этой победы вам больше нечего доказывать.",
        "achiev": "Немезида",
        "status": False
    },
    # титулы

}


duel = {
    "Слизень": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Змей Детёныш": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Гнилой волк": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Пещерный паук": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Костяной воин": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Берсерк": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Проклятый рыцарь": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Грозовой Змей": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Кровавый шаман": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Демон": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Безликий": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Адский зверь": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Пожиратель плоти": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Костяной гигант": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Чернокнижник бездны": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Осквернённый паладин": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Древний дракон": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Титан Бездны": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Архидемон": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Палач душ": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Лорд Погибели": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Первородная Чума": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Бессмертный лич": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Лорд Стихий": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Истинный Левиафан": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Владыка Бездны": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Владыка Хаоса": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Разрушитель небес": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Конец времён": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Пожиратель миров": {
        "right_duel": "0",
        "best_seria_duel": "0"
    },
    "Апостол разработчика": {
        "right_duel": "0",
        "best_seria_duel": "0"
    }
}


angl_words = [
    "apple", "archer", "artifact", "assassin", "asteroid", "avatar",
    "backpack", "bandit", "barrier", "battle", "beacon", "beast",
    "berserker", "blade", "blizzard", "bomber", "book", "bridge",
    "brother", "builder", "bullet", "captain", "castle", "cavern",
    "centaur", "champion", "chaos", "charger", "citadel", "claw",
    "cleric", "cloud", "commander", "compass", "contract", "crystal",
    "cyclone", "dagger", "defender", "demon", "desert", "destroyer",
    "diamond", "dragon", "dream", "druid", "dungeon", "eagle",
    "element", "emperor", "engineer", "explorer", "falcon", "fantom",
    "farmer", "fighter", "fireball", "forest", "fortress", "frost",
    "galaxy", "gate", "general", "ghost", "giant", "gladiator",
    "goblin", "guardian", "hammer", "harpoon", "hawk", "helmet",
    "hero", "hunter", "hurricane", "illusion", "invader", "island",
    "jungle", "keeper", "king", "knight", "kraken", "labyrinth",
    "legend", "mage", "magnet", "market", "master", "meteor",
    "mirror", "monarch", "monster", "mountain", "mystic", "necromancer",
    "nomad", "observer", "ocean", "oracle", "outlaw", "paladin",
    "phantom", "phoenix", "pilot", "pirate", "planet", "portal",
    "priest", "prince", "prisoner", "projectile", "protector", "python",
    "queen", "ranger", "ravager", "reaper", "relic", "robot",
    "rogue", "ruins", "samurai", "scholar", "scorpion", "sentinel",
    "shadow", "shield", "ship", "sniper", "soldier", "sorcerer",
    "spear", "spirit", "storm", "summoner", "sword", "temple",
    "thief", "throne", "tiger", "titan", "torch", "tower",
    "traveler", "treasure", "tribe", "troll", "vampire", "vault",
    "viking", "villager", "volcano", "voyager", "warlock", "warrior",
    "watcher", "weapon", "whisper", "wizard", "wolf", "wraith",
    "zephyr", "zombie",
    "airship", "alchemist", "ambush", "anvil", "arena", "arctic",
    "armory", "arrow", "ascension", "ash", "astronaut", "awakening",
    "bastion", "behemoth", "blacksmith", "bladeguard", "bloodstone",
    "bounty", "camp", "canyon", "caravan", "catapult", "cave",
    "celestial", "coalition", "comet", "conquest", "corsair", "coven",
    "crossbow", "crow", "crusader", "curse", "cyborg", "darkness",
    "dawn", "deity", "delta", "doom", "drake", "earthquake",
    "ember", "enigma", "expedition", "exile", "faction", "fate",
    "forge", "glacier", "horizon" "abyss", "adventurer", "alchemy", "alliance", "anchor", "android",
    "antidote", "apocalypse", "apprentice", "armada", "assault", "barrage",
    "bestiary", "blight", "brigade", "cataclysm", "chronicle", "clan",
    "collision", "colossus", "combat", "corruption", "cosmos", "creature",
    "crimson", "crypt", "darklord", "deadwood", "defense", "delusion",
    "desolation", "disaster", "dominion", "echo", "empire", "eruption",
    "eternity", "executioner", "experiment", "fable", "fury", "garrison",
    "grimoire", "harvest", "haunt", "hydra", "iceberg", "impact",
    "incursion", "inferno"
]


russ_words = [
    "абзац", "автобус", "автомат", "агент", "адрес", "азарт", "академик",
    "алмаз", "алтарь", "ананас", "ангел", "аппарат", "арбуз", "аромат",
    "архив", "астероид", "асфальт", "аэродром", "багаж", "балкон",
    "банкир", "барьер", "бассейн", "батарея", "башня", "бедняк", "билет",
    "бинокль", "блокнот", "богатырь", "болт", "борец", "ботинок",
    "браслет", "бриллиант", "бронежилет", "будильник", "букет", "буран",
    "буфер", "вагон", "валун", "варвар", "ведьмак", "вектор", "великан",
    "венец", "верстак", "ветеран", "взрыв", "викинг", "виноград",
    "витязь", "вихрь", "властелин", "водопад", "воин", "волшебник",
    "ворон", "восход", "всадник", "выстрел", "гладиатор", "гном",
    "город", "гранит", "грифон", "гром", "дворец", "дворник", "демон",
    "дирижабль", "диск", "доспех", "дракон", "дробовик", "друид",
    "дым", "еж", "жрец", "завод", "закат", "замок", "зверь", "звон",
    "зеркальце", "знак", "змей", "зомби", "идеал", "изумруд", "инженер",
    "испытатель", "кабан", "кадет", "камень", "капитан", "карман",
    "картограф", "каскад", "кентавр", "кинжал", "кирпич", "клинок",
    "клоун", "князь", "ковчег", "кодекс", "колокол", "командир",
    "компас", "конструктор", "контракт", "король", "космос", "костёр",
    "котёл", "кракен", "кристалл", "кузнец", "купол", "лабиринт",
    "лазер", "легендарь", "лекарь", "лесник", "лидер", "лифт", "лучник",
    "маг", "магнит", "мастер", "медальон", "метеор", "меч", "министр",
    "молот", "монолит", "монстр", "мореплаватель", "мост", "мудрец",
    "мушкетёр", "наблюдатель", "наёмник", "небоскрёб", "некромант",
    "обелиск", "оборотень", "огонь", "океан", "оракул", "орк", "охотник",
    "паладин", "памятник", "парус", "паук", "пекарь", "пергамент",
    "перстень", "пират", "пистолет", "пленник", "повелитель", "подземелье",
    "полководец", "портал", "посох", "предатель", "призрак", "принц",
    "проводник", "проект", "прыжок", "путник", "разведчик", "разлом",
    "рейнджер", "робот", "рудник", "рыбак", "рыцарь", "самурай",
    "сапфир", "свиток", "сектор", "серп", "скиталец", "склеп",
    "скорпион", "следопыт", "слиток", "снайпер", "советник", "солдат",
    "сосуд", "спутник", "страж", "странник", "сундук", "сфера",
    "талисман", "танк", "творец", "текст", "телепорт", "титан",
    "топор", "торнадо", "трактир", "тролль", "туман", "убийца",
    "уголь", "удар", "узник", "ураган", "факел", "фантом", "ферзь",
    "флот", "фонарь", "хищник", "храм", "цветок", "целитель", "цирк",
    "чародей", "череп", "чертёж", "шаман", "шахтёр", "шедевр",
    "щит", "эксперимент", "элемент", "эликсир", "эпизод", "ювелир",
    "яд", "якорь", "ящер",
    "абрикос", "аврора", "аквариум", "аккорд", "аккумулятор", "алфавит", "анкер", "апельсин",
    "аптека", "арена", "архитектор", "ассистент", "атлас", "аукцион", "баллада", "барабан",
    "берег", "берёза", "библиотека", "блюдо", "бриз", "броня", "бутылка", "бюро",
    "ваза", "вальс", "вершина", "весна", "вещь", "вулкан", "галактика", "гармония",
    "гитара", "гравитация", "груша", "губернатор", "долина", "дождь", "документ",
    "дуб", "ежевика", "журнал", "здание", "золото", "игла", "икона", "индикатор",
    "ирис", "история"
]
