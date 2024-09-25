# Given the degree of two polynomials and the respective coefficients calculate the degree and the coefficients of the polynomial product. (input order: P1 degree; P1 coefficients; P2 degree; P2 coefficients)

degree1 = int(input())
coeffs1 = [float(input()) for i in range(degree1 + 1)]

degree2 = int(input())
coeffs2 = [float(input()) for i in range(degree2 + 1)]

total = degree1 + degree2

coefs = [0] * (total + 1)
    
for i in range(degree1 + 1):
    for j in range(degree2 + 1):
        coefs[i + j] += coeffs1[i] * coeffs2[j]

print(f"Degree of polynomial product= {total}")

for i in range(total + 1):
    print(f"coef {i} : {coefs[i]:.1f}")