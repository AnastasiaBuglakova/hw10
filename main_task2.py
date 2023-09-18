import csv
import json
import os
import random
from typing import Callable
from functools import wraps

class Files:
    def json_safe(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not os.path.exists(f'solve_q_equation.json'):
                with open(f'solve_q_equation.json', 'w', encoding='utf-8') as f:
                    atr = ','.join(list(map(str, args))) + ','.join(
                        list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                    json.dump({atr: result}, f, indent=4, ensure_ascii=False)

            else:
                with open(f'solve_q_equation.json', 'r', encoding='utf-8') as f_read:
                    json_data = json.load(f_read)
                with open(f'solve_q_equation.json', 'w', encoding='utf-8') as f_write:
                    atr = ','.join(list(map(str, args))) + ','.join(
                        list(map(lambda x, y: str(f'{x}={y}'), kwargs.items())))
                    json_data[atr] = result
                    json.dump(json_data, f_write, indent=4, ensure_ascii=False)

            return result

        return wrapper


    def data_from_csv(num: int = 100):
        def deco(func: Callable):
            res = []

            def wrapper(*args, **kwargs):
                if args or kwargs:
                    print(func(*args, **kwargs))
                else:
                    with open("numbers in csv.csv", 'r', encoding='utf-8') as f:
                        csv_data = csv.reader(f)

                        for i in csv_data:
                            res.append(func(float(i[0]), float(i[1]), float(i[2])))

                return res

            return wrapper

        return deco

    def gen_csv():
        numbers_for_csv = [[random.randint(0, 99) for _ in range(3)] for _ in range(random.randint(100, 1001))]
        with open('numbers in csv.csv', 'w', encoding='utf-8') as f:
            csv_write = csv.writer(f)

            csv_write.writerows(numbers_for_csv)

    # Напишите следующие функции:
    # Нахождение корней квадратного уравнения


class Solvetion:
    @Files.json_safe
    @Files.data_from_csv(4)

    def solve_q_equation(a: int, b: int, c: int) -> str:
        discriminant = b ** 2 - 4 * a * c
        if discriminant < 0 or a == 0:
            return 'Корней нет'
        elif discriminant == 0:
            x = round(-b / (2 * a), 2)
            return f'{x = }'
        else:
            x1 = round((-b + discriminant ** 0.5) / (2 * a), 2)
            x2 = round((-b - discriminant ** 0.5) / (2 * a), 2)
            return f'{x1 = }, {x2 = }'





# Генерация csv файла с тремя случайными числами в каждой строке. 100-1000 строк.




Files.gen_csv()
print(f'{Solvetion.solve_q_equation() = }')