import numpy as np

x = np.array([1.0 , 2.0, 3.0, 4.0, 5.0, 6.0]) # x coordinates 
y = np.array([14.5, 19.5, 30.5, 53.5, 94.5, 195.5]) # f(x)

def getNDDCoeffs(x, y):
    """ Membuat piramida NDD dan mengekstrak kopi """
    n = np.shape(y)[0]
    pyramid = np.zeros([n, n]) # Create a square matrix to hold pyramid
    pyramid[::,0] = y # first column is y
    for j in range(1,n):
        for i in range(n-j):
            # create pyramid by updating other columns
            pyramid[i][j] = (pyramid[i+1][j-1] - pyramid[i][j-1]) / (x[i+j] - x[i])
    return pyramid[0] # kembali baris pertama

coeff_vector = getNDDCoeffs(x, y)
print (coeff_vector)

# ...
# create as many polynomials as size of coeff_vector
final_pol = np.polynomial.Polynomial([0.]) # our target polynomial
n = coeff_vector.shape[0] # get number of coeffs
for i in range(n):
    p = np.polynomial.Polynomial([1.]) # create a dummy polynomial
    for j in range(i):
        # each vector has degree of i
        # their terms are dependant on 'x' values
        p_temp = np.polynomial.Polynomial([-x[j], 1.]) # (x - x_j)
        p = np.polymul(p, p_temp) # multiply dummy with expression
    p *= coeff_vector[i] # apply coefficient
    final_pol = np.polyadd(final_pol, p) # add to target polynomial

p = np.flip(final_pol[0].coef, axis=0)
print(p)
