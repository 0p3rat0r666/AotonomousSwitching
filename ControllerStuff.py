brain.screen.set_pen_color(Color.BLACK)
brain.screen.draw_rectangle(0, 0, 480, 272, Color.GREEN)
brain.screen.draw_rectangle(2, 2, 478, 270, Color.GREEN)
# draw computer face to brain screen when function is called(be sure to move into function block later)
# screen resolution of 480x272

atonSwap
# the function for when the x button is pressed to switch to atonomous

controller.buttonX.pressed(atonSwap)
