def swap_sort(v):
    n = len(v)
    
    for i in range(n):
        for j in range(i + 1, n):
            if v[i] > v[j]:
                v[i], v[j] = v[j], v[i]
    
    return v

vetor = [5, 2, 9, 1, 4, 3]
print(swap_sort(vetor)) 

# O algoritmo é muito simples, com apenas uma troca de elementos quando necessário, e com menos comparações do que no Selection Sort, que compara todos os elementos.
# Embora a complexidade ainda seja O(n²), ele tenta minimizar as trocas e as comparações, o que pode ser um pouco mais eficiente em algumas situações.