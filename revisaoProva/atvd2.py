def inserir_em_ordem(x, v):
    v.append(x) 
    i = len(v) - 1  
    
    while i > 0 and v[i - 1] > v[i]:
        v[i - 1], v[i] = v[i], v[i - 1]  
        i -= 1
    
    return v

vetor = [1, 2, 4, 5]
x = 3
print(inserir_em_ordem(x, vetor))  
