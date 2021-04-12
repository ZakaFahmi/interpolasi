def getRestultPolynomialLagrage(self, points):
    """ Keluaran berupa fungsi perkalian polynomial Lagrange """
    x, y = points
    final_pol = np.polynomial.Polynomial([0.])
    n = len(x) # banyak point
    for i in range(n):
        p = np.polynomial.Polynomial([1.]) # pembilang
        q = 1 # penyebut
        for j in range(n):
            if i == j:
                continue
            p_temp = np.polynomial.Polynomial([-x[j], 1.]) # x - x[j]
            p = np.polymul(p, p_temp)
            q_temp = x[i] - x[j] # x[i] - x[j]
            q *= q_temp
        p *= y[i]/q
        final_pol = np.polyadd(final_pol, p)
    p = np.flip(final_pol[0].coef, axis=0)
    return p