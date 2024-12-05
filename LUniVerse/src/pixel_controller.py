import pygame
import random
from tools import draw_button, draw_circle

class PixelController:
    def __init__(self, width=800, height=600):
        """Initialize the display window and variables."""
        self.width = width
        self.height = height
        self.running = True
        self.tools = {}  # Store tools as key-value pairs (name -> function)
        self.buttons = []  # Store buttons to track interactions
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Dynamic Pixel Controller")

        # Set universal font to Comic Sans MS and dark background
        self.font = pygame.font.SysFont('Comic Sans MS', 24)  # Comic Sans font
        self.bg_color = (30, 30, 30)  # Dark background color (dark gray)

    def add_tool(self, tool_name, tool_func):
        """Dynamically add a tool."""
        self.tools[tool_name] = tool_func

    def pixel_dance(self):
        """Create pixel dance effect in top-left and bottom-right quadrants."""
        # Top-left quadrant (0, 0) to (width // 2, height // 2)
        for _ in range(10):  # 10 random pixels in top-left
            x = random.randint(0, self.width // 2 - 1)
            y = random.randint(0, self.height // 2 - 1)
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.screen.set_at((x, y), color)

        # Bottom-right quadrant (width // 2, height // 2) to (width, height)
        for _ in range(10):  # 10 random pixels in bottom-right
            x = random.randint(self.width // 2, self.width - 1)
            y = random.randint(self.height // 2, self.height - 1)
            color = (random.randint(100, 255), random.randint(100, 255), random.randint(100, 255))
            self.screen.set_at((x, y), color)

    def update_button_hover(self, mouse_pos):
        """Update the hover effect for all buttons."""
        for button in self.buttons:
            button.update_hover(mouse_pos)

    def create_button(self):
        """Create a button and add it to the buttons list."""
        button = draw_button(self.screen, "Click Me", position=(100, 100), width=200, height=50)
        self.buttons.append(button)

    def run(self):
        """Main loop to handle events and update the display."""
        self.create_button()  # Ensure that we create buttons when the app starts
        
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                # Check for mouse movement and update hover state
                if event.type == pygame.MOUSEMOTION:
                    mouse_pos = pygame.mouse.get_pos()
                    self.update_button_hover(mouse_pos)

                # Check for button click events
                if event.type == pygame.MOUSEBUTTONDOWN:
                    mouse_x, mouse_y = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.contains((mouse_x, mouse_y)):
                            print("Button clicked!")

            self.screen.fill(self.bg_color)  # Apply the universal dark background

            self.pixel_dance()  # Apply the pixel dance effect in quadrants

            for button in self.buttons:
                button.draw()  # Draw all buttons

            pygame.display.flip()  # Update the display

        self.quit()

    def quit(self):
        """Clean up and close the application."""
        pygame.quit()
        print("Application closed.")
