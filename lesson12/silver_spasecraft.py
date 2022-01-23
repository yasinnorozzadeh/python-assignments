import math
import random
import time
import arcade
DEFAULT_FONT_SIZE = 45
class Enemy(arcade.Sprite):
    def __init__(self , w , h , s= 3):
        super().__init__("doshman2.png")
        self.speed = s
        self.center_x = random.randint(0 , w)
        self.center_y = h
        self.width = 80
        self.height = 80
    # def shooot_racket_sound():
    #         arcade.play_sound(arcade.sound(":resources:sounds/hit3.wav"), 1.0 , 0.0 , False )
    def move(self):
        self.center_y -= self.speed
class Bullet(arcade.Sprite):
    def __init__(self , host):
        super().__init__("bullet2.png")
        self.speed = 4
        self.angle = host.angle
        self.center_x = host.center_x
        self.center_y = host.center_y
    def collision(self):
        arcade.play_sound(arcade.sound.Sound(':resources:sounds/laser4.wav'), 0.2, 0.0,False)
    def move(self):
        self.center_x -= self.speed * math.sin(math.radians(self.angle))
        self.center_y += self.speed * math.cos(math.radians(self.angle))
class SpaseCraft(arcade.Sprite):
    def __init__(self , w , h):
        super().__init__("khodi2.png")
        self.w = 48
        self.h = 48
        self.center_x = w // 2
        self.center_y = 85
        self.angel = 0
        self.change_angle = 0
        self.bullet_list = []
        self.speed = 4
        self.score = 0
        self.health = 3
    def rotate(self):
        self.angle += self.change_angle * self.speed
    def fire(self):
        self.bullet_list.append(Bullet(self))
class Game(arcade.Window):
    def __init__ (self):
        self.w = 700
        self.h = 700
        super().__init__(self.w , self.h , "Silver SpaceCraft")
        arcade.set_background_color(arcade.color.BLACK)
        self.bckground_image = arcade.load_texture("Bckgroundimage.jpg")
        self.me = SpaseCraft(self.w , self.h)
        self.enemy = Enemy(self.w , self.h)
        self.next_enemy_time = random.randint(2, 5)
        self.enemy_list = []
        self.game_start_time = time.time()
        self.start_time = time.time()
        self.health_image = arcade.load_texture("ghalb2.png")
    def on_draw(self):
        arcade.start_render()
        if self.me.health<=0:
            arcade.draw_text('GAME OVER', self.w//2-200, self.h//2, arcade.color.ORANGE, DEFAULT_FONT_SIZE //2, width=400, align='center')
        else:
            arcade.draw_lrwh_rectangle_textured(0, 0, self.w, self.h, self.bckground_image)
            self.me.draw()
            for i in range(len(self.me.bullet_list)):
                self.me.bullet_list[i].draw()
            for i in range(len(self.enemy_list)):
                self.enemy_list[i].draw()
            for i in range(self.me.health):
                arcade.draw_lrwh_rectangle_textured(10+i*35 ,10 ,30 ,30 ,self.health_image)
            arcade.draw_text('Score: %i'%self.me.score, self.w-130, 10, arcade.color.RED, DEFAULT_FONT_SIZE //2, width=200, align='left')
    def on_update(self, delta_time):
        self.end_time = time.time()
        if self.end_time - self.start_time > self.next_enemy_time:
            self.next_enemy_time = random.randint(2, 6)
            self.enemy_list.append(Enemy(self.w, self.h, 3+(self.end_time-self.game_start_time)//24))
            self.start_time = time.time()
        self.me.rotate()
        for i in range(len(self.me.bullet_list) ):
            self.me.bullet_list[i].move()
        for i in range(len(self.enemy_list)):
            self.enemy_list[i].move()
        for enemy in self.enemy_list:
            for bullet in self.me.bullet_list:
                if arcade.check_for_collision(bullet, enemy):
                    # self.enemy.shooot_racket_sound()
                    self.me.bullet_list.remove(bullet)
                    self.enemy_list.remove(enemy)
                    self.me.score += 1
        for enemy in self.enemy_list:
            if enemy.center_y < 0:
                self.me.health -= 1
                self.enemy_list.remove(enemy)
        for bullet in self.me.bullet_list:
            if bullet.center_y > self.height or bullet.center_x < 0 or bullet.center_x > self.width:
                self.me.bullet_list.remove(bullet)
    def on_key_press(self , key , modifiers):
        if key == arcade.key.RIGHT:
            self.me.change_angle = -1
        elif key == arcade.key.LEFT:
            self.me.change_angle = 1
        elif key == arcade.key.SPACE:
            self.me.fire()
            self.me.bullet_list[-1]
    def on_key_release(self , key ,  modifiers):
        self.me.change_angle = 0
def main():
    window = Game()
    window.center_window()
    arcade.run()
if __name__ == "__main__":
    main()
game = Game()
arcade.run()
