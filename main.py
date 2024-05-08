from graphics import Window
from cell import Cell


def main():
    num_rows = 12
    num_cols = 16
    margin = 10
    screen_x = 800
    screen_y = 600
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows
    win = Window(screen_x, screen_y)
    
    win.wait_for_close()


main()