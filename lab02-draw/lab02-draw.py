"""
This project was made by Emanuel Baciu and forked from github.com/dfbarrero.
Do not repost without permission.
"""

# We import the arcade library.
import arcade

# Summoning the window.
WIDTH = 900
HEIGHT = 900
arcade.open_window(WIDTH, HEIGHT, "Python paint n' color.")

# Change of background.
arcade.set_background_color(arcade.color.WHITE)

#Start of drawing.
arcade.start_render()

# Drawings
arcade.draw_circle_filled(450,450,300,color=arcade.color.YELLOW)
arcade.draw_circle_filled(315,500,50,color=arcade.color.BLACK)
arcade.draw_circle_filled(585,500,50,color=arcade.color.BLACK)
arcade.draw_arc_outline(
    450,
    370,
    350,
    250,
    color=arcade.color.BLACK,
    start_angle=180,
    end_angle=360,
border_width=20)

#End for drawing.
arcade.finish_render()

#Infinite Loop
arcade.run()


