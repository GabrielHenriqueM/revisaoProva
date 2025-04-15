def insercao_recursiva(v, n=None):
    if n is None:
        n = len(v)
    if n <= 1:
        return v
    insercao_recursiva(v, n - 1)
    chave = v[n - 1]
    j = n - 2
    while j >= 0 and v[j] > chave:
        v[j + 1] = v[j]
        j -= 1
    v[j + 1] = chave
    return v

vetor = [5, 2, 9, 1]
print(insercao_recursiva(vetor)) 
