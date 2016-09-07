# Matrix Algebra
import numpy as np

A = np.matrix([[1,2,3],[2,7,4]])
B = np.matrix([[1,-1],[0,1]])
C = np.matrix([[5,-1],[9,1],[6,0]])
D = np.matrix([[3,-2,-1],[1,2,3]])

u = np.array([6,2,-3,5])
v = np.array([3,5,-1,4])
w = np.array("1;8;0;5")

#Dimensions

print A.shape   # = (2,3)
print B.shape   # = (2,2)
print C.shape   # = (3,2)
print D.shape   # = (2,3)
print u.shape   # = (4)
print w.shape   # = ()

#Vector Operations

print u+v   # = [9,7,-4,9]
print u-v   # = [3,-3,-3,1]
print 6*u   # = [36,12,-18,30]
print u.dot(v)  # = 51
print np.linalg.norm(u) # = 8.60232

#Matrix Operations

#A + C gives you an error 
print A - C.T  # = [[-4 -7 -3],[ 3  6  4]]
print C.T + 3*D # = [[14  3  3],[ 2  7  9]]
print B*A   # = [[-1 -5 -1],[ 2  7  4]]

# B.dot(A.T) gives you an error

#Optional part
# B*C gives us an error
print C*B   # = [[ 5 -6], [ 9 -8], [ 6 -6]]
print B*B*B*B  # = [[ 1 -4], [ 0  1]]
print A*A.T   # = [[14 28], [28 69]]
print D.T*D   # = [[10 -4  0], [-4  8  8], [ 0  8 10]]


