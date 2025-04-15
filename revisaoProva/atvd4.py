def selecao_recursiva(v, n=None, i=0):
    if n is None:
        n = len(v)
    if i == n - 1:
        return v
    menor = i
    for j in range(i + 1, n):
        if v[j] < v[menor]:
            menor = j
    v[i], v[menor] = v[menor], v[i]
    return selecao_recursiva(v, n, i + 1)

vetor = [5, 2, 9, 1]
print(selecao_recursiva(vetor)) 
