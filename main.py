from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]
matrix = new_matrix(4, 10)
identity = new_matrix()
ident(identity)

A = [[1, 2, 3, 0],[4, 5, 6, 0],[7, 8, 9, 0], [7, 8, 9, 0]]
B = [[10, 20, 30, 1],[40, 50, 60, 1],[70, 80, 90, 1]]

print_matrix(A)
print_matrix(B)


matrix_mult(A, B)

print_matrix(B)

draw_lines( matrix, screen, color )
display(screen)
