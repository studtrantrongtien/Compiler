import random

SIGMA = ["a", "b", "c"]

ALPHA = ["a", "b", "c", "S", "A", "B", "C"]

Grammar = [['B', 'A', 'b'], ['c', 'A', 'B', 'C'], ['b', 'B'], ['a'], ['b'], ['c', 'A']]

Lookup_TB = {'S': {'a': -1, 'b': 0, 'c': -1}, 'A': {'a': 3, 'b': 2, 'c': 1}, 'B': {'a': -1, 'b': 4, 'c': -1},
             'C': {'a': -1, 'b': -1, 'c': 5}}


# print(Lookup_TB['S']['a'])


def gen_rand():
    res = ""
    k = random.randint(0, 2)
    if k == 0:
        res += 'c'
        res += gen_rand()
        res += "bc"
        res += gen_rand()
    if k == 1:
        res += "bb"
    if k == 2:
        res += "a"
    # print(res)
    return res


def generate():
    res = ""
    res += "b"
    res += gen_rand()
    res += "b"
    print("Выход: " + res)
    return res


def is_terminal(_str):
    if _str == "S" or _str == "A" or _str == "B" or _str == "C":
        return False
    return True


def is_alpha(_str):
    for x in _str:
        if x not in ALPHA:
            return False
    return True


def recognize(_str):
    gen_num = ""
    # print(_str)
    n = len(_str)
    if n <= 0:
        print("Цепочка не принадлежит языку")
        print("Код Генерации : -1")
        return

    if not is_alpha(_str):
        print("Символы не из альфавита")
        print("Код Генерации : -2")
        return
    stack = []
    current_pos = 0

    stack.append("S")
    while current_pos < n:
        current_sym = stack.pop(-1)
        if is_terminal(current_sym):
            if _str[current_pos] == current_sym:
                current_pos += 1

        if not is_terminal(current_sym):
            # find index production:
            index_production = Lookup_TB[current_sym][_str[current_pos]]
            gen_num += str(index_production)
            for x in range(0, len(Grammar[index_production])):
                stack.append(Grammar[index_production][len(Grammar[index_production]) - x - 1])

        if len(stack) == 0:
            if current_pos == n:
                # print("OK")
                print("Цепочка принадлежит языку")
                print("Код Генерации : " + gen_num)
            else:
                print("Цепочка не принадлежит языку")
                print("Код Генерации : -1")
            break


if __name__ == '__main__':
    # print(gen_rand())
    # print(generate())
    # recognize(generate())
    # recognize("bcbbbccbbbcab")
    # for i in range(0, 100):
    #    recognize(generate())
    while True:
        print("\nЛабораторная Работа 5: ")
        print("1 : Генератор")
        print("2 : Распознаватель")
        control = input("Ввод: ")
        if control == "1":
            generate()
            continue
        if control == "2":
            input_string = input("Вводит цепочку: ")
            recognize(input_string)
            continue
        break
