name_theme = "Пользовательские функции (в разработке)"
questions_dict = {
    0: {
        "question": "Что такое функция в Python?",
        "answer_1": "Это блок кода, который выполняет одну задачу.",
        "answer_2": "Это тип данных.",
        "answer_3": "Это переменная.",
        "answer_4": "Это условие.",
        "answer_5": "Это метод.",
        "valid": "answer_1",
        "explanation": "Функция — это блок кода, который можно вызывать для выполнения определенной задачи."
    },
    1: {
        "question": "Как правильно объявить функцию в Python?",
        "answer_1": "function my_function():",
        "answer_2": "def my_function():",
        "answer_3": "create my_function():",
        "answer_4": "my_function() =>",
        "answer_5": "define my_function():",
        "valid": "answer_2",
        "explanation": "Для объявления функции в Python используется ключевое слово 'def'."
    },
    2: {
        "question": "Какой синтаксис используется для возврата значения из функции?",
        "answer_1": "return value;",
        "answer_2": "return value",
        "answer_3": "yield value",
        "answer_4": "send value",
        "answer_5": "output value",
        "valid": "answer_2",
        "explanation": "Ключевое слово 'return' используется для возврата значения из функции."
    },
    3: {
        "question": "Что такое обязательные параметры функции?",
        "answer_1": "Параметры, которые могут быть пропущены.",
        "answer_2": "Параметры, которые должны быть переданы при вызове функции.",
        "answer_3": "Параметры, которые по умолчанию равны None.",
        "answer_4": "Параметры, которые не могут быть изменены.",
        "answer_5": "Все параметры функции.",
        "valid": "answer_2",
        "explanation": "Обязательные параметры должны быть переданы при вызове функции, иначе возникнет ошибка."
    },
    4: {
        "question": "Какой из следующих параметров является необязательным?",
        "answer_1": "def my_function(x):",
        "answer_2": "def my_function(x=10):",
        "answer_3": "def my_function(*args):",
        "answer_4": "def my_function(**kwargs):",
        "answer_5": "Все параметры являются обязательными.",
        "valid": "answer_2",
        "explanation": "Параметр x=10 является необязательным, так как ему присвоено значение по умолчанию."
    },
    5: {
        "question": "Как правильно вызвать функцию с передачей аргументов?",
        "answer_1": "my_function()",
        "answer_2": "my_function(10)",
        "answer_3": "my_function(x=10)",
        "answer_4": "my_function(10, 20)",
        "answer_5": "Все вышеперечисленные.",
        "valid": "answer_5",
        "explanation": "Все перечисленные способы являются правильными для вызова функции с аргументами."
    },
    6: {
        "question": "Какой будет вывод следующего кода: 'def add(a, b): return a + b; print(add(2, 3))'?",
        "answer_1": "5",
        "answer_2": "23",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция add() возвращает сумму 2 и 3, что равно 5."
    },
    7: {
        "question": "Что такое метод в Python?",
        "answer_1": "Это функция, связанная с объектом.",
        "answer_2": "Это глобальная функция.",
        "answer_3": "Это переменная.",
        "answer_4": "Это тип данных.",
        "answer_5": "Это условие.",
        "valid": "answer_1",
        "explanation": "Метод — это функция, которая вызывается в контексте объекта."
    },
    8: {
        "question": "Какой из следующих вариантов является правильным способом определения функции с переменным количеством аргументов?",
        "answer_1": "def my_function(*args):",
        "answer_2": "def my_function(args*):",
        "answer_3": "def my_function(args):",
        "answer_4": "def my_function(...):",
        "answer_5": "def my_function(**args):",
        "valid": "answer_1",
        "explanation": "Для определения функции с переменным количеством позиционных аргументов используется *args."
    },
    9: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): return \"Hello, \" + name; print(greet(\"Alice\"))'?",
        "answer_1": "Hello, Alice",
        "answer_2": "Hello, Bob",
        "answer_3": "Hello,",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция greet() возвращает строку 'Hello, Alice'."
    },
    10: {
        "question": "Какой будет результат выполнения следующего кода: 'def square(x): return x * x; print(square(4))'?",
        "answer_1": "16",
        "answer_2": "8",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция square() возвращает квадрат числа 4, что равно 16."
    },
    11: {
        "question": "Что такое возврат значения в функции?",
        "answer_1": "Это завершение функции.",
        "answer_2": "Это передача данных из функции обратно в вызывающий код.",
        "answer_3": "Это вызов другой функции.",
        "answer_4": "Это создание новой функции.",
        "answer_5": "Это изменение параметров функции.",
        "valid": "answer_2",
        "explanation": "Возврат значения позволяет передать результат выполнения функции обратно в вызывающий код."
    },
    12: {
        "question": "Какой будет вывод следующего кода: 'def func(): return; print(func())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция func() возвращает None, поэтому вывод будет None."
    },
    13: {
        "question": "Какой метод используется для создания документации функции?",
        "answer_1": "\"\"\"...",
        "answer_2": "doc()",
        "answer_3": "help()",
        "answer_4": "info()",
        "answer_5": "comments()",
        "valid": "answer_1",
        "explanation": "Документация функции создается с помощью строк документации (docstring), заключенных в тройные кавычки."
    },
    14: {
        "question": "Какой из следующих вариантов является неправильным именем функции?",
        "answer_1": "my_function",
        "answer_2": "MyFunction",
        "answer_3": "myFunction1",
        "answer_4": "1myFunction",
        "answer_5": "my_function_2",
        "valid": "answer_4",
        "explanation": "Имена функций не могут начинаться с цифры."
    },
    15: {
        "question": "Какой результат выполнения следующего кода: 'def add(a=5, b=10): return a + b; print(add())'?",
        "answer_1": "15",
        "answer_2": "10",
        "answer_3": "5",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция add() использует значения по умолчанию, поэтому результатом будет 5 + 10 = 15."
    },
    16: {
        "question": "Какой результат выполнения следующего кода: 'def multiply(a, b=2): return a * b; print(multiply(3))'?",
        "answer_1": "6",
        "answer_2": "3",
        "answer_3": "5",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция multiply() умножает 3 на значение по умолчанию 2, что равно 6."
    },
    17: {
        "question": "Какой будет вывод следующего кода: 'def my_func(): return; my_func(); print(my_func())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция my_func() ничего не возвращает, поэтому вывод будет None."
    },
    18: {
        "question": "Какой из следующих параметров является необязательным?",
        "answer_1": "def my_function(x):",
        "answer_2": "def my_function(x=10):",
        "answer_3": "def my_function(*args):",
        "answer_4": "def my_function(**kwargs):",
        "answer_5": "Все параметры являются обязательными.",
        "valid": "answer_2",
        "explanation": "Параметр x=10 является необязательным, так как ему присвоено значение по умолчанию."
    },
    19: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): return \"Hello, \" + name; print(greet(\"Alice\"))'?",
        "answer_1": "Hello, Alice",
        "answer_2": "Hello, Bob",
        "answer_3": "Hello,",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция greet() возвращает строку 'Hello, Alice'."
    },
    20: {
        "question": "Какой будет результат выполнения следующего кода: 'def square(x): return x * x; print(square(4))'?",
        "answer_1": "16",
        "answer_2": "8",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция square() возвращает квадрат числа 4, что равно 16."
    },
    21: {
        "question": "Какой из следующих операторов используется для передачи аргументов по позициям?",
        "answer_1": "args",
        "answer_2": "*args",
        "answer_3": "**args",
        "answer_4": "args[]",
        "answer_5": "arguments",
        "valid": "answer_2",
        "explanation": "Оператор *args используется для передачи переменного количества позиционных аргументов."
    },
    22: {
        "question": "Какой метод используется для создания документации функции?",
        "answer_1": "\"\"\"...",
        "answer_2": "doc()",
        "answer_3": "help()",
        "answer_4": "info()",
        "answer_5": "comments()",
        "valid": "answer_1",
        "explanation": "Документация функции создается с помощью строк документации (docstring), заключенных в тройные кавычки."
    },
    23: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(x, y): return x + y; print(add(2, 3))'?",
        "answer_1": "5",
        "answer_2": "23",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция add() возвращает сумму 2 и 3, что равно 5."
    },
    24: {
        "question": "Какой будет вывод следующего кода: 'def my_function(a, b=10): return a + b; print(my_function(5))'?",
        "answer_1": "15",
        "answer_2": "5",
        "answer_3": "10",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция my_function() использует значение по умолчанию для b, поэтому 5 + 10 = 15."
    },
    25: {
        "question": "Какой будет вывод следующего кода: 'def my_func(): return; print(my_func())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция my_func() ничего не возвращает, поэтому вывод будет None."
    },
    26: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): print(\"Hello, \" + name); greet(\"Alice\")'?",
        "answer_1": "Hello, Alice",
        "answer_2": "Hello,",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "Hello, 0",
        "valid": "answer_1",
        "explanation": "Функция greet() выводит строку 'Hello, Alice'."
    },
    27: {
        "question": "Что произойдет, если вызвать функцию, не передав обязательные параметры?",
        "answer_1": "Ошибка TypeError.",
        "answer_2": "Вернется None.",
        "answer_3": "Функция выполнится без параметров.",
        "answer_4": "Вернется 0.",
        "answer_5": "Ошибка SyntaxError.",
        "valid": "answer_1",
        "explanation": "Если не передать обязательные параметры, возникнет ошибка TypeError."
    },
    28: {
        "question": "Какой из следующих параметров является необязательным?",
        "answer_1": "def my_function(x):",
        "answer_2": "def my_function(x=10):",
        "answer_3": "def my_function(*args):",
        "answer_4": "def my_function(**kwargs):",
        "answer_5": "Все параметры являются обязательными.",
        "valid": "answer_2",
        "explanation": "Параметр x=10 является необязательным, так как ему присвоено значение по умолчанию."
    },
    29: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(): return 42; print(func())'?",
        "answer_1": "42",
        "answer_2": "Ошибка",
        "answer_3": "None",
        "answer_4": "0",
        "answer_5": "42.0",
        "valid": "answer_1",
        "explanation": "Функция func() возвращает значение 42."
    },
    30: {
        "question": "Какой будет результат выполнения следующего кода: 'def multiply(a, b): return a * b; print(multiply(2, 3))'?",
        "answer_1": "6",
        "answer_2": "5",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция multiply() возвращает произведение 2 и 3, что равно 6."
    },
    31: {
        "question": "Какой будет результат выполнения следующего кода: 'def my_function(a, b=2): return a + b; print(my_function(3))'?",
        "answer_1": "5",
        "answer_2": "3",
        "answer_3": "2",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция my_function() возвращает сумму 3 и значения по умолчанию 2, что равно 5."
    },
    32: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(x, y): return x + y; print(add(5))'?",
        "answer_1": "Ошибка",
        "answer_2": "5",
        "answer_3": "None",
        "answer_4": "0",
        "answer_5": "10",
        "valid": "answer_1",
        "explanation": "Функция add() требует два аргумента, и если передан только один, возникнет ошибка."
    },
    33: {
        "question": "Какой результат выполнения следующего кода: 'def func(a, b): return a - b; print(func(5, 3))'?",
        "answer_1": "2",
        "answer_2": "8",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция func() возвращает разность 5 и 3, что равно 2."
    },
    34: {
        "question": "Какой будет результат выполнения следующего кода: 'def print_message(message): print(message); print_message(\"Hello\")'?",
        "answer_1": "Hello",
        "answer_2": "Hello\nHello",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "Hello, 0",
        "valid": "answer_1",
        "explanation": "Функция print_message() выводит переданное сообщение 'Hello'."
    },
    35: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): return f\"Hello, {name}\"; print(greet(\"Bob\"))'?",
        "answer_1": "Hello, Bob",
        "answer_2": "Hello,",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "Hello, 0",
        "valid": "answer_1",
        "explanation": "Функция greet() возвращает строку 'Hello, Bob'."
    },
    36: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(a=1, b=2): return a + b; print(add())'?",
        "answer_1": "3",
        "answer_2": "1",
        "answer_3": "2",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция add() использует значения по умолчанию, поэтому результатом будет 1 + 2 = 3."
    },
    37: {
        "question": "Какой будет результат выполнения следующего кода: 'def my_func(): return; my_func(); print(my_func())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция my_func() ничего не возвращает, поэтому вывод будет None."
    },
    38: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(a, b=2): return a + b; print(func(3))'?",
        "answer_1": "5",
        "answer_2": "3",
        "answer_3": "2",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция func() возвращает сумму 3 и значения по умолчанию 2, что равно 5."
    },
    39: {
        "question": "Какой будет результат выполнения следующего кода: 'def square(x): return x * x; print(square(4))'?",
        "answer_1": "16",
        "answer_2": "8",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция square() возвращает квадрат числа 4, что равно 16."
    },
    40: {
        "question": "Какой будет результат выполнения следующего кода: 'def multiply(a, b=1): return a * b; print(multiply(5))'?",
        "answer_1": "5",
        "answer_2": "6",
        "answer_3": "10",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция multiply() умножает 5 на значение по умолчанию 1, поэтому результат будет 5."
    },
    41: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(): return; print(func())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция func() ничего не возвращает, поэтому вывод будет None."
    },
    42: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): print(\"Hello, \" + name); greet(\"Alice\")'?",
        "answer_1": "Hello, Alice",
        "answer_2": "Hello,",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "Hello, 0",
        "valid": "answer_1",
        "explanation": "Функция greet() выводит строку 'Hello, Alice'."
    },
    43: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(x, y): return x + y; print(add(5, 10))'?",
        "answer_1": "15",
        "answer_2": "5",
        "answer_3": "10",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция add() возвращает сумму 5 и 10, что равно 15."
    },
    44: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(a=1, b=2): return a + b; print(func(b=3))'?",
        "answer_1": "4",
        "answer_2": "3",
        "answer_3": "1",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция func() использует значение b=3 и значение по умолчанию для a, поэтому результат будет 1 + 3 = 4."
    },
    45: {
        "question": "Какой будет результат выполнения следующего кода: 'def divide(a, b): return a / b; print(divide(6, 2))'?",
        "answer_1": "3.0",
        "answer_2": "3",
        "answer_3": "4",
        "answer_4": "2",
        "answer_5": "Ошибка",
        "valid": "answer_1",
        "explanation": "Функция divide() возвращает результат деления 6 на 2, что равно 3.0."
    },
    46: {
        "question": "Какой будет результат выполнения следующего кода: 'def repeat(string, times): return string * times; print(repeat(\"Hello\", 3))'?",
        "answer_1": "HelloHelloHello",
        "answer_2": "HelloHello",
        "answer_3": "Hello, Hello, Hello",
        "answer_4": "Ошибка",
        "answer_5": "None","valid": "answer_1",
        "explanation": "Функция repeat() повторяет строку 'Hello' три раза, возвращая 'HelloHelloHello'."
    },
    47: {
        "question": "Какой будет результат выполнения следующего кода: 'def get_max(a, b): return a if a > b else b; print(get_max(5, 10))'?",
        "answer_1": "10",
        "answer_2": "5",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция get_max() возвращает максимальное значение между 5 и 10, то есть 10."
    },
    48: {
        "question": "Какой будет результат выполнения следующего кода: 'def calculate_area(radius): return 3.14 * radius ** 2; print(calculate_area(2))'?",
        "answer_1": "12.56",
        "answer_2": "6.28",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция calculate_area() вычисляет площадь круга с радиусом 2, возвращая 3.14 * 4 = 12.56."
    },
    49: {
        "question": "Какой будет результат выполнения следующего кода: 'def print_list(my_list): for item in my_list: print(item); print_list([1, 2, 3])'?",
        "answer_1": "1\n2\n3",
        "answer_2": "123",
        "answer_3": "[1, 2, 3]",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция print_list() выводит каждый элемент списка, поэтому вывод будет 1, 2, 3."
    },
    50: {
        "question": "Какой будет результат выполнения следующего кода: 'def my_function(): return; print(my_function())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция my_function() ничего не возвращает, поэтому вывод будет None."
    },
    51: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): return f\"Hello, {name}\"; print(greet(\"Alice\"))'?",
        "answer_1": "Hello, Alice",
        "answer_2": "Hello,",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "Hello, 0",
        "valid": "answer_1",
        "explanation": "Функция greet() возвращает строку 'Hello, Alice'."
    },
    52: {
        "question": "Какой будет результат выполнения следующего кода: 'def square(x): return x * x; print(square(4))'?",
        "answer_1": "16",
        "answer_2": "8",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция square() возвращает квадрат числа 4, что равно 16."
    },
    53: {
        "question": "Какой результат выполнения следующего кода: 'def add(a, b): return a + b; print(add(2, 3))'?",
        "answer_1": "5",
        "answer_2": "23",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция add() возвращает сумму 2 и 3, что равно 5."
    },
    54: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(): return; print(func())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция func() ничего не возвращает, поэтому вывод будет None."
    },
    55: {
        "question": "Какой будет результат выполнения следующего кода: 'def repeat(string, times): return string * times; print(repeat(\"Hey\", 3))'?",
        "answer_1": "HeyHeyHey",
        "answer_2": "Hey",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция repeat() повторяет строку 'Hey' три раза, возвращая 'HeyHeyHey'."
    },
    56: {
        "question": "Какой будет результат выполнения следующего кода: 'def get_max(a, b): return a if a > b else b; print(get_max(5, 10))'?",
        "answer_1": "10",
        "answer_2": "5",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция get_max() возвращает максимальное значение между 5 и 10, то есть 10."
    },
    57: {
        "question": "Какой будет результат выполнения следующего кода: 'def calculate_area(radius): return 3.14 * radius ** 2; print(calculate_area(2))'?",
        "answer_1": "12.56",
        "answer_2": "6.28",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция calculate_area() вычисляет площадь круга с радиусом 2, возвращая 3.14 * 4 = 12.56."
    },
    58: {
        "question": "Какой будет результат выполнения следующего кода: 'def print_list(my_list): for item in my_list: print(item); print_list([1, 2, 3])'?",
        "answer_1": "1\n2\n3",
        "answer_2": "123",
        "answer_3": "[1, 2, 3]",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция print_list() выводит каждый элемент списка, поэтому вывод будет 1, 2, 3."
    },
    59: {
        "question": "Что произойдет, если вызвать функцию, не передав обязательные параметры?",
        "answer_1": "Ошибка TypeError.",
        "answer_2": "Вернется None.",
        "answer_3": "Функция выполнится без параметров.",
        "answer_4": "Вернется 0.",
        "answer_5": "Ошибка SyntaxError.",
        "valid": "answer_1",
        "explanation": "Если не передать обязательные параметры, возникнет ошибка TypeError."
    },
    60: {
        "question": "Какой результат выполнения следующего кода: 'def my_func(a, b=2): return a + b; print(my_func(3))'?",
        "answer_1": "5",
        "answer_2": "3",
        "answer_3": "2",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция my_func() возвращает сумму 3 и значения по умолчанию 2, что равно 5."
    },
    61: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(): return; print(func())'?",
        "answer_1": "None",
        "answer_2": "0",
        "answer_3": "Ошибка",
        "answer_4": "Функция ничего не возвращает",
        "answer_5": "NoneType",
        "valid": "answer_1",
        "explanation": "Функция func() ничего не возвращает, поэтому вывод будет None."
    },
    62: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(x, y): return x + y; print(add(2, 3))'?",
        "answer_1": "5",
        "answer_2": "23",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция add() возвращает сумму 2 и 3, что равно 5."
    },
    63: {
        "question": "Какой будет результат выполнения следующего кода: 'def square(x): return x * x; print(square(4))'?",
        "answer_1": "16",
        "answer_2": "8",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция square() возвращает квадрат числа 4, что равно 16."
    },
    64: {
        "question": "Какой будет результат выполнения следующего кода: 'def repeat(string, times): return string * times; print(repeat(\"Hey\", 3))'?",
        "answer_1": "HeyHeyHey",
        "answer_2": "Hey",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция repeat() повторяет строку 'Hey' три раза, возвращая 'HeyHeyHey'."
    },
    65: {
        "question": "Какой будет результат выполнения следующего кода: 'def print_list(my_list): for item in my_list: print(item); print_list([1, 2, 3])'?",
        "answer_1": "1\n2\n3",
        "answer_2": "123",
        "answer_3": "[1, 2, 3]",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция print_list() выводит каждый элемент списка, поэтому вывод будет 1, 2, 3."
    },
    66: {
        "question": "Какой будет результат выполнения следующего кода: 'def max_value(a, b): return a if a > b else b; print(max_value(10, 20))'?",
        "answer_1": "20",
        "answer_2": "10",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция max_value() возвращает максимальное значение между 10 и 20, то есть 20."
    },
    67: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): return f\"Hello, {name}\"; print(greet(\"Bob\"))'?",
        "answer_1": "Hello, Bob",
        "answer_2": "Hello,",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "Hello, 0",
        "valid": "answer_1",
        "explanation": "Функция greet() возвращает строку 'Hello, Bob'."
    },
    68: {
        "question": "Какой будет результат выполнения следующего кода: 'def modify_list(lst): lst.append(4); return lst; print(modify_list([1, 2, 3]))'?",
        "answer_1": "[1, 2, 3, 4]",
        "answer_2": "[1, 2, 3]",
        "answer_3": "[1, 4, 2, 3]",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция modify_list() добавляет 4 в конец списка, поэтому результат будет [1, 2, 3, 4]."
    },
    69: {
        "question": "Какой будет результат выполнения следующего кода: 'def sum_list(lst): return sum(lst); print(sum_list([1, 2, 3]))'?",
        "answer_1": "6",
        "answer_2": "3",
        "answer_3": "5",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция sum_list() возвращает сумму элементов списка, то есть 1 + 2 + 3 = 6."
    },
    70: {
        "question": "Какой будет результат выполнения следующего кода: 'def concatenate(a, b): return a + b; print(concatenate(\"Hello, \", \"world!\"))'?",
        "answer_1": "Hello, world!",
        "answer_2": "Hello,",
        "answer_3": "Hello, world",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция concatenate() объединяет две строки, возвращая 'Hello, world!'."
    },
    71: {
        "question": "Какой будет результат выполнения следующего кода: 'def power(base, exp): return base ** exp; print(power(2, 3))'?",
        "answer_1": "8",
        "answer_2": "6",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция power() возвращает 2 в степени 3, что равно 8."
    },
    72: {
        "question": "Какой будет результат выполнения следующего кода: 'def get_length(lst): return len(lst); print(get_length([1, 2, 3, 4]))'?",
        "answer_1": "4",
        "answer_2": "3",
        "answer_3": "2",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция get_length() возвращает количество элементов в списке, что равно 4."
    },
    73: {
        "question": "Какой будет результат выполнения следующего кода: 'def is_even(n): return n % 2 == 0; print(is_even(4))'?",
        "answer_1": "True",
        "answer_2": "False",
        "answer_3": "0",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция is_even() проверяет, четное ли число 4, и возвращает True."
    },
    74: {
        "question": "Какой будет результат выполнения следующего кода: 'def multiply(a, b=1): return a * b; print(multiply(5))'?",
        "answer_1": "5",
        "answer_2": "6",
        "answer_3": "10",
        "answer_4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция multiply() умножает 5 на значение по умолчанию 1, поэтому результат будет 5."
    },
    75: {
        "question": "Какой будет результат выполнения следующего кода: 'def printnumbers(n): for i in range(n): print(i); printnumbers(3)'?",
        "answer1": "0\n1\n2",
        "answer2": "0\n1\n2\n3",
        "answer3": "0\n1\n2\n0\n1\n2",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer3",
        "explanation": "Функция printnumbers() выводит числа от 0 до n-1, и при вызове printnumbers(3) результат будет 0, 1, 2, 0, 1, 2."
    },
    76: {
        "question": "Какой будет результат выполнения следующего кода: 'def getaverage(a, b): return (a + b) / 2; print(getaverage(4, 6))'?",
        "answer1": "5.0",
        "answer2": "10",
        "answer3": "4",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция getaverage() возвращает среднее значение между 4 и 6, что равно 5.0."
    },
    77: {
        "question": "Какой будет результат выполнения следующего кода: 'def capitalize(word): return word.capitalize(); print(capitalize(\"hello\"))'?",
        "answer1": "Hello",
        "answer2": "hello",
        "answer3": "HELLO",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция capitalize() возвращает строку с заглавной первой буквой, то есть 'Hello'."
    },
    78: {
        "question": "Какой будет результат выполнения следующего кода: 'def swap(a, b): return b, a; print(swap(1, 2))'?",
        "answer1": "(2, 1)",
        "answer2": "(1, 2)",
        "answer3": "1, 2",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция swap() возвращает кортеж с элементами в обратном порядке, то есть (2, 1)."
    },
    79: {
        "question": "Какой будет результат выполнения следующего кода: 'def squarelist(lst): return x ** 2 for x in lst; print(squarelist([1, 2, 3]))'?",
        "answer1": "1, 4, 9",
        "answer2": "[1, 2, 3]",
        "answer3": "1, 8, 27",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция squarelist() возвращает новый список, содержащий квадраты элементов исходного списка."
    },
    80: {
        "question": "Какой будет результат выполнения следующего кода: 'def myfunction(): return 42; print(myfunction())'?",
        "answer1": "42",
        "answer2": "Ошибка",
        "answer3": "None",
        "answer4": "0",
        "answer5": "42.0",
        "valid": "answer1",
        "explanation": "Функция myfunction() возвращает значение 42."
    },
    81: {
        "question": "Какой будет результат выполнения следующего кода: 'def customfunc(): print(\"Test\"); return; customfunc()'?",
        "answer1": "Test",
        "answer2": "None",
        "answer3": "Ошибка",
        "answer4": "Test\nNone",
        "answer5": "Test\n0",
        "valid": "answer1",
        "explanation": "Функция customfunc() выводит 'Test'. Значение None не выводится, когда не указано."
    },
    82: {
        "question": "Что произойдет, если вызвать функцию с неправильным количеством аргументов?",
        "answer1": "Ошибка TypeError.",
        "answer2": "Вернется None.",
        "answer3": "Функция выполнится без параметров.",
        "answer4": "Вернется 0.",
        "answer5": "Ошибка SyntaxError.",
        "valid": "answer1",
        "explanation": "При вызове функции с неправильным количеством аргументов возникнет ошибка TypeError."
    },
    83: {
        "question": "Какой будет результат выполнения следующего кода: 'def divide(a, b): return a / b; print(divide(10, 2))'?",
        "answer1": "5.0",
        "answer2": "5",
        "answer3": "4",
        "answer4":"Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция divide() возвращает результат деления 10 на 2, что равно 5.0."
    },
    84: {
        "question": "Какой будет результат выполнения следующего кода: 'def addnumbers(*args): return sum(args); print(addnumbers(1, 2, 3))'?",
        "answer1": "6",
        "answer2": "3",
        "answer3": "1",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция addnumbers() суммирует все переданные аргументы, возвращая 6."
    },
    85: {
        "question": "Какой будет результат выполнения следующего кода: 'def myfunc(a=1, b=2): return a + b; print(myfunc(b=3))'?",
        "answer1": "4",
        "answer2": "3",
        "answer3": "1",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция myfunc() использует значение b=3 и значение по умолчанию для a, поэтому результат будет 1 + 3 = 4."
    },
    86: {
        "question": "Какой будет результат выполнения следующего кода: 'def maxvalue(a, b): return a if a > b else b; print(maxvalue(10, 20))'?",
        "answer1": "20",
        "answer2": "10",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Функция maxvalue() возвращает максимальное значение между 10 и 20, то есть 20."
    },
    87: {
        "question": "Какой будет результат выполнения следующего кода: 'def myfunction(): return; myfunction(); print(myfunction())'?",
        "answer1": "None",
        "answer2": "0",
        "answer3": "Ошибка",
        "answer4": "Функция ничего не возвращает",
        "answer5": "NoneType",
        "valid": "answer1",
        "explanation": "Функция myfunction() ничего не возвращает, поэтому вывод будет None."
    },
    88: {
        "question": "Какой будет результат выполнения следующего кода: 'def greet(name): return f\"Hello, {name}\"; print(greet(\"Alice\"))'?",
        "answer1": "Hello, Alice",
        "answer2": "Hello,",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "Hello, 0",
        "valid": "answer1",
        "explanation": "Функция greet() возвращает строку 'Hello, Alice'."
    },
    89: {
        "question": "Какой будет результат выполнения следующего кода: 'def square(x): return x * x; print(square(4))'?",
        "answer1": "16",
        "answer2": "8",
        "answer3": "4",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция square() возвращает квадрат числа 4, что равно 16."
    },
    90: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(a, b): return a + b; print(add(2, 3))'?",
        "answer1": "5",
        "answer2": "23",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Функция add() возвращает сумму 2 и 3, что равно 5."
    },
    91: {
        "question": "Какой будет результат выполнения следующего кода: 'def myfunction(): return; print(myfunction())'?",
        "answer1": "None",
        "answer2": "0",
        "answer3": "Ошибка",
        "answer4": "Функция ничего не возвращает",
        "answer5": "NoneType",
        "valid": "answer1",
        "explanation": "Функция myfunction() ничего не возвращает, поэтому вывод будет None."
    },
    92: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(x, y): return x + y; print(add(5, 10))'?",
        "answer1": "15",
        "answer2": "5",
        "answer3": "10",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Функция add() возвращает сумму 5 и 10, что равно 15."
    },
    93: {
        "question": "Какой будет результатвыполнения следующего кода: 'def square(x): return x * x; print(square(4))'?",
        "answer_1": "16",
        "answer_2": "8",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция square() возвращает квадрат числа 4, что равно 16."
    },
    94: {
        "question": "Какой будет результат выполнения следующего кода: 'def repeat(string, times): return string * times; print(repeat(\"Hey\", 3))'?",
        "answer_1": "HeyHeyHey",
        "answer_2": "Hey",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция repeat() повторяет строку 'Hey' три раза, возвращая 'HeyHeyHey'."
    },
    95: {
        "question": "Какой будет результат выполнения следующего кода: 'def print_list(my_list): for item in my_list: print(item); print_list([1, 2, 3])'?",
        "answer_1": "1\n2\n3",
        "answer_2": "123",
        "answer_3": "[1, 2, 3]",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция print_list() выводит каждый элемент списка, поэтому вывод будет 1, 2, 3."
    },
    96: {
        "question": "Какой будет результат выполнения следующего кода: 'def max_value(a, b): return a if a > b else b; print(max_value(10, 20))'?",
        "answer_1": "20",
        "answer_2": "10",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция max_value() возвращает максимальное значение между 10 и 20, то есть 20."
    },
    97: {
        "question": "Какой будет результат выполнения следующего кода: 'def multiply(a, b=1): return a * b; print(multiply(5))'?",
        "answer_1": "5",
        "answer_2": "6",
        "answer_3": "10",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция multiply() умножает 5 на значение по умолчанию 1, поэтому результат будет 5."
    },
    98: {
        "question": "Какой будет результат выполнения следующего кода: 'def print_numbers(n): for i in range(n): print(i); print_numbers(3)'?",
        "answer_1": "0\n1\n2",
        "answer_2": "0\n1\n2\n3",
        "answer_3": "0\n1\n2\n0\n1\n2",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_3",
        "explanation": "Функция print_numbers() выводит числа от 0 до n-1, и при вызове print_numbers(3) результат будет 0, 1, 2, 0, 1, 2."
    },
    99: {
        "question": "Какой будет результат выполнения следующего кода: 'def get_average(a, b): return (a + b) / 2; print(get_average(4, 6))'?",
        "answer_1": "5.0",
        "answer_2": "3",
        "answer_3": "4",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция get_average() возвращает среднее значение между 4 и 6, что равно 5.0."
    },
    100: {
        "question": "Какой будет результат выполнения следующего кода: 'def capitalize(word): return word.capitalize(); print(capitalize(\"hello\"))'?",
        "answer_1": "Hello",
        "answer_2": "hello",
        "answer_3": "HELLO",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция capitalize() возвращает строку с заглавной первой буквой, то есть 'Hello'."
    },
    101: {
        "question": "Какое ключевое слово используется для определения функции в Python?",
        "answer_1": "function",
        "answer_2": "def",
        "answer_3": "define",
        "answer_4": "fun",
        "answer_5": "method",
        "valid": "answer_2",
        "explanation": "Ключевое слово 'def' используется для определения функции в Python."
    },
    102: {
        "question": "Что произойдет, если вы попытаетесь вернуть несколько значений из функции?",
        "answer_1": "Вернутся все значения как кортеж.",
        "answer_2": "Вернется только первое значение.",
        "answer_3": "Произойдет ошибка.",
        "answer_4": "Вернется None.",
        "answer_5": "Ничего не произойдет.",
        "valid": "answer_1",
        "explanation": "Если вы вернете несколько значений, они будут упакованы в кортеж."
    },
    103: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(x, y=5): return x + y; print(func(10))'?",
        "answer_1": "15",
        "answer_2": "10",
        "answer_3": "5",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция func() использует значение по умолчанию для y, поэтому 10 + 5 = 15."
    },
    104: {
        "question": "Какой из следующих параметров позволяет передавать любое количество аргументов в функцию?",
        "answer_1": "*args",
        "answer_2": "**kwargs",
        "answer_3": "args",
        "answer_4": "params",
        "answer_5": "list",
        "valid": "answer_1",
        "explanation": "Параметр *args позволяет передавать произвольное количество позиционных аргументов в функцию."
    },
    105: {
        "question": "Что такое 'docstring' в функции?",
        "answer_1": "Это строка, описывающая функцию.",
        "answer_2": "Это имя функции.",
        "answer_3": "Это тип возвращаемого значения.",
        "answer_4": "Это параметр функции.",
        "answer_5": "Это переменная внутри функции.",
        "valid": "answer_1",
        "explanation": "Docstring — это строка документации, которая описывает, что делает функция."
    },
    106: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(a=1, b): return a + b; print(func(2))'?",
        "answer_1": "Ошибка",
        "answer_2": "3",
        "answer_3": "2",
        "answer_4": "1",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Необязательные параметры должны идти после обязательных, иначе возникнет ошибка."
    },
    107: {
        "question": "Какой будет результат выполнения следующего кода: 'def add(a, b=2): return a + b; print(add(3, 5))'?",
        "answer_1": "8",
        "answer_2": "5",
        "answer_3": "3",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция add() возвращает сумму 3 и 5, игнорируя значение по умолчанию для b."
    },
    108: {
        "question": "Какой будет результат выполнения следующего кода: 'def func(x): return x + 1; print(func(10))'?",
        "answer_1": "11",
        "answer_2": "10",
        "answer_3": "1",
        "answer_4": "Ошибка",
        "answer_5": "None",
        "valid": "answer_1",
        "explanation": "Функция func() возвращает 10 + 1, что равно 11."
    },
    109: {
        "question": "Что произойдет, если вы НЕ укажете ключевое команду 'return' в теле функции?",
        "answer_1": "Функция вернет None.",
        "answer_2": "Функция вызовет ошибку.",
        "answer_3": "Функция выполнится, но ничего не выведет.",
        "answer_4": "Функция вернет 0.",
        "answer_5": "Ничего не произойдет.",
        "valid": "answer_1",
        "explanation": "Если 'return' не указано, функция завершится, и вернется значение None по умолчанию."
    },
}
