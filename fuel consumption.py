price=float(input('Введите цену бензина:'))
mile=float(input('Введите расстояние которое собираетесь проехать:'))
avto=float(input('Введите средний расход топлива автомобиля на 100км:'))
a = price * avto
b = mile / 100 * a
litr = mile / 100 * avto
print('цена за 100км составит: ', a)
print('бензин выйдет на сумму:', b)
print('литров затрачено:', litr)
input('Нажмите Enter для выхода')
