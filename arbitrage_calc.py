def long(x):
    TGATE_LLY = 654.5
    IBIS_LLY = 655
    C = 4
    P = (IBIS_LLY * x - TGATE_LLY * x) - C
    return P

P = long(10)
#if P > 0:
    #print("buy TGATE, sell IBIS")
#print("return:",long(10))
!pip install y.finance

def short(y):
    TGATE_BYD = 24.16
    HKEX_BYD = 201.2
    C_TGATE = 2
    C_HKEX = 18 + y*HKEX_BYD*0.0000565 + 2 + y*HKEX_BYD*0.000027 + y*HKEX_BYD*0.0000015 + y*HKEX_BYD*0.001
    EURHKD = 8.3472
    p = (TGATE_BYD*y - HKEX_BYD/EURHKD*y) - (C_TGATE + C_HKEX/EURHKD)
    return p
    
TGATE_BYD = 24.16
cash = 6000
v = cash//TGATE_BYD
i = short(v)
if i > 0:
    print("sell TGATE, buy HKEX with volume of:",v)
elif i < 0:
    print("do not trade")
print("return:",short(v))

p = short(300)
#if p > 0:
#    print("sell TGATE, buy HKEX eith volume of:",5000//(y*TGATE_BYD))
#elif p < 0:
#    print("do not trade")
#print("return:",short(300))