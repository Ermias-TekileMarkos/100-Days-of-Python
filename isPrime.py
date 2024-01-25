def isPrime(num):
    result = True
    count = 0
    for i in range (2,num):
        if (num % i == 0):
            count += 1
        if count != 0:
            result = False 
    return result

ans = isPrime(int(input("enter to check weather primr or not: ")))
print(ans)