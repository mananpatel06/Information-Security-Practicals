import math

def checkPrime(n):
     k = math.sqrt(n)
     for i in range(3,int(k+1)):
         if n%i == 0:
            return False
     return True

def gcd(a,b):
     if b == 0:
        return a
     return gcd(b,a%b)

def get_public_key(phi):
     for i in range(2,10000):
         e = gcd(i,phi)
         if e == 1:
            return i
     return False 

def get_private_key(phi, e, t1, t2):
    global d
    if e == 0:
         d = t1
         return t1 

    get_private_key(e, phi%e, t2, t1-(phi//e)*t2)

def encrpyt(M, e, n):
    return (M**e)%n
def decrypt(C, d, n):
    return (C**d)%n

p = int(input("Enter First Prime number: "))

while not checkPrime(p):
     print(f'{p} is not a prime number. Try Again.')
     p = int(input("\nEnter First Prime number: "))

q = int(input("\nEnter Second Prime number: "))

while not checkPrime(q):
    print(f'{q} is not a prime number. Try Again.')
    q = int(input("\nEnter Second Prime number: "))

n = p*q
phi = (p-1)*(q-1)
e = get_public_key(phi)
if e:
    get_private_key(phi, e, 0, 1)
    if d<0:
        d = d+phi
    print(f'\nPublic ckey e = {e}, Private key d = {d}')
    M = int(input("\nEnter Your Message (Number): "))

    C = encrpyt(M, e, n)
    print(f"\nEncrypted Message: {C}")
    original_message = decrypt(C, d, n)
    print(f"\nDecrypted Message: {original_message}")
    print("\nMade by: Manan Patel ")
