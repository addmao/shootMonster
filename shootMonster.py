import random
import arcade

SPRITE_SCALING = 0.5

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600



class Bullet(arcade.Sprite):
    def update(self):
        self.center_y += 6


class MyAppWindow(arcade.Window):

    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Tower Shoot!!")

        self.all_sprites_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()
        self.bullet_list = arcade.SpriteList()

        self.score = 0
        self.player_sprite = arcade.Sprite("images/Tower1.png",
                                           SPRITE_SCALING)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 90
        self.all_sprites_list.append(self.player_sprite)


        for i in range(100):

            coin = arcade.Sprite("images/Monster_easy1.png", SPRITE_SCALING / 3)
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(120, SCREEN_HEIGHT)

            self.all_sprites_list.append(coin)
            self.coin_list.append(coin)

        arcade.set_background_color(arcade.color.CYAN)

    def on_draw(self):

        arcade.start_render()

        self.all_sprites_list.draw()

        output = "Score: {}".format(self.score)
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):

        self.player_sprite.center_x = x

    def on_mouse_press(self, x, y, button, modifiers):

        bullet = Bullet("images/bulletOne.png", SPRITE_SCALING * 1.5)
        bullet.center_x = self.player_sprite.center_x
        bullet.bottom = self.player_sprite.top

        self.all_sprites_list.append(bullet)
        self.bullet_list.append(bullet)

    def animate(self, delta_time):
        self.all_sprites_list.update()

        for bullet in self.bullet_list:

            hit_list = arcade.check_for_collision_with_list(bullet,
                                                            self.coin_list)

            if len(hit_list) > 0:
                bullet.kill()

            for coin in hit_list:
                coin.kill()
                self.score += 1

            if bullet.bottom > SCREEN_HEIGHT:
                bullet.kill()


def main():
    MyAppWindow()
    arcade.run()


if __name__ == "__main__":
    main()
