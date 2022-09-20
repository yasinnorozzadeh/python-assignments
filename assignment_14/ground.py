import arcade
import random
class Ground(arcade.Sprite):
    def __init__(self,x,y):
        super().__init__(":resources:images/tiles/grassHalf_mid.png")
        self.width = 80
        self.height = 80
        self.center_x = x
        self.center_y = y 

class Cloud(arcade.Sprite):
    def __init__(self):
        super().__init__("imgg\cloud 1.png")
        self.width = 100
        self.height = 100
        self.center_x = 800
        self.center_y = random.randint(350, 650)
        self.change_x -= 0.5

class Cloud1(arcade.Sprite):
    def __init__(self):
        super().__init__("imgg\cloud 2.png")
        self.width = 100
        self.height = 100
        self.center_x = 800
        self.center_y = random.randint(350, 650)
        self.change_x -= 0.5

class Cloud2(arcade.Sprite):
    def __init__(self):
        super().__init__("imgg\cloud 3.png")
        self.width = 100
        self.height = 100
        self.center_x = 800
        self.center_y = random.randint(350, 650)
        self.change_x -= 0.5

class Cloud3(arcade.Sprite):
    def __init__(self):
        super().__init__("imgg\cloud 4.png")
        self.width = 100
        self.height = 100
        self.center_x = 800
        self.center_y = random.randint(350, 650)
        self.change_x -= 0.5

class Cloud4(arcade.Sprite):
    def __init__(self):
        super().__init__("imgg\cloud 5.png")
        self.width = 100
        self.height = 100
        self.center_x = 800
        self.center_y = random.randint(350, 650)
        self.change_x -= 0.5

class Cloud5(arcade.Sprite):
    def __init__(self):
        super().__init__("imgg\cloud 6.png")
        self.width = 100
        self.height = 100
        self.center_x = 800
        self.center_y = random.randint(350, 650)
        self.change_x -= 0.5
