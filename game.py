import arcade

window = arcade.Window(1024, 960, title="Tetris")
window.center_window()

class GameView(arcade.View):
    def __init__(self) -> None:
        super().__init__()

game = GameView()
window.show_view(game)
arcade.run()