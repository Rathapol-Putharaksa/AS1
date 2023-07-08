def BackZero(num):
    i = 1
    flagValue = 1
    countZero = 0
    for i in range(1,num+1):
        flagValue*=i
    

    for digit in str(flagValue)[::-1]:
        if digit == "0":
            countZero +=1
        else:
            break
    return countZero

print(BackZero(90))


