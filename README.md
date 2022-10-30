# Combining p-Values for Multivariate Predictive Ability Testing

This repo contains functions to implement the multivariate predictive ability test 
proposed in Spreng, L, Urga, G Combining p-Values for Multivariate Predictive Ability Testing,
*Journal of Business and Economic Statistics*

We provide Python and Matlab functions to implement the test. The input parameters for the significance level, $\alpha$,
and the parameter $r$ are optional. The default values are $\alpha = 0.05$ and $r=10$.


## Python Example

The vector of p-values provided by the user must be a numpy array. 

```python
    import numpy as np

    p_i = np.array([0.05,0.05,0.01,0.02])
    statistic, p_value, crit_val = pcom_test(p_i)
```


## MATLAB Example

``` matlab
    p_i = [0.05,0.05,0.01,0.02];

    [statistic, p_value, crit_val] = pcomtest(p_i);
```

