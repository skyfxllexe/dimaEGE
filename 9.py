
corn = [200_000_000, 400_000_000]

for i in range(0,50, 2):
    for j in range(1,50,3):
        num = 2**i * 3 ** j
        if num <= corn[1] and num>=corn[0]:
            print(num)