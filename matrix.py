"""
A matrix will be an N sized list of 4 element lists.
Each individual list will represent an [x, y, z, 1] point.
For multiplication purposes, consider the lists like so:
x0  x1      xn
y0  y1      yn
z0  z1  ... zn
1  1        1
"""
import math

#print the matrix such that it looks like
#the template in the top comment
def print_matrix( matrix ):
    stri = ""
    for i in range(4):
        for l in matrix:
            stri += str(l[i]) + "\t"
        stri += "\n"
    print stri

#turn the paramter matrix into an identity matrix
#you may assume matrix is square
def ident( matrix ):
    for i in range(len(matrix)):
        for x in range(len(matrix)):
            if(i == x):
                matrix[i][x] = 1
            else:
                matrix[i][x] = 0

#multiply m1 by m2, modifying m2 to be the product
#m1 * m2 -> m2
#m1 is of size 4 by 4
def matrix_mult( m1, m2 ):
    for x in m2:

        temp = x[:]
        #x = [0] * 4

        x[0] = 0
        x[1] = 0
        x[2] = 0
        x[3] = 0
        
        for i in range(4):
            for l in range(4):
                x[i] += temp[l] * m1[i][l]



def new_matrix(rows = 4, cols = 4):
    m = []
    for c in range( cols ):
        m.append( [] )
        for r in range( rows ):
            m[c].append( 0 )
    return m
