import arcade
import time
import random
from player import Player
from ground import Ground, Cloud, Cloud1, Cloud2, Cloud3, Cloud4, Cloud5
from enemy import Enemy_Bee, Enemy_Co1, Enemy_Co2, Enemy_Co3, Enemy_Co4


class Game(arcade.View):
    def __init__(self):
        self.w = 800
        self.h = 700
        self.speed = 3
        super().__init__()
        arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
        self.player = Player()
        self.jump = arcade.load_sound(":resources:sounds/jump1.wav")
        self.background = arcade.load_texture("imgg/background_image.png")
        self.ground_list = arcade.SpriteList()
        self.cloud_list = arcade.SpriteList()
        self.cactoos_list = arcade.SpriteList()
        self.bee_list = arcade.SpriteList()
        self.score_max = 0
        self.count = 0
        self.gameover = False
        for ground in range(0,801,80):
            self.ground_list.append(Ground(ground,5))
        self.physic = arcade.PhysicsEnginePlatformer(self.player,self.ground_list,gravity_constant=0.5)
        self.start_cactoos_time = time.time()
        self.start_bee_time = time.time()
        self.start_cloud_time = time.time()
        
    def on_draw(self):
        arcade.start_render()
        self.player.draw()
        for ground in self.ground_list:
            ground.draw()
        for cactoos in self.cactoos_list:
            cactoos.draw()
        for bee in self.bee_list:
            bee.draw()
        for cloud in self.cloud_list:
            cloud.draw()

        if self.count % 20 == 0:
            arcade.set_background_color(arcade.color.BABY_BLUE_EYES)
        elif self.count % 10 ==0:
            arcade.set_background_color(arcade.color.EERIE_BLACK)
        arcade.draw_text(f"| {self.player.score}",630,670,arcade.color.BLACK_BEAN,20, italic=True, bold=True)
        arcade.draw_text(f"HI: {max(max_list)}",500,670,arcade.color.BLACK_BEAN,20, italic=True, bold=True)
        
        if self.gameover == True:
            arcade.draw_lrwh_rectangle_textured(0,0,self.w,self.h,self.background)
            arcade.draw_text("Game Over",230,400,arcade.color.WHITE_SMOKE,50,bold=True)
            arcade.draw_text("Press *Space* to Play Agane",230,330,arcade.color.GOLDEN_YELLOW,20)
            arcade.draw_text("Press *Q* to Exit Game ",250,280,arcade.color.GOLDEN_YELLOW,20)
            time.sleep(2)
                
    def on_update(self, delta_time: float):
        self.player.score +=0.5
        self.down = False
        self.end_cactoos_time = time.time()
        self.Co1 = Enemy_Co1(self.w,self.speed)
        self.Co2 = Enemy_Co2(self.w,self.speed)
        self.Co3 = Enemy_Co3(self.w,self.speed)
        self.Co4 = Enemy_Co4(self.w,self.speed)
        self.cloud = Cloud
        self.cloud1 = Cloud1()
        self.cloud2 = Cloud2()
        self.cloud3 = Cloud3()
        self.cloud4 = Cloud4()
        self.cloud5 = Cloud5()
        if self.end_cactoos_time - self.start_cactoos_time > random.randint(3,6):
            self.cactoos_list.append(random.choice([self.Co1,self.Co2,self.Co3,self.Co4]))
            self.count +=1
            if self.count % 5 == 0:
                self.speed += 0.5
            self.start_cactoos_time = time.time()
        
        self.end_bee_time = time.time()
        if self.end_bee_time - self.start_bee_time > 17 and self.player.score > 1000:
            self.cloud_list.append(random.choice([self.cloud,self.cloud1,self.cloud2,self.cloud3,self.cloud4,self.cloud5]))
            self.bee = Enemy_Bee(self.w,self.speed)
            self.bee_list.append(self.bee)
            self.start_bee_time = time.time()
        self.physic.update()
        if not self.player.down:
            self.player.update_animation()
        else:
            self.player.manual_walkDown_animation()

        for bee in self.bee_list:
            bee.update()
            bee.update_animation()
            if bee.center_x < -30:
                self.bee_list.remove(bee)
        for cactoos in self.cactoos_list:
            cactoos.update()
            if cactoos.center_x < -30:
                self.cactoos_list.remove(cactoos)
        for cloud in self.cloud_list:
            cloud.update()
            if cloud.center_x < -30:
                self.cloud_list.remove(cloud)

        for cactoos in self.cactoos_list:
            if arcade.sprite_list.spatial_hash.check_for_collision(self.player,cactoos):
                self.gameover = True
                max_list.append(self.player.score)
        for bee in self.bee_list:
            if arcade.sprite_list.spatial_hash.check_for_collision(self.player,bee):
                self.gameover = True
                max_list.append(self.player.score)

    def on_key_press(self,key,modifiers):
        if key== arcade.key.UP:
            if self.physic.can_jump():
                self.player.change_y = 18
                arcade.play_sound(self.jump)
        if key== arcade.key.SPACE:
            self.window.show_view(Game())
        if key== arcade.key.DOWN:
            self.player.down = True
        if key== arcade.key.Q:
            arcade.exit()
    
    def on_key_release(self,key,_modifiers):
            self.player.walk_down_texture = self.player.down = False
           
max_list = [0]
window = arcade.Window(800,700,"Game")
game = Game()
window.show_view(game)
arcade.run()