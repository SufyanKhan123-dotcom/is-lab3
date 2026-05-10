
p = 17
a = 2
b = 2

# Point Addition
def point_add(P, Q):
    if P == Q:
        return point_double(P)

    x1, y1 = P
    x2, y2 = Q

    m = ((y2 - y1) * pow(x2 - x1, -1, p)) % p
    x3 = (m*m - x1 - x2) % p
    y3 = (m*(x1 - x3) - y1) % p

    return (x3, y3)

# Point Doubling
def point_double(P):
    x, y = P

    m = ((3*x*x + a) * pow(2*y, -1, p)) % p
    x3 = (m*m - 2*x) % p
    y3 = (m*(x - x3) - y) % p

    return (x3, y3)

# Scalar multiplication
def scalar_mult(k, P):
    result = P
    for _ in range(k-1):
        result = point_add(result, P)
    return result

# Base point
G = (5, 1)

# Private key
d = 3

# Public key
Q = scalar_mult(d, G)

print("Private Key:", d)
print("Public Key:", Q)

# Simple Encryption (concept)
message = 2
k = 2

C1 = scalar_mult(k, G)
C2 = (message + k) % p  

print("Cipher:", (C1, C2))

# Decryption
decrypted = (C2 - k) % p
print("Decrypted:", decrypted)