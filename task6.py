# Дан следующий словарь, представляющий инвентарь персонажа игры:
inventory = {
    'золото' : 500,
    'кошель' : ['алмаз', 'брильянт', 'самоцвет'],
    'сумка' : ['ксилофон', 'кинжал', 'спальный мешок', 'буханка хлеба']
}
# Проделайте следующие модификации со словарём inventory, используя операторы и методы классов dict и list:

# добавьте ключ с названием "карман"; по ключу "карман" сохраните список, 
# содержащи й следующие строки: "ракушки", "ягода" и "платок"
# отсортируйте список, хранящийся по ключу сумка
# удалите "кинжал" из списка, который хранится по ключу "сумка"
# добавьте 50 к числу, которое хранится по ключу "золото"
# Выведите на экран обновлённый словарь inventory.

inventory['карман'] = ["ракушки", "ягода", "платок"]

inventory['сумка'].remove('кинжал')

inventory["золото"] = inventory["золото"] + 50



print(inventory)
