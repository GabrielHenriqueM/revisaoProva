def ordem_crescente(v):
    for i in range(len(v) - 1):
        if v[i] > v[i + 1]: 
            return False 
    return True 

vetor = [1, 5, 3, 4, 6]  
print(ordem_crescente(vetor))  
