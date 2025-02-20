
"""
This project was made by Emanuel Baciu and forked from github.com/dfbarrero.
Do not repost without permission.
"""

# We import the arcade library.
import arcade
# Code
def draw_bread():
    arcade.draw_arc_filled(450, 300, 100, 100, color=arcade.color.BLACK, start_angle=190, end_angle=45)
    arcade.draw_ellipse_filled(450,300,width=200,height=400,color=arcade.color.ALLOY_ORANGE,tilt_angle=-45)
def main():
    WIDTH = 900
    HEIGHT = 600
    arcade.open_window(WIDTH,HEIGHT,"Test")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    draw_bread()
    #Finish and run loop.
    arcade.finish_render()
    arcade.run()

main()