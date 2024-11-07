for i in range(1, 6):
    for j in range(1, 11): 
        num = (i - 1) * 10 + j 
        if num % 5 == 0:
            print("pass", end=' ')
        else:
            print(num, end=' ')
    print()