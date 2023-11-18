import numpy as np
import random 
class Mat:
    def matMulCheck(a, b):
        # return A.shape[1] == B.shape[0]
        return np.shape(a)[1] == np.shape(b)[0]
    def matMul(a, b):
        result = np.empty((np.shape(a)[0], np.shape(b)[1]))
        if Mat.matMulCheck(a, b) == True:
            for i in range (len(a)):
                for j in range (len(b[0])):
                    for k in range (len(b)):
                        result[i][j] += (a[i][k]*b[k][j])
            return result
        else:print ("sorry, but the dimention is not satisfat")
    def augmentedMat(a, b):
        augmented_matrix = np.concatenate((a, b.T), axis = 1)
        num_rows, num_cols = augmented_matrix.shape
        for i in range(num_rows):
            diagonal_element = augmented_matrix[i, i]
            augmented_matrix[i, :] /= diagonal_element
            for j in range(num_rows):
                if i != j:
                    factor = augmented_matrix[j, i]
                    augmented_matrix[j, :] -= factor * augmented_matrix[i, :]
        return augmented_matrix
    def solveLinearSystem(a, b):
        # if Mat.matMulCheck(a, b):
        #     x = np.linalg.solve(a, b)
        #     return x
        pass
    def isSubspace(S):
        # S = np.array(S)
        # rref, _ = np.linalg.qr(S)
        # return np.allclose(rref, np.round(rref))
        pass
    def det(a):
        # return np.linalg.det(a)
        pass
la = np.random.randint(0, 10, size= (2,4))
lb = np.random.randint(0, 10, size= (4,1))
print (la,"\n")
print (lb,"\n")
test = Mat.matMul(la, lb)
