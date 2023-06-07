import arcade

# Set up window dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self, width, height):
        super().__init__(width, height)
        self.player_x = width // 3
        self.score = 0
        self.highscore = 0

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.player_x -= 10
        elif key == arcade.key.RIGHT:
            self.player_x += 10
        
    def load_high_score(self):
        try:
            with open("high_score.txt", "r") as file:
                return file.read()
        except FileNotFoundError:
            return 0

    def save_high_score(self):
        with open("high_score.txt", "w") as file:
            file.write(str(self.high_score))

    def update(self, delta_time):
        if self.player_x > 330 and self.player_x < 470:
            self.score += 1
        self.high_score = int(self.load_high_score())
        if self.score > self.high_score:
            self.high_score = self.score
            self.save_high_score()

    def on_draw(self):
        arcade.start_render()
        arcade.draw_circle_filled(self.player_x, 50, 20, arcade.color.BLUE)
        arcade.draw_rectangle_filled(400, 50, 100, 50, arcade.color.RED)
        score_text = f"Score: {self.score}"
        arcade.draw_text(score_text, 10, 10, arcade.color.WHITE, 14)
        high_score_text = f"High Score: {self.high_score}"
        arcade.draw_text(high_score_text, 10, 30, arcade.color.WHITE, 14)

def main():
    game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT)
    arcade.run()

if __name__ == "__main__":
    main()
