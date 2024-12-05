import pygame
import numpy as np
from pygame import surfarray

class PygameWindow:
    def __init__(self, width, height, title="Pygame Window"):
        # Initialize Pygame
        pygame.init()

        # Set the dimensions of the window
        self.width = width
        self.height = height

        # Create the window
        self.screen = pygame.display.set_mode((self.width, self.height))

        # Set the window title
        pygame.display.set_caption(title)

        # Initialize the background array (default to white)
        self.bg_array = np.full((self.height, self.width, 3), (255, 255, 255), dtype=np.uint8)

    def change_background(self, new_array):
        """
        Change the background of the window using a given numpy array.
        :param new_array: A numpy array of shape (height, width, 3) representing the new background
        """
        # Get the 3D pixel array of the screen
        screen_array = surfarray.pixels3d(self.screen)

        # Check if the new array's shape matches the screen's shape
        if new_array.shape == screen_array.shape:
            # Directly copy to the screen array if shapes match
            np.copyto(screen_array, new_array)
        else:
            # If shapes do not match, transpose new_array to match screen_array dimensions
            new_array_transposed = np.transpose(new_array, (1, 0, 2))  # Transpose (height, width, 3) to (width, height, 3)
            if new_array_transposed.shape == screen_array.shape:
                np.copyto(screen_array, new_array_transposed)
            else:
                print(f"Shape mismatch: new_array shape {new_array.shape}, screen_array shape {screen_array.shape}")

    def run(self):
        # Main loop to keep the window open
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                
                # Check if this script is run directly
                if __name__ == "__main__":  # Only execute this part if the script is run directly
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        # When mouse is clicked, make the background red
                        red_array = np.full((self.height, self.width, 3), (255, 0, 0), dtype=np.uint8)
                        self.change_background(red_array)
                        pygame.display.flip()  # Update the window to show the change

            # Update the window
            pygame.display.flip()  # Update the display

        # Quit Pygame
        pygame.quit()
    
    def stop(self):
        """
        Stops the app by quitting Pygame and closing the window.
        """
        pygame.quit()
        print("App has been stopped and Pygame quit.")


if __name__ == "__main__":
    # Create a Pygame window with width 800 and height 600
    window = PygameWindow(800, 600, "My Pygame Window")
    
    # Run the window (click to make red functionality is inside the run loop)
    window.run()
