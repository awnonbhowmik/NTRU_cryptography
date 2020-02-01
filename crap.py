#=====================================================================================


# Finding the inverse of (x^2 + 1) modulo (x^4 + x + 1) using Extended Euclidean Algorithm in SageMath [GF(2^4)]
# By: Ngangbam Indrason

# Enter the coefficients of modulo n polynomial in a list from lower power to higher power
# Eg.: x^4 + x + 1 => 1.x^0 + 1.x^1 + 0.x^2 + 0.x^3 + 1.x^4
r1 = [-1,0,0,0,0,0,0,1]

# Enter the coefficients of polynomial to find inverse in a list from lower power to higher power
# Eg.: x^2 + 1 => 1.x^0 + 0.x^1 + 1.x^2
r2 = [1,-1,1,1,-1]

# Creating a copy of r1 and r2 in a and b respectively
a = list(r1)
b = list(r2)
itr = 1

def mod(a,b):
    return a%b

# Function to find degree of the polynimial
def getDegree(a):
    global deg
    for i in range(len(a)):
        if a[i] != 0:
            deg = i
    return deg

# Function to perform polynomial division: a1 = Dividend, b1 = Divisor
def doDivision(a1,b1):
    
    # Initialize quotient list with 0s of size as r1
    qq = [0]*len(r1)
    
    ai = getDegree(a1)
    bj = getDegree(b1)    
    
    while ai >= bj and 1 in a1:
        t_pow = ai-bj
        t_coeff = a1[ai]/b1[bj]
        
        qq[t_pow] = t_coeff
        
        # Initializing temporary list for intermediate products
        t_mul = [0]*len(r1)
        
        # Multipliying divisor with quotient
        for i in range(bj+1):
            t_mul[i+t_pow] = b1[i]*t_coeff
            
        # New intermediate dividend
        for i in range(len(a1)):
            a1[i] = mod(a1[i] - t_mul[i],2)
                 
        ai = getDegree(a1)
    
    return qq, a1

# Initialize t1 list as 0
t1 = [0]*len(r1)

# Initialize t2 list as 1
t2 = [0]*len(r1)
t2[0] = 1

# Initialize t list as 0
t = [0]*len(r1)

# Extended Euclidean Algorithm
while 1 in b:
    print('\n'+str(itr))
    print('Dividend: '+str(a))
    print('Divisor: '+str(b))
    quot, rem = doDivision(a,b)
    print('\nQuotient: '+str(quot))
    print('Remainder: '+str(rem))
    
    #Initializing intermediate list for quotient * t2
    t_qt2 = [0]*len(r1)
    d_quot = getDegree(quot)
    d_t2 = getDegree(t2)
    
    # Multipliying quotient and t2
    for i in range(d_quot+1):
        for j in range(d_t2+1):
            t_qt2[i+j] = t_qt2[i+j] + (quot[i] * t2[j])
        

    # Calculating t = t1 - quotient * t2
    for i in range(len(r1)):
        t[i] = mod(t1[i] - t_qt2[i],2)
    
    # Checking the degree of t: if deg(t) == deg(r1), then perform t = t modulo r1
    if getDegree(r1) == getDegree(t):
        print('\nt needs to perform modulo n')
        print('t_value before modulo: '+str(t))
        t_quo, t_rem = doDivision(t,r1)
        t = list(t_rem)
        
    
    print('\nt1: '+str(t1))
    print('t2: '+str(t2))
    print('t: '+str(t))
    a = list(b)
    b = list(rem)
    t1 = list(t2)
    t2 = list(t)

    itr = itr+1
    
# The result can be generated by rearranging the cofficients in the list from lower power to higher power    
print('\nInverse of the polynomial: '+str(t1))

#=========================================================================================

import sympy as sym
from sympy import GF

def make_poly(N, coeffs):
    """Create a polynomial in x."""
    x = sym.Symbol('x')
    coeffs = list(reversed(coeffs))
    y = 0
    for i in range(N):
        y += (x**i)*coeffs[i]
    y = sym.poly(y)
    return y

N = 7
p = 3
q = 41

#-x^4 + x^3 + x^2 - x + 1
#f = [-1,1,1,-1,1]
f = [1,0,-1,1,1,0,-1]

f_poly = make_poly(N,f)

x = sym.Symbol('x')

Fp = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(p, symmetric=False))
Fq = sym.polys.polytools.invert(f_poly,x**N-1,domain=GF(q, symmetric=False))

print('\nf =',f_poly)
print('\nFp =',Fp)
print('\nFq =',Fq)