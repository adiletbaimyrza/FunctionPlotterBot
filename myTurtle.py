import plotter
import math



sec = plotter.Linear()
sec.set_dimensions(20)
sec.set_dot_size(3)
sec.set_mode('light')
sec.set_precision(110)
sec.set_tick(1)
sec.set_zoom(10)



sec.open_screen()



sec.draw_plane()



sec.plot_equation(2, 5)
