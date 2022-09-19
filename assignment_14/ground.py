import random
import arcade

class Enemy_Bee(arcade.AnimatedWalkingSprite):
    def __init__(self,x,s):
        super().__init__()
        self.walk_left_textures = [arcade.load_texture("imgg/bee_w1.png"),
                                    arcade.load_texture("imgg/bee_w2.png"),
                                    arcade.load_texture("imgg/bee_w3.png"),
                                    arcade.load_texture("imgg/bee_w4.png")]
        self.width = 5
        self.height = 5
        self.center_x = x
        self.center_y = random.randint(200, 300)
        self.change_x -= (s+1) 

class Enemy_Co1(arcade.Sprite):
    def __init__(self,x,s):
        super().__init__("imgg\c1.png")
        self.width = 80
        self.height = 100
        self.center_y = 90
        self.center_x = x
        self.change_x -= s

class Enemy_Co2(arcade.Sprite):
    def __init__(self,x,s):
        super().__init__("imgg\c2.png")
        self.width = 40
        self.height = 100
        self.center_x = x
        self.center_y = 90
        self.change_x -= s

class Enemy_Co3(arcade.Sprite):
    def __init__(self,x,s):
        super().__init__("imgg\c3.png")
        self.width = 70
        self.height = 100
        self.center_x = x
        self.center_y = 90
        self.change_x -= s

class Enemy_Co4(arcade.Sprite):
    def __init__(self,x,s):
        super().__init__("imgg\c4.png")
        self.width = 65
        self.height = 40
        self.center_x = x
        self.center_y = 65
        self.change_x -= s
