import tkinter
import quiz
import importlib
import os
import settings as s
from PIL import ImageTk, Image


# Объявление глобальных переменных
frames_dict = {}

# Стили для размещения элементов интерфейса
opts = {'sticky': 'nsew'}


def create_menu(frame: tkinter.Frame, tests_dict: dict) -> None:
    """
    Создает меню для окна приложения.

    Аргументы:
        frame (tkinter.Frame): Фрейм, в котором будет создано меню.
        tests_dict (dict): Словарь с тестами.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Создает меню с пунктом "Файл" и подменю "Темы", в котором находятся пункты тестов из словаря `tests_dict`.
        - Добавляет пункт "Выход" в меню "Файл".
        - Привязывает команду `quit_app` к пункту "Выход".
        - Добавляет созданное меню к фрейму `frame`.
    """
    menubar = tkinter.Menu(frame,)
    frame.config(menu=menubar)
    file_menu = tkinter.Menu(menubar, tearoff=0,)
    submenu = tkinter.Menu(file_menu, tearoff=0,)
    create_submenu_items(submenu, tests_dict)
    file_menu.add_cascade(label="Темы", menu=submenu, underline=0)
    file_menu.add_separator()
    file_menu.add_command(label="Выход", underline=0, command=quit_app)
    menubar.add_cascade(label="Файл", underline=0, menu=file_menu)
    frames_dict["globalFrame"].config(menu=menubar)


def create_submenu_items(menu: tkinter.Menu, tests_dict: dict) -> tkinter.Menu:
    """
    Создает подпункты меню для выбора теста.

    Аргументы:
        menu (tkinter.Menu): Меню, в котором будут создаваться подпункты.
        tests_dict (dict): Словарь с тестами.

    Возвращает:
        menu (tkinter.Menu): Меню с добавленными подпунктами.

    Исключения:
        None

    Побочные эффекты:
        - Создает подпункты меню для каждого теста из словаря `tests_dict`.
        - Привязывает каждый подпункт к функции `start_new_quiz` с аргументом `test`, взятым из словаря `tests_dict`.
        - Возвращает меню с добавленными подпунктами.
    """
    for test_file, test_info in tests_dict.items():
        print("test_name", test_file, "test_info", test_info)
        menu.add_command(label=test_info["name_theme"],
                         command=lambda test=test_info["test"]: start_new_quiz(test))
    return menu


def start_new_quiz(test: dict) -> None:
    """
    Запускает новый квиз, используя заданный тест.

    Аргументы:
        test (dict): Тест, из которого будут взяты вопросы.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Вызывает функцию `create_quiz_settings` для создания настроек квиза.
        - Выводит последовательность вопросов на экран.
        - Запускает новый квиз с первым вопросом по последовательности.
    """
    sequence_of_questions = quiz.create_quiz_settings(test)
    print(sequence_of_questions)
    current_sequence = 0
    next_question(test, current_sequence, sequence_of_questions)


def next_question(test: dict, current_sequence: int, sequence_of_questions: list) -> None:
    """
    Переходит к следующему вопросу в квизе.

    Аргументы:
        test (dict): Тест, из которого будут взяты вопросы.
        current_sequence (int): Текущая последовательность вопроса.
        sequence_of_questions (list): Последовательность вопросов в квизе.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Выводит текущую последовательность вопроса и длину последовательности на экран.
        - Если текущая последовательность меньше длины последовательности, вызывает функции `drawing_area_quest_frame`,
        `drawing_empty_area_explanation_frame` и `create_answer_buttons` для отображения следующего вопроса.
        - В противном случае вызывает функцию `question_end`.
    """
    print("current_sequence", current_sequence)
    print("len(sequence_of_questions)", len(sequence_of_questions))
    print("sequence_of_questions", sequence_of_questions)
    if current_sequence < len(sequence_of_questions):
        drawing_area_quest_frame(test, current_sequence, sequence_of_questions)
        drawing_empty_area_explanation_frame()
        create_answer_buttons(test, current_sequence, sequence_of_questions)
    else:
        question_end()


