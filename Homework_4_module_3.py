import multiprocessing
import math
import time

def find_divisors(num):
    divisors = []
    for i in range(1, int(math.sqrt(num)) + 1):
        if num % i == 0:
            divisors.append(i)
            if i != num // i:
                divisors.append(num // i)
    return sorted(divisors)

def factorize_parallel(*numbers):
    with multiprocessing.Pool(multiprocessing.cpu_count()) as pool:
        result = pool.map(find_divisors, numbers)
    return result

if __name__ == "__main__":
    # Тестуємо паралельну версію
    start_time = time.time()

    a, b, c, d = factorize_parallel(128, 255, 99999, 10651060)

    print("Паралельна версія виконана за: %s секунд" % (time.time() - start_time))

    # Перевірка правильності
    assert a == [1, 2, 4, 8, 16, 32, 64, 128]
    assert b == [1, 3, 5, 15, 17, 51, 85, 255]
    assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
    assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]





import time
import math

def factorize(*numbers):
    result = []
    for num in numbers:
        divisors = []
        for i in range(1, int(math.sqrt(num)) + 1):
            if num % i == 0:
                divisors.append(i)
                if i != num // i:  # Уникаємо дублювання для квадратів
                    divisors.append(num // i)
        result.append(sorted(divisors))
    return result
# Тестуємо функцію
start_time = time.time()

a, b, c, d  = factorize(128, 255, 99999, 10651060)

print("Синхронна версія виконана за: %s секунд" % (time.time() - start_time))

# Перевірка правильності
assert a == [1, 2, 4, 8, 16, 32, 64, 128]
assert b == [1, 3, 5, 15, 17, 51, 85, 255]
assert c == [1, 3, 9, 41, 123, 271, 369, 813, 2439, 11111, 33333, 99999]
assert d == [1, 2, 4, 5, 7, 10, 14, 20, 28, 35, 70, 140, 76079, 152158, 304316, 380395, 532553, 760790, 1065106, 1521580, 2130212, 2662765, 5325530, 10651060]
