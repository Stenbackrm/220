"""
Robert Stenback
button class file for three door game
"""
from graphics import Text

class Button:

    def __init__(self, Rectangle_shape, String_label):
        self.shape = Rectangle_shape
        self.text = Text(Rectangle_shape.getCenter(), String_label)

    """
     this class defines a button given its shape <Rectangle_shape> and its
     label <String_label>
     """

    def get_label(self):
        label = self.text.getText()
        return label
    def draw(self, win):
        self.shape.draw(win)
        self.text.draw(win)
    def undraw(self):
        self.shape.undraw()
        self.text.undraw()
    def is_clicked(self, point):
        p_1 = self.shape.getP1()
        p_2 = self.shape.getP2()
        width = abs(p_1.getX() - p_2.getX())
        height = abs(p_1.getY() - p_2.getY())
        x_a = point.getX()
        y_a = point.getY()
        d_x = abs((self.shape.getCenter()).getX() - x_a)
        d_y = abs((self.shape.getCenter()).getY() - y_a)
        return d_x <= width / 2 and d_y <= height / 2
    def color_button(self, color):
        self.shape.setFill(color)
    def set_label(self, label):
        self.text = self.text.setText(label)
