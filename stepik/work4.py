def end_word(n: int):
    end = n % 10
    sufix = 'ов'
    if end == 1:
        sufix = ''    
    elif end > 1 and end < 5:
        sufix = 'a'
    return (sufix)


n = 7
n=int(input("Введите число программистов: "))


print("В комнате {} программист{}".format(n, end_word(n)))


