"""
This project was made by Emanuel Baciu and forked from github.com/dfbarrero.
Do not repost without permission.
"""

# We import the arcade library.
import arcade

# --------Drawing functions--------

def draw_hand_grab():
    arcade.draw_rectangle_filled(740,220,35,200,color=(97, 77, 66))
    arcade.draw_rectangle_filled(740,307,35,25,color=(59, 47, 40))
    arcade.draw_circle_filled(740, 100, 40, color=arcade.color.ARSENIC)
    arcade.draw_circle_outline(740, 100, 30, color=arcade.color.BATTLESHIP_GREY)
    arcade.draw_circle_filled(740, 100, 28, color=(30, 31, 38))

def draw_blade_start():
    arcade.draw_rectangle_filled(740,480,80,120,color=arcade.color.RED)
    arcade.draw_triangle_filled(690,500,739,800,790,500, color= arcade.color.RED)
    arcade.draw_rectangle_filled(790,445,20,125,color=arcade.color.BAZAAR,tilt_angle=45)
    arcade.draw_rectangle_filled(690,445,20,125,color=arcade.color.BAZAAR,tilt_angle=-45)

def draw_handle_support():
    arcade.draw_triangle_filled(700,370,739,455,780,370, color= arcade.color.ARSENIC)
    arcade.draw_triangle_filled(700,330,630,355,700,380, color=arcade.color.ARSENIC)
    arcade.draw_triangle_filled(776,330,850,355,776,380, color=arcade.color.ARSENIC)
    arcade.draw_circle_filled(740,355,50,color=arcade.color.ARSENIC)
    arcade.draw_circle_outline(740,355,40,color=arcade.color.BATTLESHIP_GREY)
    arcade.draw_circle_filled(740,355,38,color=(30, 31, 38))

def draw_red_symbol():
    arcade.draw_rectangle_filled(740,375,35,6,color=arcade.color.RED)
    arcade.draw_rectangle_filled(740,353,4,50,color=arcade.color.RED)
    arcade.draw_rectangle_filled(745,340,40,4,color=arcade.color.RED,tilt_angle=-35)
    arcade.draw_rectangle_filled(724,335,15,4,color=arcade.color.RED,tilt_angle=45)
# Red Laser Blade
def draw_laser_blade():
    arcade.draw_rectangle_filled(690,500,20,125,color=arcade.color.BAZAAR)
    arcade.draw_rectangle_filled(790,500,20,125,color=arcade.color.BAZAAR)

#Bottom circles
#arcade.draw_circle_filled(740,100,40,color=arcade.color.ARSENIC)
#arcade.draw_circle_outline(740,100,30,color=arcade.color.BATTLESHIP_GREY)
# arcade.draw_circle_filled(740,100,28,color=(30, 31, 38))
def main():

    WIDTH = 1480
    HEIGHT = 900
    arcade.open_window(WIDTH, HEIGHT, "Python paint n' color.")

    # Change of background.
    arcade.set_background_color(arcade.color.BAZAAR)

    # Start of drawing.
    arcade.start_render()
    draw_hand_grab()
    draw_blade_start()
    draw_handle_support()
    draw_red_symbol()
    draw_laser_blade()

    # End of drawing and run loop.
    arcade.finish_render()
    arcade.run()

main()