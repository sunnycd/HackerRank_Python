from math import erf
Sn = int(input())
n = int(input())
u = n * int(input())
std_dev = (n**0.5) *int(input())
print(round(0.5*(1 + erf((Sn-u)/(std_dev*(2**0.5)))), 4))
