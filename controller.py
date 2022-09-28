# Основная логика программы

#from log import add2log
#import view_module
#import io_module

def init(): # Приветствие, и загрузка данных
    pass

def _help():
    print('Обрабатываются следующие команды:')
    print('\t /help - вывод помощи')
    print('\t /info - вывод информации о программе')
    print('\t /exit или /quit - выход из программы')
    print('\t /list - вывод списка телефонов')
    print('\t /add  - добавить новый телефон')
    print('\t /edit - редактировать телефон')
    print('\t /del  - удалить телефон')
    print('\t /save - принудительно сохранить базу в файл')
    print('\t /exportcsv  - экспорт базы в csv формате')
    print('\t /exporttxt  - экспорт базы в txt формате')
    print('\t /exportjson  - экспорт базы в json формате')
    print('\t /importjson  - импорт базы из формата json')

def _info():
    print('Программа - телефонный справочник.')
    print('Выполнена в качестве командного домашнего задания')

def _save(phones): # Сохраняем в файл всю базу
    pass

def _list(phones): # Выводим на экран всю базу
    pass

def _del(): # Возвращаем номер записи к удалению
    pass

def _get_edit_idx(): # Возвращаем номер записи к редактированию
    pass

def _exportcsv(phone_list): # Делаем экпорт в csv
    pass

def _exporttxt(phone_list): # Делаем экпорт в txt
    pass

def _exportjson(phone_list): # Делаем экпорт в json
    pass

def _importjson(phone_list): # Импорт из json файла
    pass

def controller(): # Главный цикл

    phone_list = init() # Считываем всю базу из файла

    while True: 
        inp = input('>>> ')

        match inp.lower(): # парсим то, что пользователь навводил
            case '/help': _help()
            case '/info': _info()
            case '/exit': break
            case '/quit': break
            case _ :
                print('Неверная команда. Для помощи наберите /help')
    print('Выход из программы.')

