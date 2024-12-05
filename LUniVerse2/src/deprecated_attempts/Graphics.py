import pygame
import numpy as np
from pixel_renderer import GameWindow


class GameEngine:
    def __init__(self, width, height):
        """Initialize the game window and store the display state matrix."""
        self.window = GameWindow(width, height)
        self.width = width
        self.height = height
        self.display_state = np.ones((height, width, 3), dtype=np.uint8) * 255
        print(f"Initialized display_state with dimensions: {self.display_state.shape}")

    def get_display_state(self):
        """Return the current display state."""
        return self.display_state

    def single_update(self, new_state):
        """Update the display state with the given matrix and render it once."""
        if new_state.shape != (self.height, self.width, 3):
            raise ValueError(
                f"New state must have dimensions {(self.height, self.width, 3)}, but got {new_state.shape}"
            )
        self.display_state = new_state
        self.window.update(self.display_state)
        print("Display updated with single_update.")

    def apply_transformation(self, transformation_matrix):
        """
        Apply a linear algebra transformation to each pixel in the display state.
        :param transformation_matrix: A 3x3 matrix to transform RGB values.
        """
        # Validate transformation matrix dimensions
        if transformation_matrix.shape != (3, 3):
            raise ValueError(
                f"Transformation matrix must have dimensions (3, 3), but got {transformation_matrix.shape}"
            )

        # Apply the transformation to each pixel
        reshaped_state = self.display_state.reshape(-1, 3)  # Flatten to (height * width, 3)
        transformed_state = np.dot(reshaped_state, transformation_matrix.T)  # Apply transformation

        # Clip values to valid range [0, 255] and convert back to uint8
        transformed_state = np.clip(transformed_state, 0, 255).astype(np.uint8)

        # Reshape back to original dimensions
        self.display_state = transformed_state.reshape(self.height, self.width, 3)

        # Update the display
        self.single_update(self.display_state)

    def wait_for_user_close(self):
        """Keep the window open until the user decides to close it."""
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Close window on user request
                    running = False
                    self.window.quit()
                    print("Window closed by user.")


if __name__ == "__main__":
    engine = GameEngine(800, 600)

    # Define a transformation matrix (e.g., reduce red, boost green, invert blue)
    transformation_matrix = np.array([
        [0.5, 0.2, 0.0],  # Red channel transformation
        [0.1, 1.5, 0.0],  # Green channel transformation
        [0.0, 0.0, -1.0]  # Blue channel inversion
    ])

    # Apply the transformation
    print("Applying transformation...")
    engine.apply_transformation(transformation_matrix)

    # Keep the window open until the user closes it
    engine.wait_for_user_close()
