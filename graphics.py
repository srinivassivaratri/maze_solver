from tkinter import Tk, BOTH, Canvas  # Import necessary components from tkinter for creating a graphical interface.

class Window:  # Define a blueprint for creating a window for our application.
    
    def __init__(self, width, height):  # Initialize a new window with given width and height.
        
        self.root = Tk()  # Create the main window of the application.
        self.root.title("Maze Solver")  # Set the title of the window to "Maze Solver".
        self.canvas = Canvas(self.root, bg="white", height=height, width=width)  # Create a drawing area inside the window.
        self.canvas.pack(fill=BOTH, expand=1)  # Make the drawing area fill the entire window.
        self.running = False  # Set a flag to indicate if the application is running or not.
        self.root.protocol("WM_DELETE_WINDOW", self.close)  # Set up a function to handle window closing.

    def redraw(self):  # Function to update the graphics in the window.
        
        self.root.update_idletasks()  # Update any pending tasks in the window.
        self.root.update()  # Update the window to reflect changes.

    def wait_for_close(self):  # Function to keep the window open until it is closed by the user.
        
        self.running = True  # Set the flag to indicate that the application is running.
        while self.running:  # Keep looping until the application is closed.
            self.redraw()  # Update the graphics in the window.
        print("window closed...")  # Print a message when the window is closed.

    def close(self):  # Function to close the window and stop the application..
        
        self.running = False  # Set the flag to indicate that the application should stop.
