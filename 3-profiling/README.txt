3a.
The loop that takes by far most of the runtime:
Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    23                                               # iterate through rows of X
    24       251        178.0      0.7      0.0      for i in range(len(X)):
    25                                                   # iterate through columns of Y
    26     63000      32559.0      0.5      0.1          for j in range(len(Y[0])):
    27                                                       # iterate through rows of Y
    28  15750250    8349404.0      0.5     37.2              for k in range(len(Y)):
    29  15687500   13605008.0      0.9     60.6                  result[i][j] += X[i][k] * Y[k][j]

specifically line 29 seems to be very costly.

Line 29 also uses the most memory as far as I can tell although th memery_profiler decorator seems to use even more.

3b.
the most time consuming function seems to be the factorize function, specifically these lines:

Line #      Hits         Time  Per Hit   % Time  Line Contents
==============================================================
    25     96347      25475.0      0.3     19.0      for p in primes:
    26    118736      42809.0      0.4     32.0          while(n%p == 0):
    27     22389       6873.0      0.3      5.1              n = n/p
    28     22389       7626.0      0.3      5.7              factors.append(p)
    29     96347      33565.0      0.3     25.1          if(p > sqrt(n)):

3c.
I would somehow have to speed up the nested loops of the:

# iterate through rows of X
for i in range(len(X)):
    # iterate through columns of Y
    for j in range(len(Y[0])):
        # iterate through rows of Y
        for k in range(len(Y)):
            result[i][j] += X[i][k] * Y[k][j]

replaced it with:
    23       251        222.0      0.9      0.0      for X_i, X_row in enumerate(X):
    24     62750      36109.0      0.6      0.2          for Y_i, Y_row in enumerate(Y):
    25  15750000    8371493.0      0.5     42.9              for Y_j, Y_val in enumerate(Y_row):
    26  15687500   10662243.0      0.7     54.6                  result[X_i][Y_j] += X_row[Y_i] * Y_val

It seems to be faster probably because you have to do less indexing at the final line
python matmult.py  2.98s user 0.03s system 97% cpu 3.087 total
python matmult_fast.py  2.38s user 0.02s system 96% cpu 2.484 total

about 2.38 is the best performance I can achieve.
