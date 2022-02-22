# Program to multiply two matrices using nested loops
import random

def main():
    N = 250
    
    # NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    
    # Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    
    # result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    
    for X_i, X_row in enumerate(X):
        for Y_i, Y_row in enumerate(Y):
            for Y_j, Y_val in enumerate(Y_row):
                result[X_i][Y_j] += X_row[Y_i] * Y_val
    
    for r in result:
        print(r)

if __name__ == '__main__':
    main()


