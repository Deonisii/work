number = 23
guess = int(input('Ведите целое число : '))

if guess == number: # (if - если) (== сравнние)
    print('Поздравляю, вы угадали')
    print('Хотя и не выйграли никакого приза!')
elif guess < number: # 
    print('Нет, загаданное число немного больше этого.')
else: # (else - иначе)
    print('Нет, загаданное число немного меньше этого.')

print('Завершено')