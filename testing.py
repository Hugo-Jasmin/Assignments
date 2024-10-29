def Fibbonaci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    fibonaci_list = [0,1]
    x = 2 
    while x < n:
        numberAdded = fibonaci_list[x-2]+fibonaci_list[x-1]
        fibonaci_list.append(numberAdded)
        x +=1
    print(fibonaci_list)
    return(fibonaci_list[n-1])
print(Fibbonaci(10))