def drawing_area_quest_frame(test: dict, current_sequence: int, sequence_of_questions: list) -> None:
    """
    Отображает фрейм с вопросом в текущем квизе.

    Аргументы:
        test (dict): Тест, из которого будет взят вопрос.
        current_sequence (int): Текущая последовательность вопроса.
        sequence_of_questions (list): Последовательность вопросов в квизе.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Очищает фрейм `frames_dict["questFrame"]`.
        - Получает текущий вопрос из словаря `test` по последовательности `sequence_of_questions`.
        - Создает текстовое поле `question_fill` для отображения вопроса.
        - Заполняет текстовое поле `question_fill` текстом вопроса и номером вопроса в квизе.
        - Размещает текстовое поле `question_fill` в фрейме `frames_dict["questFrame"]`.
        - Настраивает внешний вид текстового поля `question_fill`.
    """
    clear((frames_dict["questFrame"],))
    question = test[sequence_of_questions[current_sequence]]
    text = f"Вопрос {current_sequence + 1} из {len(sequence_of_questions)}"
    question_fill = tkinter.Text(frames_dict["questFrame"], wrap="word")
    question_fill.insert("1.0", text + "\n\n" + question['question'])
    question_fill.grid(row=1, column=0, padx=10, pady=50)
    question_fill.configure(font=("Tahoma", 12, "bold"), fg="#E0E0E0", bg="#252525", borderwidth=0, state="disabled")


def drawing_empty_area_explanation_frame() -> None:
    """
    Отображает пустой фрейм для объяснения ответа.

    Аргументы:
        None

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Очищает фрейм `frames_dict["explanationFrame"]`.
        - Создает текстовое поле `explanation` для отображения объяснения ответа.
        - Размещает текстовое поле `explanation` в фрейме `frames_dict["explanationFrame"]`.
        - Настраивает внешний вид текстового поля `explanation`.
    """
    clear((frames_dict["explanationFrame"],))
    explanation = tkinter.Text(frames_dict["explanationFrame"], font=20, state='disabled', bg=s.bg_fon, borderwidth=0)
    explanation.grid(row=0, column=0, **opts)


def drawing_area_explanation_frame(test: dict, current_sequence: int, sequence_of_questions: list) -> None:
    """
    Отображает фрейм с объяснением ответа для текущего вопроса в квизе.

    Аргументы:
        test (dict): Тест, из которого будет взят вопрос.
        current_sequence (int): Текущая последовательность вопроса.
        sequence_of_questions (list): Последовательность вопросов в квизе.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Очищает фрейм `frames_dict["explanationFrame"]`.
        - Получает текущий вопрос из словаря `test` по последовательности `sequence_of_questions`.
        - Создает текстовое поле `explanation` для отображения объяснения ответа.
        - Заполняет текстовое поле `explanation` текстом объяснения ответа.
        - Размещает текстовое поле `explanation` в фрейме `frames_dict["explanationFrame"]`.
        - Настраивает внешний вид текстового поля `explanation`.
        - Увеличивает `current_sequence` на 1.
        - Создает кнопку "Следующий вопрос", которая вызывает функцию `next_question` при нажатии.
        - Размещает кнопку "Следующий вопрос" в фрейме `frames_dict["explanationFrame"]`.
    """
    clear((frames_dict["explanationFrame"],))
    question = test[sequence_of_questions[current_sequence]]
    explanation = tkinter.Text(frames_dict["explanationFrame"], bg=s.bg_fon, borderwidth=0, )
    text = "ПОЯСНЕНИЕ:\n\n"
    explanation.insert("1.0", text + question["explanation"], )
    explanation.grid(row=0, column=0, **opts)
    explanation.configure(font=("Tahoma", 13, "bold"), fg="#E0E0E0", wrap="word", state="disabled")

    # Загрузка и вставка изображения
    if question.get("image"):
        try:
            # Открываем и подготавливаем изображение
            img = Image.open(question["image"])
            img = img.resize((800, 500), Image.Resampling.LANCZOS)
            photo = ImageTk.PhotoImage(img)

            # Вставляем изображение после текста
            explanation.image_create("end", image=photo)

            # Добавляем перенос строки после изображения
            explanation.insert("end", "\n\n")

            # Сохраняем ссылку на изображение
            explanation.photo = photo

        except Exception as e:
            print(f"Ошибка загрузки изображения: {e}")

    current_sequence += 1
    next_btn = tkinter.Button(frames_dict["explanationFrame"], text="Следующий вопрос", )
    next_btn.configure(font=("tahoma", 12, "bold"), fg="#E0E0E0", bg="#454545", width=1000, height=3)
    next_btn.bind("<Button-1>", lambda event, answer="answer_1", question=question:
                  next_question(test, current_sequence, sequence_of_questions))
    next_btn.grid(row=1, column=0, sticky="s")


