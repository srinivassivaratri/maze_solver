from graphics import Window, Line, Point  # Import the Window class from the graphics module for creating a graphical window.

def main():  # Define the main function where the program execution starts.
    
    win = Window(800, 600)  # Create a window object with width 800 and height 600.
    c = Cell(win)
    c.has_left_wall = False
    c.draw(50, 50, 100, 100)
    # l = Line(Point(50,50), Point(400,400))
    # win.draw_line(l,"green")
    c = Cell(win)
    c.has_right_wall = False
    c.draw(125, 125, 200, 200)

    c = Cell(win)
    c.has_top_wall = False
    c.draw(300, 300, 500, 500)

    c = Cell(win)
    c.has_bottom_wall = False
    c.draw(225,225, 250, 250)
    
    win.wait_for_close()  # Wait for the user to close the window.

main()  # Call the main function to start the program execution...
