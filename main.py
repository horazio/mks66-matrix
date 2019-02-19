from display import *
from draw import *
from matrix import *

screen = new_screen()
color = [ 0, 255, 0 ]

IDENT = new_matrix()
ident(IDENT)
A = []

add_edge(A, 1, 2, 3, 4, 5, 6)
print_matrix(A)

matrix_mult(IDENT, A)
print_matrix(A)

B = []
add_point(B, 1, 2, 3)
add_point(B, 4, 5, 6)
add_point(B, 7, 8, 9)
add_point(B, 10, 11, 12)

matrix_mult(B, A)

print_matrix(A)

#draw_lines( matrix, screen, color )
#display(screen)
