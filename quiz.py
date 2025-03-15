from random import choice
import app_functions
from typing import List


# Объявление глобальных переменных
valid_answers = 0
invalid_answers = 0


def shuffle_questions(quantity: int) -> List[int]:
    """
    Генерирует случайную последовательность номеров вопросов для квиза.

    Аргументы:
        quantity (int): Количество вопросов в квизе.

    Возвращает:
        sequence_of_questions (list): Случайная последовательность номеров вопросов.

    Исключения:
        None

    Побочные эффекты:
        - Создает пустой список для хранения последовательности вопросов.
        - Создает список с номерами вопросов.
        - Перемешивает список номеров вопросов.
        - Добавляет выбранный номер вопроса в последовательность.
        - Возвращает сгенерированную случайную последовательность номеров вопросов.
    """
    # Инициализируем пустой список для хранения последовательности вопросов
    sequence_of_questions = []

    # Создаем список с номерами вопросов
    lst = list(range(quantity))

    # Перемешиваем список номеров вопросов
    for _ in range(quantity):
        # Выбираем случайный номер вопроса из списка
        num_of_question = choice(lst)
        # Удаляем выбранный номер вопроса из списка
        lst.remove(num_of_question)
        # Добавляем выбранный номер вопроса в последовательность
        sequence_of_questions.append(num_of_question)

    # Возвращаем сгенерированную случайную последовательность номеров вопросов
    return sequence_of_questions


def rate_test():
    """
    Вычисляет оценку теста на основе количества правильных и неправильных ответов и выводит результат.

    Аргументы:
        None

    Возвращает:
        None

    Исключения:
        None

    Побочные эффекты:
        - Вычисляет оценку теста, используя количество правильных и неправильных ответов.
        - Выводит результат теста с помощью функции `result` из модуля `app_functions`.
    """
    grade = calculate_grade(valid_answers, invalid_answers)
    text = f"Правильных ответов: {valid_answers}\n\n" \
           f"НЕ правильных ответов: {invalid_answers}\n\n" \
           f"Твоя оценка: {grade}"

    app_functions.result(text)


def calculate_grade(valid_answers, invalid_answers):
    """
    Вычисляет оценку на основе количества правильных и неправильных ответов.

    Параметры:
        valid_answers (int): Количество правильных ответов.
        invalid_answers (int): Количество неправильных ответов.

    Возвращает:
        str: Оценка на основе процентного соотношения правильных ответов.
            - "Отлично" если процент правильных ответов больше или равен 90.
            - "Хорошо" если процент правильных ответов находится в диапазоне от 80 до 90.
            - "Трояк" если процент правильных ответов находится в диапазоне от 70 до 80.
            - "Это даже на 2 не тянет" если процент правильных ответов находится в диапазоне от 60 до 70.
            - "На кол тебя!" в противном случае.
    """
    total_answers = valid_answers + invalid_answers
    percentage = valid_answers / total_answers * 100

    if percentage >= 90:
        return "Отлично"
    elif 80 <= percentage < 90:
        return "Хорошо"
    elif 70 <= percentage < 80:
        return "Трояк"
    elif 60 <= percentage < 70:
        return "Это даже на 2 не тянет"
    else:
        return "На кол тебя!"


def check_answer(answer, question, test, current_sequence, sequence_of_questions):
    """
    Проверяет, соответствует ли предоставленный ответ правильному ответу на вопрос.

    Аргументы:
        answer (str): Ответ, предоставленный пользователем.
        question (dict): Вопрос, который проверяется.
        test (dict): Тест, который проходит.
        current_sequence (int): Текущий номер последовательности вопроса.
        sequence_of_questions (list): Последовательность вопросов в тесте.

    Возвращает:
        bool: True, если ответ правильный, в противном случае - False.

    Исключения:
        None

    Побочные эффекты:
        - Увеличивает счетчик `valid_answers`, если ответ правильный.
        - Увеличивает `current_sequence`, если ответ правильный.
        - Вызывает функцию `next_question` из модуля `app_functions` с обновленными `current_sequence`
        и `sequence_of_questions`, если ответ правильный.

        - Отключает кнопки ответа, если ответ неправильный.
        - Увеличивает счетчик `invalid_answers`, если ответ неправильный.
        - Вызывает функцию `drawing_area_explanation_frame` из модуля `app_functions` с обновленными `current_sequence`
        и `sequence_of_questions`, если ответ неправильный.
    """
    if question["valid"] == answer:
        add_valid_answers()
        current_sequence += 1
        app_functions.next_question(test, current_sequence, sequence_of_questions)
    else:
        app_functions.create_answer_buttons(test, current_sequence, sequence_of_questions, disabled=True)
        add_invalid_answers()
        app_functions.drawing_area_explanation_frame(test, current_sequence, sequence_of_questions)
    return True


def add_valid_answers():
    """
    Изменяет глобальную переменную `valid_answers`.

    Исключения:
        None

    Побочные эффекты:
        - Увеличивает счетчик `valid_answers`, если ответ правильный (check_answer).
    """
    global valid_answers
    valid_answers += 1


def add_invalid_answers():
    """
    Изменяет глобальную переменную `invalid_answers`.

    Исключения:
        None

    Побочные эффекты:
        - Увеличивает счетчик `invalid_answers`, если ответ НЕ правильный (check_answer).
    """
    global invalid_answers
    invalid_answers += 1


def rest_global_values():
    """
    Сбрасывает значения глобальных переменных `sequence_of_questions`, `questions`, `current_seq_of_question`,
    `valid_answers` и `invalid_answers`.

    Эта функция устанавливает значения этих глобальных переменных в `None`, `0`, `0` и `0` соответственно.
    Она используется для сброса состояния программы перед началом нового теста или викторины.

    Параметры:
        None

    Возвращает:
        None
    """
    global valid_answers, invalid_answers
    valid_answers = 0
    invalid_answers = 0
    return True


def create_quiz_settings(test_questions):
    """
    Создает настройки квиза, используя заданные вопросы теста.

    Аргументы:
        test_questions (list): Список вопросов для теста.

    Возвращает:
        sequence_of_questions (list): Случайно перемешанная последовательность вопросов для квиза.

    Исключения:
        None

    Побочные эффекты:
        - Очищает глобальные значения, используемые в quiz.py.
        - Перемешивает список вопросов в случайном порядке.
    """
    rest_global_values()
    sequence_of_questions = shuffle_questions(len(test_questions))
    return sequence_of_questions