def result(text: str) -> None:
    """
    Отображает фрейм с результатом.

    Аргументы:
        text (str): Текст результата.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Очищает фрейм `frames_dict["questFrame"]`.
        - Создает текстовое поле `text_fill` для отображения результата.
        - Заполняет текстовое поле `text_fill` текстом результата.
        - Настраивает внешний вид текстового поля `text_fill`.
        - Размещает текстовое поле `text_fill` в фрейме `frames_dict["questFrame"]`.
        - Очищает фрейм `frames_dict["answerFrame"]`.
    """
    text_fill = tkinter.Text(frames_dict["questFrame"], font=20)
    text_fill.configure(font=("tahoma", 12, "bold"),)
    text_fill.insert("1.0", text)
    text_fill.configure(font=("Tahoma", 12, "bold"), fg="#E0E0E0", bg=s.bg_fon, borderwidth=0, state="disabled")
    text_fill.grid(row=0, column=0, padx=40, pady=100)
    clear((frames_dict["answerFrame"],))


def question_end() -> None:
    """
    Отображает фрейм с сообщением о завершении вопросов.

    Аргументы:
        None

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Очищает фреймы `frames_dict["questFrame"]`, `frames_dict["answerFrame"]` и `frames_dict["explanationFrame"]`.
        - Создает текстовое поле `text` для отображения сообщения о завершении вопросов.
        - Заполняет текстовое поле `text` текстом "Вопросы закончились".
        - Настраивает внешний вид текстового поля `text`.
        - Размещает текстовое поле `text` в фрейме `frames_dict["questFrame"]`.
        - Создает кнопку "Посмотреть результаты", которая вызывает функцию `quiz.rate_test` при нажатии.
        - Размещает кнопку "Посмотреть результаты" в фрейме `frames_dict["answerFrame"]`.
    """
    clear((frames_dict["questFrame"], frames_dict["answerFrame"], frames_dict["explanationFrame"],))
    text = tkinter.Text(frames_dict["questFrame"])
    text.insert("1.0", 'Вопросы закончились')
    text.configure(font=("Tahoma", 12, "bold"), fg="#E0E0E0", bg=s.bg_fon, borderwidth=0, state="disabled")

    check_btn = tkinter.Button(frames_dict["answerFrame"], text="Посмотреть результаты", command=quiz.rate_test)
    check_btn.grid(row=0, column=0, **opts)
    text.grid(row=0, column=0, padx=10, pady=50, **opts)


def create_answer_buttons(test: dict, current_sequence: int, sequence_of_questions: list, disabled=False) -> tuple:
    """
    Создает кнопки ответов для текущего вопроса в квизе.

    Аргументы:
        test (dict): Тест, из которого будет взят вопрос.
        current_sequence (int): Текущая последовательность вопроса.
        sequence_of_questions (list): Последовательность вопросов в квизе.
        disabled (bool, optional): Флаг, указывающий, должны ли кнопки быть отключенными. По умолчанию `False`.

    Возвращает:
        Кнопки ответов.

    Исключения:
        None

    Побочные эффекты:
        - Очищает фрейм `frames_dict['answerFrame']`.
        - Получает текущий вопрос из словаря `test` по последовательности `sequence_of_questions`.
        - Создает кнопки ответов для каждого из возможных ответов на вопрос.
        - Настраивает внешний вид кнопок ответов.
        - Привязывает обработчики событий к кнопкам ответов, которые вызывают функцию `quiz.check_answer` при нажатии.
        - Возвращает созданные кнопки ответов.
    """
    clear((frames_dict['answerFrame'],))
    state = "normal" if not disabled else "disabled"
    question = test[sequence_of_questions[current_sequence]]

    btn_1 = create_answer_button(frames_dict['answerFrame'], question['answer_1'], state, row=0)
    btn_2 = create_answer_button(frames_dict['answerFrame'], question['answer_2'], state, row=1)
    btn_3 = create_answer_button(frames_dict['answerFrame'], question['answer_3'], state, row=2)
    btn_4 = create_answer_button(frames_dict['answerFrame'], question['answer_4'], state, row=3)
    btn_5 = create_answer_button(frames_dict['answerFrame'], question['answer_5'], state, row=4)

    if state == "normal":
        btn_1.bind("<Button-1>", lambda event, answer="answer_1", question=question:
                   quiz.check_answer(answer, question, test, current_sequence, sequence_of_questions))
        btn_2.bind("<Button-1>", lambda event, answer="answer_2", question=question:
                   quiz.check_answer(answer, question, test, current_sequence, sequence_of_questions))
        btn_3.bind("<Button-1>", lambda event, answer="answer_3", question=question:
                   quiz.check_answer(answer, question, test, current_sequence, sequence_of_questions))
        btn_4.bind("<Button-1>", lambda event, answer="answer_4", question=question:
                   quiz.check_answer(answer, question, test, current_sequence, sequence_of_questions))
        btn_5.bind("<Button-1>", lambda event, answer="answer_5", question=question:
                   quiz.check_answer(answer, question, test, current_sequence, sequence_of_questions))

    return btn_1, btn_2, btn_3, btn_4, btn_5


