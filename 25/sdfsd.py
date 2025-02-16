


def f(x,y,A): # def - define - определить
    return ((x<A)<=(x**2<100)) and ((y**2<=64) <= (y<=A))


count = 0
for A in range(100):
    flag = True # изначально полагаем, что такое A - нам подходит
    for x in range(100):
        for y in range(100):
            if f(x,y,A)==False:
                flag = False # если мы оказались тут, значит поймали False на f(x,y,A) => такое A не подходит

    count += (flag == True)

print(count)