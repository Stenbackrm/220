'''
Robert Stenback's bumper car simulation
'''

import time
from random import randint
from graphics import Circle, GraphWin, Point, color_rgb

def get_random(move_amount):
    ran_move = randint(move_amount * -1, move_amount)
    return ran_move

def get_random_color():
    color = color_rgb(randint(1, 255), randint(1, 255), randint(1, 255))
    return color

def hit_horizontal(circle_ball, graphwin_win):
    upper_bound = graphwin_win.getHeight() - circle_ball.getRadius()
    lower_bound = circle_ball.getRadius()
    return circle_ball.getCenter().getY() >= upper_bound or \
           circle_ball.getCenter().getY() <= lower_bound


def hit_vertical(circle_ball, graphwin_win):
    right_bound = graphwin_win.getWidth() - circle_ball.getRadius()
    left_bound = circle_ball.getRadius()
    return circle_ball.getCenter().getX() >= right_bound or \
           circle_ball.getCenter().getX() <= left_bound


def did_collide(circle_ball_1, circle_ball_2):
    x_1 = circle_ball_1.getCenter().getX()
    y_1 = circle_ball_1.getCenter().getY()
    x_2 = circle_ball_2.getCenter().getX()
    y_2 = circle_ball_2.getCenter().getY()
    distance = ((x_1 - x_2) ** 2 + (y_1 - y_2) ** 2) ** .5

    avg_rad = (circle_ball_1.getRadius() + circle_ball_2.getRadius()) / 2
    return distance < avg_rad * 2


def main():
    win_height = 500
    win_width = 500
    title = 'bumper cars'
    move_amount = 10
    win = GraphWin(title, win_width, win_height)

    radius = 30
    start_point_1 = Point(randint(radius, win_width - radius),
                          randint(radius, win_height - radius))
    start_point_2 = Point(randint(radius, win_width - radius),
                          randint(radius, win_height - radius))

    circle_1 = Circle(start_point_1, radius)
    circle_1.setFill(get_random_color())
    circle_1.setOutline('black')
    circle_1.draw(win)

    circle_2 = Circle(start_point_2, radius)
    circle_2.setOutline('black')
    circle_2.setFill(get_random_color())
    circle_2.draw(win)

    ran_dx_1, ran_dy_1 = get_random(move_amount), get_random(move_amount)
    ran_dx_2, ran_dy_2 = get_random(move_amount), get_random(move_amount)

    dummy = True
    while dummy is True:
        time.sleep(.04)
        circle_1.move(ran_dx_1, ran_dy_1)
        circle_2.move(ran_dx_2, ran_dy_2)
        if hit_horizontal(circle_1, win) is True:
            ran_dy_1 = ran_dy_1 * -1
            circle_1.move(ran_dx_1, ran_dy_1)
        if hit_vertical(circle_1, win) is True:
            ran_dx_1 = ran_dx_1 * -1
            circle_1.move(ran_dx_1, ran_dy_1)
        if hit_horizontal(circle_2, win) is True:
            ran_dy_2 = ran_dy_2 * -1
            circle_2.move(ran_dx_2, ran_dy_2)
        if hit_vertical(circle_2, win) is True:
            ran_dx_2 = ran_dx_2 * -1
            circle_2.move(ran_dx_2, ran_dy_2)
        if did_collide(circle_1, circle_2) is True:
            ran_dx_1 = ran_dx_1 * -1
            ran_dy_1 = ran_dy_1 * -1
            ran_dx_2 = ran_dx_2 * -1
            ran_dy_2 = ran_dy_2 * -1
            circle_1.move(ran_dx_1, ran_dy_1)
            circle_2.move(ran_dx_2, ran_dy_2)
            circle_1.setFill(get_random_color())
            circle_2.setFill(get_random_color())

    win.getMouse()
if __name__ == '__main__':
    main()
