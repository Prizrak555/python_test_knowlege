name_theme = "Коллекции данных (в разработке)"
questions_dict = {
    0: {
        "question": "Какой из следующих типов данных является изменяемым?",
        "answer_1": "tuple",
        "answer_2": "list",
        "answer_3": "frozenset",
        "answer_4": "str",
        "answer_5": "dict",
        "valid": "answer_2",
        "explanation": "Списки (list) являются изменяемыми, что позволяет добавлять, удалять и изменять их элементы."
    },
    1: {
        "question": "Какой из следующих типов данных является неизменяемым?",
        "answer_1": "list",
        "answer_2": "dict",
        "answer_3": "tuple",
        "answer_4": "set",
        "answer_5": "bytearray",
        "valid": "answer_3",
        "explanation": "Кортежи (tuple) являются неизменяемыми, что означает, что их нельзя изменить после создания."
    },
    2: {
        "question": "Какой метод используется для добавления элемента в список?",
        "answer_1": "add()",
        "answer_2": "append()",
        "answer_3": "insert()",
        "answer_4": "extend()",
        "answer_5": "push()",
        "valid": "answer_2",
        "explanation": "Метод append() добавляет элемент в конец списка."
    },
    3: {
        "question": "Какой метод используется для получения всех ключей словаря?",
        "answer_1": "keys()",
        "answer_2": "get()",
        "answer_3": "values()",
        "answer_4": "items()",
        "answer_5": "all_keys()",
        "valid": "answer_1",
        "explanation": "Метод keys() возвращает все ключи словаря."
    },
    4: {
        "question": "Какой тип данных лучше всего подходит для хранения уникальных значений?",
        "answer_1": "list",
        "answer_2": "tuple",
        "answer_3": "dict",
        "answer_4": "set",
        "answer_5": "str",
        "valid": "answer_4",
        "explanation": "Множества (set) предназначены для хранения уникальных значений."
    },
    5: {
        "question": "Какой метод используется для удаления элемента из множества?",
        "answer_1": "remove()",
        "answer_2": "discard()",
        "answer_3": "pop()",
        "answer_4": "delete()",
        "answer_5": "clear()",
        "valid": "answer_2",
        "explanation": "Метод discard() удаляет элемент из множества, если он существует, и не вызывает ошибку, если его нет."
    },
    6: {
        "question": "Какой из следующих типов данных занимает меньше памяти?",
        "answer_1": "list",
        "answer_2": "tuple",
        "answer_3": "dict",
        "answer_4": "set",
        "answer_5": "frozenset",
        "valid": "answer_2",
        "explanation": "Кортежи (tuple) занимают меньше памяти, чем списки (list), так как они неизменяемы."
    },
    7: {
        "question": "Какой метод используется для объединения двух списков?",
        "answer_1": "join()",
        "answer_2": "merge()",
        "answer_3": "combine()",
        "answer_4": "extend()",
        "answer_5": "append()",
        "valid": "answer_4",
        "explanation": "Метод extend() добавляет элементы одного списка в другой."
    },
    8: {
        "question": "Какой из следующих типов данных подходит для хранения пар ключ-значение?",
        "answer_1": "list",
        "answer_2": "tuple",
        "answer_3": "set",
        "answer_4": "dict",
        "answer_5": "str",
        "valid": "answer_4",
        "explanation": "Словари (dict) используются для хранения пар ключ-значение."
    },
    9: {
        "question": "Какой метод используется для получения значения по ключу в словаре?",
        "answer_1": "get()",
        "answer_2": "find()",
        "answer_3": "retrieve()",
        "answer_4": "search()",
        "answer_5": "index()",
        "valid": "answer_1",
        "explanation": "Метод get() позволяет получить значение по заданному ключу в словаре."
    },
    10: {
        "question": "Какой будет результат выполнения следующего кода: 'x = (1, 2, 3); print(x1)'?",
        "answer1": "1",
        "answer2": "2",
        "answer3": "3",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer2",
        "explanation": "Кортежи индексируются, и элемент с индексом 1 равен 2."
    },
    11: {
        "question": "Какой из следующих методов используется для сортировки списка?",
        "answer1": "sort()",
        "answer2": "order()",
        "answer3": "sorted()",
        "answer4": "shuffle()",
        "answer5": "reverse()",
        "valid": "answer1",
        "explanation": "Метод sort() сортирует элементы списка на месте."
    },
    12: {
        "question": "Какой из следующих типов данных позволяет хранить только уникальные значения и не имеет порядка?",
        "answer1": "list",
        "answer2": "tuple",
        "answer3": "dict",
        "answer4": "set",
        "answer5": "frozenset",
        "valid": "answer4",
        "explanation": "Множества (set) хранят только уникальные значения и не имеют порядка."
    },
    13: {
        "question": "Какой результат выполнения следующего кода: 'd = {\"key\": \"value\"}; print(d\"key\")'?",
        "answer1": "key",
        "answer2": "value",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer2",
        "explanation": "Словарь d содержит пару ключ-значение, и доступ к значению осуществляется по ключу."
    },
    14: {
        "question": "Какой из следующих методов используется для копирования списка?",
        "answer1": "copy()",
        "answer2": "duplicate()",
        "answer3": "clone()",
        "answer4": "replicate()",
        "answer5": "slice()",
        "valid": "answer1",
        "explanation": "Метод copy() создает поверхностную копию списка."
    },
    15: {
        "question": "Какой будет результат выполнения выражения 'len(1, 2, 3)'?",
        "answer1": "2",
        "answer2": "3",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer2",
        "explanation": "Функция len() возвращает количество элементов в списке, в данном случае это 3."
    },
    16: {
        "question": "Какой метод используется для очистки всех элементов из множества?",
        "answer1": "clear()",
        "answer2": "remove()",
        "answer3": "discard()",
        "answer4": "delete()",
        "answer5": "reset()",
        "valid": "answer1",
        "explanation": "Метод clear() удаляет все элементы из множества."
    },
    17: {
        "question": "Какой из следующих типов данных лучше всего подходит для хранения фиксированного набора данных?",
        "answer1": "list",
        "answer2": "set",
        "answer3": "tuple",
        "answer4": "dict",
        "answer5": "str",
        "valid": "answer3",
        "explanation": "Кортежи (tuple) лучше всего подходят для хранения фиксированного набора данных, так как они неизменяемы."
    },
    18: {
        "question": "Какой метод используется для получения всех значений словаря?",
        "answer1": "values()",
        "answer2": "get()",
        "answer3": "keys()",
        "answer4": "items()",
        "answer5": "allvalues()",
        "valid": "answer1",
        "explanation": "Метод values() возвращает все значения словаря."
    },
    19: {
        "question": "Какой будет результат выполнения следующего кода: 'x = {1, 2, 3}; x.add(4); print(x)'?",
        "answer1": "{1, 2, 3}",
        "answer2": "{1, 2, 3, 4}",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer2",
        "explanation": "Метод add() добавляет элемент в множество, если его там нет."
    },
    20: {
        "question": "Какой метод используется для получения количества элементов в множестве?",
        "answer1": "count()",
        "answer2": "len()",
        "answer3": "size()",
        "answer4": "length()",
        "answer5": "get()",
        "valid": "answer2",
        "explanation": "Функция len() возвращает количество элементов в множестве."
    },
    21: {
        "question": "Какой результат выполнения следующего кода: 'x = (1, 2, 3); x[0] = 10'?",
        "answer1": "10",
        "answer2": "1",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer3",
        "explanation": "Кортежи (tuple) являются неизменяемыми, и попытка изменить элемент вызовет ошибку."
    },
    22: {
        "question": "Какой оператор используется для объединения двух множеств?",
        "answer1": "|",
        "answer2": "+",
        "answer3": "&",
        "answer4": "add()",
        "answer5": "union()",
        "valid": "answer1",
        "explanation": "Оператор | используется для объединения двух множеств."
    },
    23: {
        "question": "Какой результат выполнения следующего кода: 'x = {1, 2, 2}; print(x)'?",
        "answer1": "{1, 2}",
        "answer2": "{1, 2, 2}",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Множества автоматически удаляют дубликаты, поэтому результатом будет {1, 2}."
    },
    24: {
        "question": "Какой метод используется для получения элементов из списка, начиная с определенного индекса?",
        "answer1": "slice()",
        "answer2": "get()",
        "answer3": "sublist()",
        "answer4": "slice()",
        "answer5": "index()",
        "valid": "answer1",
        "explanation": "Метод slice() позволяет получить подсписок, начиная с заданного индекса."
    },
    25: {
        "question": "Какой будет результат выполнения выражения 'set([1, 2, 2])'?",
        "answer1": "{1, 2}",
        "answer2": "{1, 2, 2}",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Множества автоматически удаляют дубликаты, поэтому результатом будет {1, 2}."
    },
    26: {
        "question": "Какой метод используется для создания копии словаря?",
        "answer1": "copy()",
        "answer2": "duplicate()",
        "answer3": "clone()",
        "answer4": "replicate()",
        "answer5": "slice()",
        "valid": "answer1",
        "explanation": "Метод copy() создает поверхностную копию словаря."
    },
    27: {
        "question": "Какой будет результат выполнения кода: 'x = {1: \"один\", 2: \"два\"}; print(x[2])'?",
        "answer1": "один",
        "answer2": "два",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer2",
        "explanation": "Словарь x содержит пару ключ-значение, и доступ к значению осуществляется по ключу."
    },
    28: {
        "question": "Какой метод используется для добавления элемента в множество, не вызывая ошибки, если он уже существует?",
        "answer1": "add()",
        "answer2": "insert()",
        "answer3": "discard()",
        "answer4": "append()",
        "answer5": "update()",
        "valid": "answer3",
        "explanation": "Метод discard() удаляет элемент из множества, если он существует, и не вызывает ошибку, если его нет."
    },
    29: {
        "question": "Какой результат выполнения следующего кода: 'x = [1, 2, 3]; x.pop(); print(x)'?",
        "answer1": "1, 2",
        "answer2": "[1, 2, 3]",
        "answer3": "3",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Метод pop() удаляет последний элемент из списка, поэтому результатом будет [1, 2]."
    },
    30: {
        "question": "Какой будет результат выполнения выражения '1 in (1, 2, 3)'?",
        "answer1": "True",
        "answer2": "False",
        "answer3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Оператор in проверяет наличие элемента в последовательности, и 1 действительно содержится в (1, 2, 3)."
    },
    31: {
        "question": "Какой метод используется для получения элемента по индексу в списке?",
        "answer_1": "get()",
        "answer_2": "index()",
        "answer_3": "pop()",
        "answer_4": "__getitem__()",
        "answer_5": "slice()",
        "valid": "answer_4",
        "explanation": "Метод __getitem__() позволяет получить элемент по индексу в списке."
    },
    32: {
        "question": "Какой из следующих типов данных позволяет хранить элементы в порядке их добавления?",
        "answer_1": "set",
        "answer_2": "dict",
        "answer_3": "list",
        "answer_4": "tuple",
        "answer_5": "frozenset",
        "valid": "answer_3",
        "explanation": "Списки (list) сохраняют порядок добавления элементов."
    },
    33: {
        "question": "Какой результат выполнения следующего кода: 'd = {\"a\": 1, \"b\": 2}; d[\"c\"] = 3; print(d)'?",
        "answer_1": "{\"a\": 1, \"b\": 2}",
        "answer_2": "{\"a\": 1, \"b\": 2, \"c\": 3}",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_2",
        "explanation": "Словари могут динамически добавлять новые пары ключ-значение, поэтому результатом будет {\"a\": 1, \"b\": 2, \"c\": 3}."
    },
    34: {
        "question": "Какой оператор используется для пересечения двух множеств?",
        "answer_1": "&",
        "answer_2": "|",
        "answer_3": "+",
        "answer_4": "intersect()",
        "answer_5": "combine()",
        "valid": "answer_1",
        "explanation": "Оператор & используется для пересечения двух множеств."
    },
    35: {
        "question": "Какой будет результат выполнения кода: 'x = [1, 2, 3]; x.remove(2); print(x)'?",
        "answer_1": "[1, 2, 3]",
        "answer_2": "[1, 3]",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_2",
        "explanation": "Метод remove() удаляет первый найденный элемент из списка, в данном случае 2."
    },
    36: {
        "question": "Какой результат выполнения выражения 'tuple([1, 2, 3])'?",
        "answer_1": "(1, 2, 3)",
        "answer_2": "[1, 2, 3]",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Функция tuple() создает кортеж на основе переданного списка."
    },
    37: {
        "question": "Какой метод используется для получения элемента по индексу в словаре?",
        "answer_1": "get()",
        "answer_2": "index()",
        "answer_3": "retrieve()",
        "answer_4": "find()",
        "answer_5": "pop()",
        "valid": "answer_1",
        "explanation": "Метод get() позволяет получить значение по заданному ключу в словаре."
    },
    38: {
        "question": "Какой результат выполнения следующего кода: 'x = {1, 2}; x.update([2, 3]); print(x)'?",
        "answer_1": "{1, 2, 3}",
        "answer_2": "{1, 2}",
        "answer_3": "Ошибка",
        "answer_4": "None",
        "answer_5": "0",
        "valid": "answer_1",
        "explanation": "Метод update() добавляет элементы из другого коллекции, включая дубликаты."
    },
    39: {
        "question": "Какой метод используется для получения первого элемента списка?",
        "answer_1": "first()",
        "answer_2": "get_first()",
        "answer_3": "pop(0)",
        "answer_4": "index(0)",
        "answer_5": "list[0]",
        "valid": "answer_5",
        "explanation": "Элементы списка можно получить по индексу, и первый элемент имеет индекс 0."
    },
    40: {
        "question": "Какой результат выполнения следующего кода: 'x = {\"key\": \"value\"}; del x[\"key\"]; print(x)'?",
        "answer_1": "{}",
        "answer_2": "{\"key\": \"value\"}",
        "answer_3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Оператор del удаляет элемент по ключу, и после этого словарь станет пустым."
    },
    41: {
        "question": "Какой будет результат выполнения выражения '3 not in [1, 2, 3]'?",
        "answer1": "True",
        "answer2": "False",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer2",
        "explanation": "3 содержится в списке, поэтому результат будет False."
    },
    42: {
        "question": "Какой оператор используется для определения, является ли множество подмножеством другого?",
        "answer1": "in",
        "answer2": "issubset()",
        "answer3": "subset",
        "answer4": "not in",
        "answer5": "is",
        "valid": "answer2",
        "explanation": "Метод issubset() используется для проверки, является ли одно множество подмножеством другого."
    },
    43: {
        "question": "Какой результат выполнения следующего кода: 'x = [1, 2, 3]; print(x[:2])'?",
        "answer1": "1, 2",
        "answer2": "[1, 2, 3]",
        "answer3": "2, 3",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Срез x[:2] возвращает элементы с индексами 0 и 1."
    },
    44: {
        "question": "Какой метод используется для получения уникальных значений из списка?",
        "answer1": "unique()",
        "answer2": "distinct()",
        "answer3": "set()",
        "answer4": "removeduplicates()",
        "answer5": "filter()",
        "valid": "answer3",
        "explanation": "Функция set() создает множество, которое содержит только уникальные значения из списка."
    },
    45: {
        "question": "Какой будет результат выполнения следующего кода: 'x = (1, 2, 3); print(len(x))'?",
        "answer1": "3",
        "answer2": "2",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Функция len() возвращает количество элементов в кортеже."
    },
    46: {
        "question": "Какой метод используется для добавления нескольких элементов в множество?",
        "answer1": "add()",
        "answer2": "update()",
        "answer3": "extend()",
        "answer4": "insert()",
        "answer5": "append()",
        "valid": "answer2",
        "explanation": "Метод update() добавляет несколько элементов в множество."
    },
    47: {
        "question": "Какой будет результат выполнения кода: 'x = 1, 2, 3; x.insert(1, 4); print(x)'?",
        "answer1": "[1, 4, 2, 3]",
        "answer2": "4, 1, 2, 3",
        "answer3": "[1, 2, 3, 4]",
        "answer4": "Ошибка",
        "answer5": "None",
        "valid": "answer1",
        "explanation": "Метод insert() добавляет элемент 4 на индекс 1, сдвигая остальные элементы вправо."
    },
    48: {
        "question": "Какой результат выполнения выражения '1 in {1, 2, 3}'?",
        "answer1": "True",
        "answer2": "False",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Оператор in проверяет наличие элемента в множестве, и 1 действительно содержится в {1, 2, 3}."
    },
    49: {
        "question": "Какой будет результат выполнения следующего кода: 'x = 1, 2, 3; x.clear(); print(x)'?",
        "answer1": "[]",
        "answer2": "1, 2, 3",
        "answer3": "Ошибка",
        "answer4": "None",
        "answer5": "0",
        "valid": "answer1",
        "explanation": "Метод clear() удаляет все элементы из списка, и результатом будет пустой список."
    },
    50: {
        "question": "Какой метод используется для получения элемента и удаления его из списка?",
        "answer1": "pop()",
        "answer2": "remove()",
        "answer3": "delete()",
        "answer4": "discard()",
        "answer_5": "shift()",
        "valid": "answer_1",
        "explanation": "Метод pop() удаляет элемент по индексу и возвращает его значение."
    },

}
