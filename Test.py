

def main():
    str=input("Введите пример:")
    str = str.split()
    if(len(str)>3):
        raise Exception('формат математической операции не удовлетворяет заданию - два операнда и один оператор')
    try:
        a = int(str[0])
        if (a<1) or (a>10):
            raise Exception('значение должно быть в диапазоне от 1 до 10')
        znak = str[1]
        b = int(str[2])
        if (b<1) or (b>10):
            raise Exception('значение должно быть в диапазоне от 1 до 10')
        if znak == "+":
            return a+b
        elif znak == "-":
            return a-b
        elif znak == "*":
            return a*b
        elif znak == "/":
            return round(a/b)
    except:
        print('строка не является математической операцией')
print(main())
