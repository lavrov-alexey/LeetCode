def num_validation(in_str: str):
    MIN_NUM, MAX_NUM = -2000000000, 2000000000
    try:
        num = int(in_str)
        assert MIN_NUM <= num <= MAX_NUM
    except (ValueError, AssertionError):
        print('Недопустимые слагаемые. Ожидается ввод через пробел 2х целых '
              'чисел в диапазоне от -2е9 до 2е9!')
        exit(1)
    return num


if __name__ == '__main__':
    IN_FILE, OUT_FILE = 'input.txt', 'output.txt'
    try:
        with open(IN_FILE, 'r', encoding='utf-8') as in_f:
            num1, num2 = map(num_validation, in_f.readline().split())
    except FileNotFoundError:
        print(f'Входной файл {IN_FILE} не найден!')
        exit(2)
    try:
        with open(OUT_FILE, 'w', encoding='utf-8') as out_f:
            out_f.write(str(num1 + num2))
    except:
        print('Что-то пошло не так...')
        exit(3)
