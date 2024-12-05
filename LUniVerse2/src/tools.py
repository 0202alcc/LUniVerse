import pygame


class Shapes:
    def __init__(self, screen):
        """
        Initializes the Shapes class with a reference to the Pygame screen.
        :param screen: The Pygame screen where shapes will be drawn.
        """
        self.screen = screen
        self.circles = []  # List to store circles
        self.selected_circle = None  # Currently selected circle for dragging

    def add_circle(self, position, radius=20, color=(0, 0, 255)):
        """
        Adds a new circle at the specified position.
        :param position: Tuple (x, y) of the circle's center.
        :param radius: Radius of the circle.
        :param color: Color of the circle in RGB format.
        """
        circle = {"position": position, "radius": radius, "color": color}
        self.circles.append(circle)
        print(f"Circle added at {position}.")

    def select_circle(self, position):
        """
        Selects a circle if the click is within its radius.
        :param position: Tuple (x, y) of the mouse click.
        """
        for circle in self.circles:
            dist = ((position[0] - circle["position"][0]) ** 2 + (position[1] - circle["position"][1]) ** 2) ** 0.5
            if dist <= circle["radius"]:
                self.selected_circle = circle
                print(f"Circle selected at {circle['position']}.")
                break

    def move_circle(self, position):
        """
        Moves the selected circle to the specified position.
        :param position: Tuple (x, y) of the mouse position.
        """
        if self.selected_circle:
            self.selected_circle["position"] = position
            print(f"Circle moved to {position}.")

    def draw_circles(self):
        """
        Draws all circles onto the screen.
        """
        for circle in self.circles:
            pygame.draw.circle(self.screen, circle["color"], circle["position"], circle["radius"])
