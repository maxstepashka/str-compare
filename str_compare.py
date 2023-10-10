def compare(str1, str2, required_procent, **kwargs):

    number = 0
    true = 0
    false = 0

    # перевод строк в списки
    str1 = list(str1)
    str2 = list(str2)

    # уравнивание списков по длине
    if len(str1) > len(str2):
        for i in range(len(str1) - len(str2)):
            str2.append(" ")

    if len(str2) > len(str1):
        for i in range(len(str2) - len(str1)):
            str1.append(" ")

    lenght = len(str1)

    # подсчёт количества совпадающих и несовпадающих символов
    for i in range(lenght):
        if str1[number] == str2[number]:
            true += 1

        else:
            false += 1

        number += 1

    # вычисление процента совпадения
    procent = 100 / lenght * true
    if procent >= required_procent:
        return True
    else:
        return False