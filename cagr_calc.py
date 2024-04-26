def cagr_func(AK,EK,t):
    AK_abs = abs(AK)
    t_abs = abs(t)
    CAGR = ((EK/AK_abs)**(1/t_abs)-1) # *100
    return CAGR

print(cagr_func(100,700,30))

AK = 120
t = 30
cagr = cagr_func(100, 700, 30)
EK = AK * (1 + cagr)**t

print(EK)