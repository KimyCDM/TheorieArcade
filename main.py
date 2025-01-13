"""
Yul Kim
405
20 cercle et une affaire semblable a dvd
"""
import arcade
import random


exercise = int(input("1:20 boule,2:dvd "))


if exercise == 1:
    class MyGame(arcade.Window):

        def __init__(self, width, height, title):
            super().__init__(width, height, title)
            self.list_color = [arcade.color.BLUE, arcade.color.BROWN]
            self.cercle_amount = 0

        def on_draw(self):
            if self.cercle_amount == 20:
                pass
            else:
                x = random.randint(20, 620)
                y = random.randint(20, 460)
                arcade.draw_circle_filled(x, y, 20, random.choice(self.list_color))
                self.cercle_amount += 1


    def main():
        _ = MyGame(640, 480, "Drawing Example")
        arcade.run()


    main()

if exercise == 2:
    class MyGame(arcade.Window):

        def __init__(self, width, height, title):
            super().__init__(width, height, title)
            self.list_color = [arcade.color.BLUE]
            self.cercle_change_x = 10
            self.cercle_change_y = 10
            self.cercle_x = 100
            self.cercle_y = 100
            self.rayon_cercle = 20
            self.SCREEN_WIDTH = 500
            self.SCREEN_HEIGHT = 400

        def on_update(self, delta_time: float):
            self.cercle_x += self.cercle_change_x
            self.cercle_y += self.cercle_change_y
            if self.cercle_x < self.rayon_cercle:
                self.cercle_change_x *= -1
            if self.cercle_x > self.SCREEN_WIDTH - self.rayon_cercle:
                self.cercle_change_x *= -1
            if self.cercle_y < self.rayon_cercle:
                self.cercle_change_y *= -1
            if self.cercle_y > self.SCREEN_HEIGHT - self.rayon_cercle:
                self.cercle_change_y *= -1

        def on_draw(self):
            self.clear()
            arcade.draw_circle_filled(self.cercle_x, self.cercle_y, self.rayon_cercle, random.choice(self.list_color))

    def main():
        _ = MyGame(500, 400, "Drawing Example")
        arcade.run()

    main()
