import tkinter
import app_functions
import settings

# Создание главного окна приложения
global_frame = tkinter.Tk()

# Вычисление ширины и высоты окна
width = global_frame.winfo_screenwidth()
width = width - width // 10
height = global_frame.winfo_screenheight()
height = height - height // 10

# Настройка главного окна
global_frame.title("Тесты")  # Задание заголовка окна
global_frame.geometry(f'{width}x{height}')  # Установка размеров окна
global_frame.resizable(False, False)  # Запрет изменения размеров окна
global_frame.configure(bg=settings.bg_fon)

# Настройка колонок в главном окне
global_frame.grid_columnconfigure(0, weight=1)  # Настройка колонки 0
global_frame.grid_columnconfigure(1, weight=1)  # Настройка колонки 1

# Настройка строк в главном окне
global_frame.grid_rowconfigure(0, weight=1)  # Настройка строки 0

# Создание фреймов для размещения элементов интерфейса
quizFrame = tkinter.Frame(global_frame, bg=settings.bg_fon)
questFrame = tkinter.Frame(quizFrame, bg=settings.bg_fon)
answerFrame = tkinter.Frame(quizFrame, bg=settings.bg_fon)
explanationFrame = tkinter.Frame(global_frame, bg=settings.bg_fon)

# Размещение фреймов в главном окне
quizFrame.grid(row=0, column=0, **settings.opts_frame)  # Размещение фрейма quizFrame
explanationFrame.grid(row=0, column=1, **settings.opts_frame)  # Размещение фрейма explanationFrame
questFrame.grid(row=0, column=0, **settings.opts_frame)  # Размещение фрейма questFrame
answerFrame.grid(row=1, column=0, **settings.opts_frame)  # Размещение фрейма answerFrame

# Настройка колонок в фрейме quizFrame
quizFrame.grid_columnconfigure(0, weight=1)  # Настройка колонки 0

# Настройка строк в фрейме quizFrame
quizFrame.grid_rowconfigure(0, weight=1)  # Настройка строки 0
quizFrame.grid_rowconfigure(1, weight=1)  # Настройка строки 1


questFrame.grid_columnconfigure(0, weight=1)
questFrame.grid_rowconfigure(0, weight=1)

answerFrame.grid_columnconfigure(0, weight=1)
answerFrame.grid_rowconfigure(0, weight=1)

explanationFrame.grid_columnconfigure(0, weight=1)
explanationFrame.grid_rowconfigure(0, weight=1)
explanationFrame.grid_rowconfigure(1, weight=1)

global_frame.grid_propagate(False)
quizFrame.grid_propagate(False)
questFrame.grid_propagate(False)
answerFrame.grid_propagate(False)
explanationFrame.grid_propagate(False)


app_functions.frames_dict = {'globalFrame': global_frame, 'quizFrame': quizFrame, 'questFrame': questFrame,
                             'answerFrame': answerFrame, 'explanationFrame': explanationFrame}


def run() -> None:
    """
        Запускает приложение.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Создает список тем из файлов в папке "tests".
        - Импортирует тесты из файлов в папке "tests".
        - Создает меню с темами из импортированных тестов.
        - Запускает главный цикл приложения.
    """
    files = app_functions.create_list_of_themes()
    tests_dict = app_functions.import_tests(files)
    app_functions.create_menu(global_frame, tests_dict)

    global_frame.mainloop()
