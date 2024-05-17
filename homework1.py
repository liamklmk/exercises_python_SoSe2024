import matplotlib.pyplot as plt

def spar_func(A, S, i, l):
    kapital = A
    gesamt_kapital = []
    
    for k in range (1, l+1):
        kapital = S + kapital * (1 + i)
        gesamt_kapital.append(kapital)
        
    return gesamt_kapital

print(spar_func(10000, 1000, 0.01, 10))