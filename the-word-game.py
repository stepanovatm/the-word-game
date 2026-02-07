countwords = 0
iitog = ''
ccount = 0
itog = ''
count = 0
words = {'огород', 'самолёт', 'компьютер', 'собака', 'поляна', 'скрепка', 'деревня', 'библиотека', 'природа', 'алфавит', 'поместье',\
                 'животное', 'археология', 'бабушка', 'документ', 'словосочетание', 'велосипед', 'автомобиль', 'аэропорт', 'аквариум'}
print('Здравствуйте!')
print('Вы бы хотели сыграть в игру?(Если хотите, то напишите "да", если не хотите - "нет".)')
otvet = input()
if otvet == 'да':
    while otvet == 'да' and countwords <= 20:
        countwords += 1
        print('Введите любую цифру от 15 до 33 включительно.')
        chislo = int(input())
        if chislo < 15 or chislo > 33:
            print('Ошибка! Введите число ещё раз, убедившись, что оно удовлетворяет условию.')
            chislo = int(input())
        word = words.pop()
        print(f'Пишите все буквы в этой игре с маленькой буквы. Правила: я загадываю слово и вывожу сколько в нём букв звёздочками({len(word)} букв). Вы пишете букву.')
        print(f'Если эта буква есть в слове, то вместо звёздочек я вывожу её. У Вас есть столько попыток, какое Вы ввели число({chislo} попыток.).')
        print('*' * len(word))
        bukva = input()
        while count < chislo:
            count += 1
            if itog == word:
                break
            iitog = itog
            itog = ''
            for i in word:
                if i == bukva:
                    ccount += 1
                    itog += i
                elif i in iitog:
                    itog += i
                else:
                    itog += '*'
            if itog == word:
                break
            if ccount != 0:
                print(f'{itog}. У Вас осталось {chislo - count} опыток(-ки).')
            else:
                print(f'Этой буквы нет в этом слове. У Вас осталось {chislo - count} попыток(-ки).')
            ccount = 0
            bukva = input()
        if itog == word:
            print(f'Здорово! Вы отгадали слово.({word})')
        else:
            print(f'К сожалению, у Вас не получилось отгадать слово. Это было слово "{word}".')
        itog = ''
        iitog = ''
        count = 0
        print('Вы бы хотели повторно сыграть в эту игру?(Если хотите, то напишите "да", если не хотите - "нет".)')
        otvet = input()
print('До свидания!')
