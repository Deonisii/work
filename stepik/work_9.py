'''Напишите программу, на вход которой даются четыре числа a, b, c и d, каждое в своей строке. 
Программа должна вывести фрагмент таблицы умножения для всех чисел отрезка [a;b] 
на все числа отрезка [c;d].

Числа a, b, c и d являются натуральными и не превосходят 10, a≤b, c≤d.

Следуйте формату вывода из примера, для разделения элементов внутри строки используйте 
'\t' — символ табуляции. 
Заметьте, что левым столбцом и верхней строкой выводятся сами числа из заданных
отрезков — заголовочные столбец и строка таблицы.'''
# a= 7|b= 10|c= 5|d= 6
a=int(input())
b=int(input())
c=int(input())
d=int(input())
while (a,b,c,d<=10) and (a<=b) and (c<=d):
    for x in range(c,d+1):
        print('\t',x,end="")
    break
print('\n')
for i in range(a,b+1):
    print(i,'\t',i*c, '\t', i*d,'\t')
    continue

    