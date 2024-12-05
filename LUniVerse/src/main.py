import pygame
from tools import draw_button, draw_circle  # Importing tools from tools.py
from pixel_controller import PixelController

def main():
    # Create an instance of PixelController
    controller = PixelController()

    # Add tools dynamically
    # controller.add_tool('draw_button', draw_button)
    # controller.add_tool('draw_circle', draw_circle)

    # Run the application
    controller.run()

if __name__ == "__main__":
    main()
