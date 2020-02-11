def selection(L):
    for i in range(len(L)):
        pos = 0
        for j in range(len(L)-i):
            if L[pos] < L[j]:
                pos = j
        L[pos], L[j] = L[j], L[pos]
    print(L)





L = [12,31,10,22,19,7,51]
selection(L)