# Основная логика программы

<<<<<<< HEAD
#from log import add2log
#import view_module
#import io_module
=======
from log import add2log
#import view_module
import io_module
>>>>>>> data

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
<<<<<<< HEAD
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
=======
    io_module.save_db(phones)

def _exportcsv(phone_list): # Делаем экпорт в csv
    io_module.export_csv(phone_list)

def _exporttxt(phone_list): # Делаем экпорт в txt
    io_module.export_txt(phone_list)

def _exportjson(phone_list): # Делаем экпорт в json
    io_module.export_json(phone_list)

def _importjson(phone_list): # Импорт из json файла
    return io_module.import_json(phone_list)
>>>>>>> data

def controller(): # Главный цикл

    phone_list = init() # Считываем всю базу из файла

<<<<<<< HEAD
    while True: 
        inp = input('>>> ')

=======
    while True:
        inp = input('>>> ')
        add2log(inp,'>') # Записываем в журнал все, что вводят
>>>>>>> data
        match inp.lower(): # парсим то, что пользователь навводил
            case '/help': _help()
            case '/info': _info()
            case '/exit': break
            case '/quit': break
<<<<<<< HEAD
            case _ :
                print('Неверная команда. Для помощи наберите /help')
=======

            case '/save':
                _save(phone_list)
                print('Данные записаны на диск')
            case '/exportcsv':
                _exportcsv(phone_list)
            case '/exporttxt':
                _exporttxt(phone_list)
            case '/exportjson':
                _exportjson(phone_list)
            case '/importjson':
                phone_list = _importjson(phone_list)
            case _ :
                print('Неверная команда. Для помощи наберите /help')
    _save(phone_list)
>>>>>>> data
    print('Выход из программы.')

