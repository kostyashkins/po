# Библиотека функций

def fibonacci(n):
    """
    Возвращает список из первых n чисел Фибоначчи.
    :param n: Количество чисел Фибоначчи.
    :return: Список чисел Фибоначчи.
    """
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]

    fib = [0, 1]
    for i in range(2, n):
        fib.append(fib[i - 1] + fib[i - 2])
    return fib

def bubble_sort(arr):
    """
    Сортирует список чисел методом пузырька.
    :param arr: Список чисел.
    :return: Отсортированный список.
    """
    if not isinstance(arr, list):
        raise TypeError("Входные данные должны быть списком.")

    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

def sieve_of_eratosthenes(n):
    """
    Возвращает список всех простых чисел до n (включительно).
    :param n: Верхняя граница поиска простых чисел.
    :return: Список простых чисел.
    """
    if n < 2:
        return []

    sieve = [True] * (n + 1)
    sieve[0] = sieve[1] = False

    for p in range(2, int(n ** 0.5) + 1):
        if sieve[p]:
            for i in range(p * p, n + 1, p):
                sieve[i] = False

    primes = [p for p, is_prime in enumerate(sieve) if is_prime]
    return primes