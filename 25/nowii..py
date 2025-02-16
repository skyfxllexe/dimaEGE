


# def f(x,y,A):
#     return (((y+2*x)<A) or (x>30) or (y>20))

# for A in range(100):
#     flag=True
#     for x in range(100):
#         for y in range(100):
#             if f(x,y,A)==False:
#                 flag=False
#     if flag == True:
#         print(A)








def f(x,A):
    return ((120%A==0)) and ((x%36==0)<=((x%A!=0)<=(x%45!=0)))



for A in range(1,1000):
    flag=True
    for x in range(1,1000):
        if f(x,A)==False:
            flag=False
    if flag==True:
        print(A)