from copy import deepcopy
import arcade
import letters
CELL_SIZE = 64
GRID_WIDTH = 12
GRID_HEIGHT = 15
GRID_H_SIZE = GRID_WIDTH * CELL_SIZE
GRID_V_SIZE = GRID_HEIGHT * CELL_SIZE
GRID_LINE_COLOR = (255,255,255,35)

STRAT_X = 4
STRAT_Y = 1

current_x = STRAT_X
current_y = STRAT_Y

class Grid:
    def __init__(self):
        self.main_grid = self.create()
        self.test_grid = deepcopy(self.main_grid)
        self.active_letters = letters.choose_random_letter()
        self.next_letter = None
        self.copy_letter_to_grid()
        self.letter_rotation = 1
        self.game_over = False
        self.cleared_row = 0

    def check_grids_is_in_wall(self) -> bool:
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.test_grid[y][x] == 8 and self.get_cell(x, y) != 8:
                    self.letter_rotation -= 1
                    return False
                elif self.test_grid[y][x] == 11 and self.get_cell(x, y) != 11:
                    self.letter_rotation -= 1
                    return False
                elif self.test_grid[y][x] == 12 and self.get_cell(x, y) != 12:
                    self.letter_rotation -= 1
                    return False
                elif self.test_grid[y][x] == 13 and self.get_cell(x, y) != 13:
                    self.letter_rotation -= 1
                    return False
                elif self.test_grid[y][x] == 14 and self.get_cell(x, y) != 14:
                    self.letter_rotation -= 1
                    return False
                elif self.test_grid[y][x] == 15 and self.get_cell(x, y) != 15:
                    self.letter_rotation -= 1
                    return False
                elif self.test_grid[y][x] == 16 and self.get_cell(x, y) != 16:
                    self.letter_rotation -= 1
                    return False
                elif self.test_grid[y][x] == 17 and self.get_cell(x, y) != 17:
                    self.letter_rotation -= 1
                    return False
        return True

    def can_whole_letter_move(self) -> bool:
        letter_can_move = []
        for y in range(GRID_HEIGHT-1, -1, -1):
            for x in range(GRID_WIDTH):
                if self.get_cell(x, y) == 1:
                    if self.get_cell(x, y + 1) == 0 or self.get_cell(x, y + 1) == 1:
                        letter_can_move.append(True)
                    else:
                        letter_can_move.append(False)
        return all(letter_can_move)

    def grid_copy(self,from_grid, to_grid) -> None:
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                to_grid[y][x] = from_grid[y][x]

    def try_move(self, x, y) -> bool:
        if self.get_cell(x, y) != 0:
            return False
        return True

    def move_left(self) -> None:
        global current_x
        breaker = False
        for x in range(GRID_WIDTH):
            if breaker:
                break
            for y in range(GRID_HEIGHT):
                if self.get_cell(x, y) == 1:
                    if self.try_move(x - 1, y):
                        self.set_cell(x, y, 0)
                        self.set_cell(x - 1, y, 1)
                    else:
                        breaker = True
                        break
        if not breaker:
            current_x -= 1

    def move_right(self) -> None:
        global current_x
        breaker = False
        for x in range(GRID_WIDTH-1, -1, -1):
            if breaker:
                break
            for y in range(GRID_HEIGHT):
                if self.get_cell(x, y) == 1:
                    if self.try_move(x + 1, y):
                        self.set_cell(x, y, 0)
                        self.set_cell(x + 1, y, 1)
                    else:
                        breaker = True
                        break
        if not breaker:
            current_x += 1

    def move_down(self) -> None:
        if not self.can_whole_letter_move():
            self.settle_letter()
            self.clear_full_rows()
            return

        global current_y
        breaker = False
        for y in range(GRID_HEIGHT - 1, -1, -1):
            if breaker:
                break
            for x in range(GRID_WIDTH):
                if self.get_cell(x, y) == 1:
                    if self.try_move(x, y + 1):
                        self.set_cell(x, y, 0)
                        self.set_cell(x, y + 1, 1)
                    else:
                        breaker = True
                        break
        if not breaker:
            current_y += 1

    def settle_letter(self) -> None:
        global current_y, current_x
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if self.get_cell(x, y) == 1:
                    self.set_cell(x, y, self.active_letters["settled_letter"])
        current_x = STRAT_X
        current_y = STRAT_Y
        self.letter_rotation = 1
        self.active_letters = self.next_letter
        self.copy_letter_to_grid()

    def draw_all(self) -> None:
        self.draw_lines()
        self.draw_walls()
        self.draw_letters()
        self.draw_next_letters()

    def draw_lines(self) -> None:
        for x in range(1, GRID_WIDTH):
            arcade.draw_line(
                x * CELL_SIZE, 0,
                x * CELL_SIZE, GRID_V_SIZE,
                GRID_LINE_COLOR,1
            )
        for y in range(1, GRID_HEIGHT):
            arcade.draw_line(
                0, y * CELL_SIZE,
                GRID_H_SIZE, y * CELL_SIZE,
                GRID_LINE_COLOR,2
            )

    def draw_walls(self) -> None:
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                square_x = x * CELL_SIZE
                square_y = (GRID_V_SIZE - CELL_SIZE) - y * CELL_SIZE
                if self.get_cell(x, y) == 8:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHEAT)
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, GRID_LINE_COLOR)

    def draw_letters(self) -> None:
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                square_x = x * CELL_SIZE
                square_y = (GRID_V_SIZE - CELL_SIZE) - y * CELL_SIZE
                if self.get_cell(x, y) == 1:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,self.active_letters["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE,arcade.color.WHITE)
                elif self.get_cell(x, y) == 11:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,letters.letter_T["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHITE, border_width=2)
                elif self.get_cell(x, y) == 12:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,letters.letter_o["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHITE, border_width=2)
                elif self.get_cell(x, y) == 13:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,letters.letter_left_l["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHITE, border_width=2)
                elif self.get_cell(x, y) == 14:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,letters.letter_right_l["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHITE, border_width=2)
                elif self.get_cell(x, y) == 15:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,letters.letter_I["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHITE, border_width=2)
                elif self.get_cell(x, y) == 16:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,letters.letter_z["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHITE, border_width=2)
                elif self.get_cell(x, y) == 17:
                    arcade.draw_lbwh_rectangle_filled(square_x, square_y, CELL_SIZE, CELL_SIZE,letters.letter_s["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x, square_y, CELL_SIZE, CELL_SIZE, arcade.color.WHITE, border_width=2)

    def draw_next_letters(self) -> None:
        for y in range(len(self.next_letter[1])):
            for x in range(len(self.next_letter[1][y])):
                if self.next_letter[1][y][x] == 1:
                    square_x = x * 60 + 32 + 790
                    square_y = (960 - 512) - y * 60 + 32
                    arcade.draw_lbwh_rectangle_filled(square_x,square_y,60,60,self.next_letter["color"])
                    arcade.draw_lbwh_rectangle_outline(square_x,square_y,60,60,arcade.color.WHITE, border_width=2)

    def create(self) -> list[list]:
        grid = []
        for y in range(GRID_HEIGHT):
            grid.append([])
            for x in range(GRID_WIDTH):
                if x == 0 or x == GRID_WIDTH - 1 or y == GRID_HEIGHT - 1:
                    grid[y].append(8)
                else:
                    grid[y].append(0)
        return grid

    def get_cell(self, x: int, y: int) -> int:
        return self.main_grid[y][x]

    def set_cell(self, x:int, y:int, value:int) -> None:
        self.main_grid[y][x] = value

    def copy_letter_to_grid(self) -> None:
        rot = self.active_letters[1]
        for y in range(len(rot)):
            for x in range(len(rot[y])):
                if rot[y][x] == 1:
                    if self.get_cell(x + STRAT_X, y + STRAT_Y) == 0:
                        self.set_cell(x + STRAT_X, y + STRAT_Y, 1)
                    else:
                        self.game_over = True
        self.next_letter = letters.choose_random_letter()

    def rotate_letter(self) -> None:
        self.clear_grid()
        self.letter_rotation += 1
        if self.letter_rotation > self.active_letters["num_of_rotations"]:
            self.letter_rotation = 1
        rot = self.active_letters[self.letter_rotation]
        for y in range(len(rot)):
            for x in range(len(rot[y])):
                if rot[y][x] == 1:
                    self.set_cell(x + current_x, y + current_y, 1)

    def clear_grid(self, all_cell = False) -> None:
        for y in range(GRID_HEIGHT):
            for x in range(GRID_WIDTH):
                if all_cell:
                    if self.get_cell(x, y) != 8:
                        self.set_cell(x, y, 0)
                else:
                    if self.get_cell(x, y) not in [8, 11, 12, 13, 14, 15, 16, 17]:
                        self.set_cell(x, y, 0)

    def clear_full_rows(self) -> None:
        y = GRID_HEIGHT - 1
        while y > 0:
            count = 0
            for x in range(GRID_WIDTH):
                if self.get_cell(x, y) != 8 and self.get_cell(x, y) > 10:
                    count += 1
            if count == 10:
                for yy in range(y, 1, -1):
                    for xx in range(GRID_WIDTH):
                        if self.get_cell(xx, yy) != 8:
                            cell_above = self.get_cell(xx, yy -1)
                            self.set_cell(xx,yy,cell_above)
                            self.set_cell(xx,yy-1,0)
                y = GRID_HEIGHT - 1
                self.cleared_row += 1
            y -= 1

    def restart(self) -> None:
        global current_x
        global current_y
        current_x = STRAT_X
        current_y = STRAT_Y
        self.clear_grid(True)
        self.active_letters = letters.choose_random_letter()
        self.next_letter = None
        self.letter_rotation = 1
        self.copy_letter_to_grid()
        self.game_over = False
        self.cleared_row = 0

if __name__ == "__main__":
    from pprint import pprint
    g = Grid()
    pprint(g.main_grid)