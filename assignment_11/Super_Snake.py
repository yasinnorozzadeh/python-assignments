import random
import arcade
width = 650
height = 650
class Apple(arcade.Sprite):
    def __init__(self , w , h):
        arcade.Sprite.__init__(self)
        self.image = "apple.jpg"
        self.apple = arcade.Sprite(self.image, 0.03)
        self.apple.center_x = random.randint(10 ,w - 10)
        self.apple.center_y = random.randint(10 ,h - 10)
    def draw(self):
        self.apple.draw()

class Poop(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = "poop.jpg"
        self.poop = arcade.Sprite(self.image, 0.07)
        self.poop.center_x = random.randint(10, w - 10)
        self.poop.center_y = random.randint(10, h - 10)
    def draw(self):
        self.poop.draw()

class Pear(arcade.Sprite):
    def __init__(self, w, h):
        arcade.Sprite.__init__(self)
        self.image = "pear.jpg"
        self.pear = arcade.Sprite(self.image, 0.15)
        self.pear.center_x = random.randint(10, w - 10)
        self.pear.center_y = random.randint(10, h - 10)
    def draw(self):
        self.pear.draw()

class Snake(arcade.Sprite):
    def __init__(self , w , h):
        arcade.Sprite.__init__(self)
        self.color = arcade.color.DARK_OLIVE_GREEN
        self.speed = 3
        self.width = 16
        self.height = 16
        self.r = 8
        self.snake_score = 1
        self.center_x = w // 2
        self.center_y = h // 2
        self.change_x = 0
        self.change_y = 0
        self.body = []
        self.length = 0

    def draw(self):
        arcade.draw_circle_filled(self.center_x, self.center_y, self.r, self.color)
        self.body.append([self.center_x, self.center_y])
        for body_item in self.body:
            arcade.draw_circle_filled(body_item[0], body_item[1], self.r ,self.color)
        if len(self.body) > self.length:
            self.body.pop(0)

    def move(self):
        self.center_x += self.speed * self.change_x
        self.center_y += self.speed * self.change_y

    def score_food(self, snake_food):
        if snake_food == "apple":
            self.snake_score += 1
            self.length += 2
            self.speed += 0.05
        elif snake_food == "pear":
            self.snake_score += 2
            self.length += 3
            self.speed += 0.5
        elif snake_food == "poop":
            self.snake_score -= 1
            if self.snake_score == 0:
                arcade.draw_text('GAME OVER', width//2, height//2, arcade.color.BLACK, 5 * 5, width=width, align='left')
                arcade.exit()
            else:
                self.speed -= 1
                self.body.pop()

class Game(arcade.Window):
    def __init__ (self):
        arcade.Window.__init__(self, width, height, "super snake")
        arcade.set_background_color(arcade.color.SAND)
        self.snake = Snake(width, height)
        self.apple = Apple(width, height)
        self.pear = Pear(width, height)
        self.poop = Poop(width, height)
        self.txt = arcade.Camera(width, height)
        
    def on_draw(self):
        arcade.start_render()
        self.snake.draw()
        self.apple.draw()
        self.pear.draw()
        self.poop.draw()
        score = f"Score: {self.snake.snake_score}"
        arcade.draw_text(score, 10, 630, arcade.color.BLACK, 15, align='left')
        if self.snake.snake_score  <= 0 or self.snake.center_x < 0 or self.snake.center_x > width or self.snake.center_y < 0 or self.snake.center_y > height:
            arcade.draw_text('GAME OVER', width//2, height//2, arcade.color.BLACK, 5 * 5, width=width, align='left')
            arcade.exit()

    def on_update(self, delta_time: float):
        self.snake.move()
        if arcade.check_for_collision(self.snake, self.apple.apple):
            self.snake.score_food("apple")
            self.apple = Apple(width, height)
        elif arcade.check_for_collision(self.snake, self.pear.pear):
            self.snake.score_food("pear")
            self.pear = Pear(width, height)
        elif arcade.check_for_collision(self.snake, self.poop.poop):
            self.snake.score_food("poop")
            self.poop = Poop(width, height)

    def on_key_release(self, key, modifiers):
        if key == arcade.key.UP  or key == arcade.key.W:
            self.snake.change_x = 0
            self.snake.change_y = 1
        elif key == arcade.key.DOWN or key == arcade.key.S:
            self.snake.change_x = 0
            self.snake.change_y = -1
        elif key == arcade.key.LEFT or key == arcade.key.A:
            self.snake.change_x = -1
            self.snake.change_y = 0
        elif key == arcade.key.RIGHT or key == arcade.key.D:
            self.snake.change_x = 1
            self.snake.change_y = 0

Game()
arcade.run()
