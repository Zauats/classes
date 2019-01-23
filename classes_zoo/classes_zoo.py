import random
class Animals:
    eat = 'голодные'
    name = ''
    weight = 1 #кг

    def feeding(self):
        set


class Bird(Animals):
    ball = random.randrange(10) + 1 #яйца
    say = 'Цып-цып'

    def collection(self):
        egg_collection = input('У какой птицы собрать яйцы? У Ко-Ко, Кукареку или Кряква? ')
        if egg_collection == 'Ко-Ко':
            print('У Ко-Ко вы собрали {} яиц'.format(chicken_co.ball))
        elif egg_collection == 'Кукареку':
            print('У Ко-Ко вы собрали {} яиц'.format(chicken_ku.ball))
        elif egg_collection == 'Кряква':
            print('У Ко-Ко вы собрали {} яиц'.format(duck.ball))
        else:
            print('Сегодня яиц нет!')

chicken_co = Bird()
chicken_co.name = 'Ко-Ко'
chicken_co.weight = 5


chicken_ku = Bird()
chicken_ku.name = 'Кукареку'
chicken_ku.weight = 3

duck = Bird()
duck.name = 'Кряква'
duck.weight = 3
duck.say = 'Кря-Кря'


class Brute(Animals):
    milk = random.randrange(7) + 1
    say = 'Бееее'


cow = Brute()
cow.name = 'Манька'
cow.weight = 70
cow.say = 'Мууууу'

horns = Brute()
horns.name = 'Рога'
horns.weight = '10'

hooves = Brute()
hooves.name = 'Копыта'
hooves.weight = 11


class Sheep(Animals):
    wool = random.randrange(3) + 1
    say = 'Беееее'

lamb = Sheep()
lamb.name = 'Барашек'
lamb.weight = 8

curly = Sheep()
curly.name = 'Кудрявый'
lamb.weight = 6

lamb.feeding()