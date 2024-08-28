# Создание функции
def get_matrix(n, m, value):
    # Создание пустого списка для хранения матрицы
    matrix = []

    # Проверка размеров матрицы на годность
    if n <= 0 or m <= 0:
        return matrix  # Возвращает пустой спиок при негодности размеров

    # Внешний цикл для создания строк матрицы
    for _ in range(n):
        # Создание строки с повторяющимися значениями
        string = [value] * m
        # Последловательное добавление строк в матрицу
        matrix.append(string)

    # Завершение функции
    return matrix

# Исходный код:
result1 = get_matrix(2, 2, 10)
result2 = get_matrix(3, 5, 42)
result3 = get_matrix(4, 2, 13)

# Вывод на консоль:
print(result1)
print(result2)
print(result3)