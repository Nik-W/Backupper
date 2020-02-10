#комментарии в оба файла, укоротить код, тесты и отлов ошибок. Сообщение о успешной архивации
#посмотреть про доступные методы архивирование, сделать выбор метода
#изучить os что бы внешние каталоги не архивировались 
#

import os, time, zipfile, path

# 1. Файлы и каталоги, которые необходимо скопировать, собираются в список.
# source = ['E:\\Code Dev\\py\\Backupper', 'E:\\Code Dev\\py\\Project Euler']
# Заметьте, что для имён, содержащих пробелы, необходимо использовать
# двойные кавычки внутри строки.
#source = path.source[:]

# 2. Резервные копии должны храниться в основном каталоге резерва.
#target_dir = 'E:\\Code Dev\\py' # Подставьте тот путь, который вы будете использовать.
def Conversion_path(str):
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

source = []
for s in path.source:
    source.append(Conversion_path(s))
#print (source)
target_dir = Conversion_path(path.target_dir)

# 3. Файлы помещаются в zip-архив.
# 4. Текущая дата служит именем подкаталога в основном каталоге
today = target_dir + os.sep + time.strftime('%d-%m-%Y')
# Текущее время служит именем zip-архива
now = time.strftime('%H.%M.%S')

# Запрашиваем комментарий пользователя для имени файла
comment = input('Введите комментарий --> ')
if len(comment) == 0: # проверяем, введён ли комментарий
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '(' + \
    comment.replace(' ', '_') + ').zip'

# Создаём каталог, если его ещё нет
if not os.path.exists(today):
    os.mkdir(today) # создание каталога
print('Каталог успешно создан', today)

# 5. Создание архива
zip = zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) 
#Архивирование всех файлов каталога
for s in source:
    for root, dirs, files in os.walk(s): # Список всех файлов и папок в директории folder
        for file in files:
            zip.write(os.path.join(root,file))
            print(os.path.join(root,file)) 
            
zip.close()

'''
# Запускаем создание резервной копии
if os.system(zip_command) == 0:
    print('Резервная копия успешно создана в', target)
else:
    print('Создание резервной копии НЕ УДАЛОСЬ')
'''


