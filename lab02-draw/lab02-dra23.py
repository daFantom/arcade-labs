
"""
This project was made by Emanuel Baciu and forked from github.com/dfbarrero.
Do not repost without permission.
"""

# We import the arcade library.
import arcade
# Code
def draw_ytb_bg():
    arcade.draw_rectangle_filled(450, 300, 550, 350, color=arcade.color.DARK_BLUE_GRAY)
    arcade.draw_rectangle_filled(450,300,500,300,color=arcade.color.BLACK)
    arcade.draw_rectangle_filled(450, 200, 500, 10, color=arcade.color.GRAY)
    arcade.draw_circle_filled(220,200,10,color=arcade.color.RED)

def draw_loading_arc(x:int):
    arcade.draw_arc_outline(450,300,100,100,border_width=10,color=arcade.color.GRAY,start_angle=45,end_angle=198,tilt_angle=0+x)
    #arcade.draw_rectangle_filled(0,0,)

def on_draw(delta_time):
    arcade.start_render()

    draw_ytb_bg()
    draw_loading_arc(on_draw.draw_loading_arc1_x)
    on_draw.draw_loading_arc1_x += 1

on_draw.draw_loading_arc1_x = 0


def main():
    WIDTH = 900
    HEIGHT = 600
    arcade.open_window(WIDTH,HEIGHT,"Test")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.schedule(on_draw, 1 / 60)
    #Finish and run loop.
    arcade.run()

main()