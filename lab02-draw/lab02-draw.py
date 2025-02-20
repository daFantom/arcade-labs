"""
This project was made by Emanuel Baciu and forked from github.com/dfbarrero.
Do not repost without permission.
"""

# We import the arcade library.
import arcade
# Code
def draw_smiley_face(x:int,y:int):
    arcade.draw_circle_filled(450,450+y,300,color=arcade.color.YELLOW)
    arcade.draw_circle_filled(315,500+y,50,color=arcade.color.BLACK)
    arcade.draw_circle_filled(585,500+y,50,color=arcade.color.BLACK)
    arcade.draw_arc_outline(450,370+y,350,250,color=arcade.color.BLACK,start_angle=180,end_angle=360,border_width=20)

def main():
    WIDTH = 1200
    HEIGHT = 700
    arcade.open_window(WIDTH,HEIGHT,"Smiley Face")
    arcade.set_background_color(arcade.color.WHITE)
    arcade.start_render()
    draw_smiley_face(200,100)
    #Finish and run loop.
    arcade.finish_render()
    arcade.run()

main()



