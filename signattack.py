def h(n):
    return hex(n).replace("0x","")

def modinv(n, p):
    return pow(n, p - 2, p)

#rand2 = a * rand1 + b
a = 0x16
b = 0x22
k1 = 0xa4078095
k2 = 0xe18a50cf0
X = 0x40ef48e82e6aa909d9eef02e602d5bf374ea55c6ed6e689599c239efc4d7d16e
r1 = 0x4112df1f206da96e8ef62f6c2c04a55fa8271d4f32afe83051b9a2ef409e959c#
s1 = 0x99aa6d274daa023891e30b89c195654efea532ef26140f61aa5ccde09ce24eac#
r2 = 0xeb12d0155b6ef0ade1b9faf8e807bde6ef9e2100e7dd4010064dcade54fb8e7c
s2 = 0x23cfca0ee0e0fddd9cffbe4508b2ed40197705f6d8ffbda2987cbde3b7d383fc
m = 0x79be667ef9dcbbac55a06295ce870b07029bfcdb2dce28d959f2815b16f81798
N = 0xfffffffffffffffffffffffffffffffebaaedce6af48a03bbfd25e8cd0364141
pkey = (b - m * (s2^-1 - a * s1^-1)) / (r2 * s2^-1 - r1 * a * s1^-1)
print(h(pkey % N))
print(h((((m + (r1*X))*(modinv(s1,N))))%N))
print(h((((m + (r2*X))*(modinv(s2,N))))%N))
print(h((((m + (r1*X))*(modinv(s1,N))))%N))
print(h((((m + (r2*X))*(modinv(s2,N))))%N))
print(h((((m + (r1*X))*(modinv(s1,N))))%N))
print(h((((m + (r2*X))*(modinv(s2,N))))%N))
print(h((((s1 * k1)-m)*(modinv(r1,N)))%N))
print(h((((s2 * k2)-m)*(modinv(r2,N)))%N))
print(h((((s1 * k1)-m)*(modinv(r1,N)))%N))
print(h((((s2 * k2)-m)*(modinv(r2,N)))%N))
