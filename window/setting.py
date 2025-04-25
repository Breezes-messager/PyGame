class Setting:
    def __init__(self):
        self.red = (255, 0, 0)
        self.green = (0, 255, 0)
        self.blue = (0, 0, 255)


class Player:
    def __init__(self):
        self.rect_x = 100
        self.rect_y = 100
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        self.speed = 5