def create_answer_button(frame: tkinter.Frame, text: str, state, row: int) -> tkinter.Button:
    """
    Создает кнопку ответа.

    Аргументы:
        frame (tkinter.Frame): Фрейм, в котором будет создана кнопка.
        text (str): Текст кнопки.
        state (str): Состояние кнопки (normal или disabled).
        command (function): Команда, выполняемая при нажатии кнопки.
    """
    button = tkinter.Button(frame, text=text, state=state, wraplength=frame.winfo_width()-200, width=5000)
    button.configure(font=("Tahoma", 12, "bold"), fg="#E0E0E0", bg="#1C1C1C")
    opts = {"pady": 3, "sticky": 's'}
    button.grid(row=row, column=0, **opts)
    return button


def create_list_of_themes() -> list:
    """
    Создает список тем из файлов в папке "tests".

    Возвращает:
        list: Список тем без расширения файла.

    Исключения:
        None

    Побочные эффекты:
        - Получает список файлов в папке "tests".
        - Удаляет расширение файла из каждого имени файла в списке.
        - Возвращает список тем без расширения файла.
    """
    files = os.listdir("tests")
    files_without_extension = []
    for i in files:
        if i.endswith(".py"):
            files_without_extension.append(i[:-3])
    return files_without_extension


def import_tests(files: list) -> dict:
    """
    Импортирует тесты из файлов в папке "tests".

    Аргументы:
        files (list): Список файлов в папке "tests".

    Возвращает:
        dict: Словарь, где ключи - это имена файлов без расширения, а значения - словари с информацией о тесте.
        Каждый словарь содержит ключи "name_theme" и "test", где "name_theme" - это название темы,
        а "test" - это словарь с вопросами.

    Исключения:
        None

    Побочные эффекты:
        - Импортирует каждый файл из папки "tests" с помощью `importlib.import_module`.
        - Извлекает название темы и словарь вопросов из каждого импортированного модуля.
        - Сохраняет информацию о тесте в словаре `tests`.
        - Возвращает словарь `tests`.
    """
    tests = {}
    for file in files:
        name_file = f"tests.{file}"
        import_file = importlib.import_module(name_file)
        name_theme = import_file.name_theme
        questions = import_file.questions_dict
        tests[file] = {"name_theme": name_theme, "test": questions}
    return tests


def quit_app(frame: tkinter.Frame):
    """
    Закрывает указанный фрейм.

    Аргументы:
        frame (tkinter.Frame): Фрейм, который нужно закрыть.

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Закрывает указанный фрейм.
    """
    frame.destroy()


def clear(frames: tuple):
    """
    Очищает все виджеты в указанных фреймах.

    Аргументы:
        frames (tuple): Кортеж фреймов, которые нужно очистить.

    Возвращает:
        bool: `True`, если очистка успешно завершена.

    Исключения:
        None

    Побочные эффекты:
        - Очищает все виджеты в каждом из указанных фреймов.
        - Возвращает `True`, если очистка успешно завершена.
    """
    for frame in frames:
        for widget in frame.winfo_children():
            widget.destroy()
    return True
