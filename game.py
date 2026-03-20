import arcade
from grid import Grid
from enum import Enum, auto
window = arcade.Window(1024, 960, title="Tetris")
window.center_window()

class State(Enum):
    PAUSE = auto()
    PLAYING = auto()
    LOST = auto()


class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()
        self.grid = Grid()
        self.timer = 0
        self.state = State.PLAYING
        self.down_key_held = False

        self.cleared_row_text = arcade.Text("Cleared rows:", 832, 840, arcade.color.AERO_BLUE, 20)
        self.next_letter_text = arcade.Text("Next, Letter:", 832, 600, arcade.color.AERO_BLUE, 20)
        self.p_text = arcade.Text("Press P to Pause", 832, 80, arcade.color.AERO_BLUE, 15)
        self.esc_text = arcade.Text("Press Esc to exit", 832, 40, arcade.color.AERO_BLUE, 15)
        self.pause_text = arcade.Text("Game paused", 256, 480, arcade.color.YELLOW, 40)
        self.game_over_text = arcade.Text("Game Over", 256, 480, arcade.color.RED, 40)
        self.restart_text = arcade.Text("Press space to restart", 256 + 48, 440, arcade.color.AERO_BLUE)
        self.cleared_row_num_text = arcade.Text("0", 896, 800, arcade.color.AERO_BLUE, 25)

    def on_key_press(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.UP and self.state == State.PLAYING:
            self.grid.grid_copy(self.grid.main_grid, self.grid.test_grid)
            self.grid.rotate_letter()
            if not self.grid.check_grids_is_in_wall():
                self.grid.grid_copy(self.grid.test_grid, self.grid.main_grid)
        elif symbol == arcade.key.LEFT and self.state == State.PLAYING:
            self.grid.move_left()
        elif symbol == arcade.key.RIGHT and self.state == State.PLAYING:
            self.grid.move_right()
        elif symbol == arcade.key.P:
            if self.state == State.PLAYING:
                self.state = State.PAUSE
            else:
                self.state = State.PLAYING
        elif symbol == arcade.key.DOWN and self.state == State.PLAYING:
            self.down_key_held = True
        elif symbol == arcade.key.ESCAPE:
            arcade.exit()
        elif symbol == arcade.key.SPACE and self.state == State.LOST:
            self.grid.restart()
            self.state = State.PLAYING
    def on_key_release(self, symbol: int, modifiers: int) -> None:
        if symbol == arcade.key.DOWN and self.state == State.PLAYING:
            self.down_key_held = False

    def on_update(self, delta_time: float) -> None:
        if self.state == State.PLAYING:
            self.timer += delta_time
            if self.down_key_held and self.timer >= 0.05:
                self.grid.move_down()
                self.timer = 0
            else:
                if self.timer >= 0.5:
                    self.grid.move_down()
                    self.timer = 0
        if self.grid.game_over:
            self.state = State.LOST

    def on_draw(self) -> None:
        self.clear()
        self.grid.draw_all()
        self.cleared_row_text.draw()
        self.cleared_row_num_text.text = (str(self.grid.cleared_row))
        self.cleared_row_num_text.draw()
        self.next_letter_text.draw()

        self.p_text.draw()
        self.esc_text.draw()
        if self.state == State.PAUSE:
            self.pause_text.draw()
        elif self.state == State.LOST:
            arcade.draw_lbwh_rectangle_filled(256-128, 480-70, 512, 140, arcade.color.YANKEES_BLUE)
            self.game_over_text.draw()
            self.restart_text.draw()

game = GameView()
window.show_view(game)
arcade.run()

