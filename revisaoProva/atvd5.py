def selection_sort_decrescente(v):
    n = len(v)
    for i in range(n):
        maior = i
        for j in range(i + 1, n):
            if v[j] > v[maior]:
                maior = j
        v[i], v[maior] = v[maior], v[i]
    return v

vetor = [5, 2, 9, 1]
print(selection_sort_decrescente(vetor)) 
