import arcade


class Player(arcade.AnimatedWalkingSprite):
    def __init__(self):
        super().__init__()
        self.walk_up_textures = [arcade.load_texture_pair("imgg\human_jump3.png")] 
        self.walk_right_textures = [arcade.load_texture_pair("imgg\human_w1.png"),arcade.load_texture_pair("imgg\human_w2.png"),arcade.load_texture_pair("imgg\human_w6.png"),arcade.load_texture_pair("imgg\human_w4.png"),arcade.load_texture_pair("imgg\human_w5.png"),arcade.load_texture_pair("imgg\human_w6.png")]
    
        self.width = 80
        self.height = 80
        self.center_x = 150
        self.center_y = 300
        self.score = 0
        self.control_speed = 0 
        self.frame = 0
        self.down = False

    def update_animation(self, delta_time: float = 1 / 60):
        if self.frame>=5:
            self.frame = 0
        else:
            self.frame +=1
            self.texture = self.walk_right_textures[self.frame][0]

    def manual_walkDown_animation(self):
        self.texture = arcade.load_texture("imgg/human_down.png")
        self.change_y -= 5
        