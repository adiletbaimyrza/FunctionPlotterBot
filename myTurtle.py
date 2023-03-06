import quadratic
import linear
import trigonometric
import math
import plane


type = input()

coordinate_plane = plane.Plane()
coordinate_plane.draw_plane()

if type == 'linear':
    sec = linear.Linear()
    sec.draw(0.5, 2)
elif type == 'quadratic':
    sec2 = quadratic.Quadratic()
    sec2.draw(1, 2, 0)
elif type == 'trigonometric':
    sec3 = trigonometric.Trigonometric()
    sec3.draw(10, 0, math.sin)
