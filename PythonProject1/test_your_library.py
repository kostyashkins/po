# Тесты с использованием pytest

import pytest
from your_library import fibonacci, bubble_sort, sieve_of_eratosthenes

# Тесты для функции fibonacci
def test_fibonacci():
    # Корректные входные данные
    assert fibonacci(0) == []  # Граничное значение
    assert fibonacci(1) == [0]  # Граничное значение
    assert fibonacci(2) == [0, 1]  # Граничное значение
    assert fibonacci(5) == [0, 1, 1, 2, 3]  # Обычный случай
    assert fibonacci(10) == [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]  # Обычный случай

    # Некорректные входные данные
    with pytest.raises(TypeError):
        fibonacci("5")  # Неверный тип данных
    with pytest.raises(TypeError):
        fibonacci(-5)  # Отрицательное число

# Тесты для функции bubble_sort
def test_bubble_sort():
    # Корректные входные данные
    assert bubble_sort([4, 3, 2, 1]) == [1, 2, 3, 4]  # Обычный случай
    assert bubble_sort([1]) == [1]  # Граничное значение
    assert bubble_sort([]) == []  # Граничное значение
    assert bubble_sort([5, -3, 0, 2]) == [-3, 0, 2, 5]  # С отрицательными числами

    # Некорректные входные данные
    with pytest.raises(TypeError):
        bubble_sort("not a list")  # Неверный тип данных

# Тесты для функции sieve_of_eratosthenes
def test_sieve_of_eratosthenes():
    # Корректные входные данные
    assert sieve_of_eratosthenes(0) == []  # Граничное значение
    assert sieve_of_eratosthenes(1) == []  # Граничное значение
    assert sieve_of_eratosthenes(2) == [2]  # Граничное значение
    assert sieve_of_eratosthenes(10) == [2, 3, 5, 7]  # Обычный случай
    assert sieve_of_eratosthenes(20) == [2, 3, 5, 7, 11, 13, 17, 19]  # Обычный случай

    # Некорректные входные данные
    with pytest.raises(TypeError):
        sieve_of_eratosthenes("10")  # Неверный тип данных
    with pytest.raises(TypeError):
        sieve_of_eratosthenes(-10)  # Отрицательное число