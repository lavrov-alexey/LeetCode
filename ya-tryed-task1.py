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
    num1, num2 = map(num_validation, input().split())
    print(num1 + num2)
