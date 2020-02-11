#комментарии в оба файла, укоротить код, тесты и отлов ошибок. Сообщение о успешной архивации
#посмотреть про доступные методы архивирование, сделать выбор метода - не поддерживаются!
#изучить os что бы внешние каталоги не архивировались (os.walk(s), os.chdir(s), print(os.getcwd()) - улучшение на будущее
#файлы не архивируются, для архивации файлов, убедиться, что это файл (у него будет .расширение) и записать отдельно

import os, time, zipfile, path

def Conversion_path(str):
    '''Преобразование путей в поддерживаемые .py'''
    start = 0
    end = 0
    STR = ""
    while end != -1:
        end = str.find('\\',start)
        if end != -1:
            STR += str[start:end] + "\\"
        else:
            STR += str[start:]
        start = end + 1
    return STR

#получение путей
source = []
for s in path.source:
    source.append(Conversion_path(s))
target_dir = Conversion_path(path.target_dir)

#интерфейс
Start = input ("Для создания резервных копий каталогов в {} введите 1: ".format(target_dir))
if Start != "1": exit(0)
print("Выбранные вами каталоги:")
for s in source:
    print(s)
print()

today = target_dir + os.sep + "BackUp(" + time.strftime('%d-%m-%Y') + ")" #имя каталога
now = time.strftime('%H.%M.%S') #имя архива без комментария

#Комментарий 
comment = input('Введите комментарий или ничего: ')
if len(comment) == 0: #если нет комментария
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '(' + \
    comment.replace(' ', '_') + ').zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)

try:
    #Создание архива
    zip = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) 
    #Архивирование всех файлов выбранных каталогов
    for s in source:
        for root, dirs, files in os.walk(s): # Список всех файлов и папок в директории
            for file in files:
                zip.write(os.path.join(root,file))  
    zip.close()
except: print('Создание резервной копии НЕ УДАЛОСЬ')
else: 
    print('Резервная копия успешно создана в', target) 



'''
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
'''


