import numpy as np
import random 
class Mat:
    def matMulCheck(a, b):
        return np.shape(a)[1] == np.shape(b)[0]
    def matMul(a, b):
        if Mat.matMulCheck(a, b) == True:
            return np.dot(a, b)
        else:print ("sorry, but the dimention is not satisfat")
    def augmentedMat(a, b):
        pass
    def solveLinearSystem(a, b):
        pass
    def isSubspace(S):
        pass
    def det(a):
        pass
la = np.random.randint(0, 10, size= (4,5))
lb = np.random.randint(0, 10, size= (5,2))
test = Mat.matMulCheck(la, lb)
