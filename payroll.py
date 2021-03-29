def is_valid(num):
    if num.isdigit():
        return True
    else:
         return False


def payroll():
    while True:
        employees_count = input('Количество сотрудников в смене: ')
        if is_valid(employees_count):
            employees_count = int(employees_count)
            break
        else:
            print('Нужно ввести чило!')

    while True:
        sum_tire = input('Касса по шиномонтажу: ')
        if is_valid(sum_tire):
            sum_tire = int(sum_tire)
            break
        else:
            print('Нужно ввести чило!')
    
    while True:
        sum_service = input('Касса по сервису: ')
        if is_valid(sum_service):
            sum_service = int(sum_service)
            break
        else:
            print('Нужно ввести чило!')

    total = (sum_tire * 0.30 / employees_count) + (sum_service * 0.40 / employees_count)
    print('зарплата за этот день', total)
    lst.append(total)
    print('общая сумма за все дни', sum(lst))
    proceed = input('Продолжить подсчет? Y/N').lower()
    if proceed == 'y':
        payroll()
    recording = input('Записать данные? Y/N ').lower()
    if recording == 'y':
        ch = input('введите дату (день/месяц) за какое число был расчет: ')
        s = open('C:\\Users\\User\\Desktop\\payroll.txt', 'a')
        s.write(str(ch))
        s.write('-')
        s.write(str(lst[0]))
        s.write('\n')
        s.close()
        input('press any key for exit')

lst = []
payroll()
