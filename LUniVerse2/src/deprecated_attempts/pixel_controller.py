import pygame
import numpy as np

class PixelController:
    def __init__(self, width, height, bg_color):
        self.width = width
        self.height = height
        self.bg_color = bg_color
        # Initialize Pygame and the display window
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))

    def update_display(self, pixel_matrix):
        """
        Takes in a NumPy matrix where each entry is an RGBA string and updates
        the Pygame display window accordingly.

        Parameters:
        - pixel_matrix (numpy.ndarray): A 2D matrix where each element is a string
                                         in the format 'rgba(r, g, b, a)'.
        """
        # Convert the string matrix to a NumPy array of integers
        rgba_array = np.array([self.convert_to_rgba(c) for c in pixel_matrix.flatten()])
        rgba_array = rgba_array.reshape((self.height, self.width, 4))

        # Update the display using Pygame's surfarray
        pygame.surfarray.blit_array(self.screen, rgba_array)
        pygame.display.flip()

    def convert_to_rgba(self, color_str):
        """
        Convert a string 'rgba(r, g, b, a)' to an RGBA tuple of integers.
        Example: 'rgba(255, 0, 0, 255)' -> (255, 0, 0, 255)

        Parameters:
        - color_str (str): A string representing an RGBA color.

        Returns:
        - tuple: A tuple of integers representing the RGBA values.
        """
        color_str = color_str.strip('rgba()')  # Remove 'rgba(' and ')'
        rgba = tuple(map(lambda x: int(x.strip()), color_str.split(',')))  # Strip spaces and convert to ints
        return rgba

    def run(self):
        """Main loop to keep the Pygame window open and responsive."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            pygame.time.wait(10)  # Control frame rate

        pygame.quit()
