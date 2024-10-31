brain.screen.set_pen_width(2)
brain.screen.set_pen_color(Color.BLACK)
brain.screen.draw_rectangle(0, 0, 480, 272, Color.0x74ac6c)
brain.screen.draw_rectangle(20, 20, 460, 252, Color.0x)
brain.screen.set_pen_color(0x5c8c5c)
brain.screen.draw_rectangle(3, 3, 476, 268)
brain.screen.draw_rectangle(18, 18, 444, 236)
brain.screen.set_pen_width(1)
brain.screen.draw_rectangle()
# 5c8c5c
# draw computer face to brain screen when function is called(be sure to move into function block later)
# screen resolution of 480x272

atonSwap
# the function for when the x button is pressed to switch to atonomous

controller.buttonX.pressed(atonSwap)

driverSwap
# function for going back to using the controller


controller.buttonY.press(driverSwap)