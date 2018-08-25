def func_oter():
    x = 2
    print('Х равен', x)

    def func_inner():
        nonlocal x
        x = 5

     func_inner()
     print('Локальная Х сменилась на', x)

func_oter()

