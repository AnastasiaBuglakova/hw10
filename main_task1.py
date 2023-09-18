# Задание
# Решить задачи, которые не успели решить на семинаре.
# Доработаем задачи 5-6. Создайте класс-фабрику.
# ○ Класс принимает тип животного (название одного из созданных классов) и параметры для этого типа.
# ○ Внутри класса создайте экземпляр на основе переданного типа и верните его из класса-фабрики.
# Возьмите 1-3 любые задачи из прошлых семинаров (например сериализация данных), которые вы уже решали.
# Превратите функции в методы класса, а параметры в свойства. Задачи должны решаться через вызов методов экземпляра.

class Animal:

    def __init__(self, **kwargs):
        print('a')
        self.kwargs = kwargs
        print(f'{self=}', self.kwargs)

    def get_special(self):
        return self.kwargs


class Dog(Animal):

    def __init__(self, cl: str, **kwargs):
        if cl == 'dog':
            self.word = 'gav'
            super().__init__(kwargs.get('breet', None))


class Cat(Animal):

    def __init__(self, cl: str, **kwargs):
        if cl == 'cat':
            print('it is cat')
            print('from cat init', kwargs.get('color', None))
            self.word = 'myau'
            super().__init__(kwargs.get('color', None))


class Fish(Animal):

    def __init__(self, cl: str, **kwargs):
        if cl == 'fish':
            print('it is fish')
            super().__init__(kwargs.get('habitat', None))
            self.word = 'bul'


class Fabric(Fish, Cat, Dog):
    """Fabric documentation."""

    def __init__(self, name, age, **kwargs):
        self.name = name
        self.age = age
        self.cl = kwargs['cl']
        self.kwargs = kwargs
        self.kwargs.pop('cl')
        super().__init__(self.cl, **kwargs)


citty = Fabric('bow', 4, cl='cat', color='pink')
yo = Fabric('taily', 1, cl='fish', habitat='silver')
mitty = Fabric('fee', 6, cl='cat', color='white')
print(f'{mitty.cl=}, {mitty.name=},{mitty.age=},  {mitty.get_special() = }')
print(f'{yo.cl=}, {yo.name=},{yo.age=},  {yo.get_special()}, {yo.word=}')

print(f'____> {citty.__dict__ = }')
help(Fabric)
