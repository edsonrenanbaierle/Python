def fabonaci(N, n1, n2):
    if(N<=1):
        return N
    else:
        n3 = n1+n2
        if N == 2:
            print("{}". format(n3))
        else:
            print("{}". format(n3), end=' ')
        n1 = n2
        n2 = n3
        return fabonaci(N-1, n1, n2)





N = int(input())
n1 = 0
n2 = 1
print("{} {}".format(n1, n2), end=' ')
fabonaci(N-1, n1, n2)