a=int(input())
the_first = a//100
the_second = (a%100)//10
the_third = a%10
c = (the_first + the_second + the_third)
d = (the_first * the_second * the_third)
print("Сумма цифр =", c)
print("Произведение цифр =", d)