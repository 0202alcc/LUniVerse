# Import the PygameWindow class from Window.py
from Window import PygameWindow
from tools import Shapes
import numpy as np
import pygame


class MainApp:
    def __init__(self):
        """
        Initialize the app by creating the Pygame window instance, lavender background, and setting isRunning to False.
        """
        self.window = PygameWindow(800, 600, "My Pygame Window")

        # Create a numpy array for the lavender color (RGB: 230, 230, 250)
        self.lavender_array = np.full((self.window.height, self.window.width, 3), (230, 230, 250), dtype=np.uint8)

        # Initialize the isRunning variable to False (app is not running initially)
        self.isRunning = False

        # Initialize the Shapes class with the window's screen
        self.shapes = Shapes(self.window.screen)

    def init(self):
        """
        Initialize the app by setting up the initial background color and running the window.
        """
        # Set the background color to lavender
        self.window.change_background(self.lavender_array)

        # Run the window (this will start the event loop and handle the window updates)
        self.window.run()

    def update(self):
        """
        Code that should be executed once, regardless of the app's state.
        This can be called before, during, or after the app's running.
        """
        print("Update method called.")

    def handle_events(self):
        """
        Handles all pygame events, including mouse clicks and dragging.
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.isRunning = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 3:  # Right-click to add a circle
                    self.shapes.add_circle(event.pos)
                elif event.button == 1:  # Left-click to select a circle
                    self.shapes.select_circle(event.pos)

            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:  # Release left click to drop the circle
                    self.shapes.selected_circle = None

            elif event.type == pygame.MOUSEMOTION:
                if self.shapes.selected_circle:  # Drag the selected circle
                    self.shapes.move_circle(event.pos)

    def while_running(self, func=None):
        """
        Code to run iteratively in the main loop. This can be customized.
        Sets isRunning to True when the app starts running.
        Accepts a function to run within the loop.
        """
        self.isRunning = True
        print("App is running...")

        while self.isRunning:
            self.handle_events()  # Handle mouse and other events
            self.window.screen.fill((230, 230, 250))  # Reset background to lavender
            self.shapes.draw_circles()  # Draw all circles
            pygame.display.flip()  # Update the display

            # If a function is provided, call it
            if func:
                func()

    def pause(self):
        """
        Pauses the app by resetting the isRunning flag to False.
        This stops the event loop and can be used to pause the app.
        """
        self.isRunning = False
        print("App is paused.")

    def stop(self):
        """
        Stops the app by quitting Pygame and closing the window.
        """
        self.window.stop()


if __name__ == "__main__":
    app = MainApp()  # Create an instance of MainApp

    # Call update method (this could be before the app starts, during, or after it's running)
    app.update()  # This will be executed regardless of the app state

    # Run the app
    app.while_running()
