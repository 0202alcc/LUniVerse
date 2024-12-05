import pygame
import numpy as np

class GameWindow:
    def __init__(self, width, height, initial_color=(255, 255, 255)):
        """
        Initialize the window, set up the display, and blit the initial state.
        :param width: Width of the game window.
        :param height: Height of the game window.
        :param initial_color: RGB tuple for the initial background color.
        """
        self.width = width
        self.height = height

        # Initialize pygame display
        pygame.init()
        self.screen = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Game Window")

        # Create an initial NumPy array with the specified color
        self.initial_state = np.ones((height, width, 3), dtype=np.uint8)
        self.initial_state[:, :] = initial_color  # Set initial color

        # Convert the NumPy array to a pygame surface
        surface = pygame.surfarray.make_surface(self.initial_state)

        # Blit the surface onto the screen and update the display
        self.screen.blit(surface, (0, 0))
        pygame.display.update()

    def update(self, new_state):
        """
        Update the display with the new state (a numpy array).
        :param new_state: NumPy array representing the new state.
        """
        # Convert the numpy array (new_state) to a pygame surface
        surface = pygame.surfarray.make_surface(new_state)

        # Blit the surface onto the screen and update the display
        self.screen.blit(surface, (0, 0))
        pygame.display.update()

    def quit(self):
        """Quit the game and close the window."""
        pygame.quit()


# Example usage
if __name__ == "__main__":
    # Create the GameWindow instance with an initial blue background
    game_window = GameWindow(800, 600, initial_color=(0, 0, 255))

    # Create a NumPy array for the surface (height, width, 3 for RGB)
    array = np.zeros((600, 800, 3), dtype=np.uint8)

    # Fill the array with some data (e.g., a green screen)
    array[:, :] = [0, 255, 0]  # RGB color for green

    # Update the screen with the array
    # game_window.update(array)

    # Wait for a few seconds to observe the changes
    pygame.time.wait(3000)

    # Quit Pygame
    game_window.quit()
