from tkinter import Tk, BOTH, Canvas

class Window:
    """Represents a graphical window for the Maze Solver application."""

    def __init__(self, width, height):
        """Initializes a new instance of the Window class.

        Args:
            width (int): The width of the window.
            height (int): The height of the window.
        """
        self.root = Tk()  # Create the root window of the application.
        self.root.title("Maze Solver")  # Set the title of the window.
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)  # Create a canvas widget for drawing graphics.
        self.canvas.pack(fill=BOTH, expand=1)  # Pack the canvas widget into the window.
        self.running = False  # Indicates whether the application is running or not.
        self.root.protocol("WM_DELETE_WINDOW", self.close)  # Set the close event handler.

    def redraw(self):
        """Redraws the window and updates the graphics.

        This method updates the graphics displayed in the window.
        It should be called whenever the graphics need to be updated.
        """
        self.root.update_idletasks()  # Update the idle tasks of the window.
        self.root.update()  # Update the window.

    def wait_for_close(self):
        """Waits for the window to be closed by the user.

        This method starts the main event loop of the window,
        which waits for the user to close the window.
        """
        self.running = True  # Set the running flag to True.
        while self.running:
            self.redraw()  # Redraw the window.

    def close(self):
        """Closes the window and stops the application.

        This method is called when the user closes the window.
        It stops the application and closes the window.
        """
        self.running = False  # Set the running flag to False.
