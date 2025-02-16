def devider(n):
    array=[]
    for i in range(2,int(n**0.5)+1):
        if n % i == 0:
            array.append(i)
            if n//i != i:
                array.append(n//i)
    array.sort(reverse=True)
    return array
count=0
for i in range(300000000+1,400000000):
    q=devider(i)
    if len(q)>=5:

        print(i, q[4])
        # print(w)
        count+=1
        if count==5:
            break