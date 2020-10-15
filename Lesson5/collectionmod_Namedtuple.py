# Именованные кортежи придают значение каждой позиции в кортеже и обеспечивают
# более читаемый, самодокументирующийся код. Их можно использовать везде, где
# используются обычные кортежи, и они добавляют возможность доступа к полям по
# имени вместо индекса позиции.

from collections import namedtuple, OrderedDict


hero_1 = ('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_1[4])

class Person:

    def __init__(self, name, race, health, mana, strenght):
        self.name = name
        self.race = race
        self.health = health
        self.mana = mana
        self.strenght = strenght

hero_2 = Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_2.strenght)


New_Person = namedtuple('New_Person', 'name, race, health, mana, sterenght')
hero_3 = New_Person('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_3.mana)

prop = ['name', 'race', 'health', 'mana', 'sterenght']
New_Person1 = namedtuple('New_Person1', prop)
hero_4 = New_Person1('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_4.race)


New_Person2 = namedtuple('New_Person2', 'name race health mana sterenght')
hero_5 = New_Person2('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_5.name)

prop1 = ['name', '3race', 'health', '_mana', 'sterenght'] # используем недопустимые типы имен
New_Person3 = namedtuple('New_Person3', prop1, rename=True)
hero_6 = New_Person3('Aaz', 'Izverg', 100, 0.0, 250)
print(hero_6)

print('*' * 50)
Point = namedtuple('Point', 'x, y, z')
p1 = Point(2, z=3, y=4)
print(p1)

# сохраним список, который будет хранить координаты точки, а затем, на его основе
# построим эту точку
print('*' * 50)
t = [5, 10, 15]
p2 = Point._make(t)
print(p2)

# преобразуем namedtuple в OrderedDict(в версии 3,7 и ниже)
print('*' * 50)
d2 = p2._asdict()
print(d2)
print(type(d2))

# преобразуем namedtuple в OrderedDict в версии 3,8
print('*' * 50)
d3 = OrderedDict(p2._asdict())
print(d3)

# замена значений
print('*' * 50)
p3 = p2._replace(x=6)
print(p3)

# просмотр полей кортежа
print('*' * 50)
print(p3._fields)

# добавление значений по умолчанию(начиная с 3,7)
print('*' * 50)
New_Point = namedtuple('New_Point', 'x, y, z', defaults=[0, 0])
p4 = New_Point(5)
print(p4)

# просмотр значений по умолчанию
print('*' * 50)
print(p4._field_defaults)

# создание namedtuple на основе словаря
print('*' * 50)
dct = {'x': 5, 'y': 410, 'z': 15}
p5 = New_Point(**dct)
print(p5)
