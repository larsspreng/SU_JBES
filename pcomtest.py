"""
Function to implement intersection union of 
Spreng and Urga (2022) Combining p-Values for Multivariate Predictive
Ability Testing, Journal of Business and Economic Statistics
"""
import numpy as np

p_i = np.array([0.05, 0.02, 0.1, 0.0])

def pcom_test(p_i,alpha=0.05,r=10):

    if type(p_i) != np.ndarray:
        raise ValueError("Vector of p-values must be numpy array")

    n = p_i.size
    p_i[p_i<=10**(-4)] = 10**(-4)

    p_rn = np.sum(p_i**(-r))**(1/r)/n      # Test statistic
    pval = np.minimum(r/((r-1)*p_rn),1)    # p-value (proposition 1)
    cval = r/(alpha*(r-1));                # Critical value

    print(
        "---------------------------------------- \n"
        "Intersection Union Test: \n"
        "---------------------------------------- \n"
        "Test Statistic:", p_rn, "\n"
        "Critical Value:", cval, "\n"
        "p-value:", pval, "\n"
        "----------------------------------------"
     )

    if p_rn >= cval:
        print("Conclude: reject H_0")
    else:
        print("Conclude: do not reject H_0")
    print("----------------------------------------")

    return p_rn, pval, cval