from display import *
from draw import *
from matrix import *
import math

screen = new_screen()
color = [ 255, 255, 0 ]

IDENT = new_matrix()
ident(IDENT)
all = []
A = []
cnx = []

add_edge(A, 75, 75, 0, 75, 25, 0)
add_edge(A, 75, 25, 0, 25, 25, 0)
add_edge(A, 25, 25, 0, 25, 75, 0)
add_edge(A, 25, 75, 0, 75, 75, 0)

for i in range(50):
    B = [[1.1, 0, 0, 0],[0, 1.05,0,0],[0,0,1,0],[0,0,0,1]]
    matrix_mult(B, A)
    count = len(all) - 8
    for pt in A:
        if(len(all) >= 8):
            add_edge(cnx, all[count][0], all[count][1], all[count][2], pt[0], pt[1], pt[2])
            count += 1
        all.append(pt[:])
        

draw_lines(cnx, screen, [250,5,5])
draw_lines(all, screen, color )
save_ppm(screen, "Img.ppm")
display(screen)
