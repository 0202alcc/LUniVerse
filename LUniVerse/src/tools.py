import pygame

class Button:
    def __init__(self, screen, text, position, width, height, shape="rectangle", hover_color=(255, 255, 255), normal_color=(0, 0, 0)):
        self.screen = screen
        self.text = text
        self.position = position
        self.width = width
        self.height = height
        self.shape = shape
        self.hover_color = hover_color
        self.normal_color = normal_color
        self.hovering = False
        
        # Initialize the rect for collision detection
        self.rect = pygame.Rect(position[0], position[1], width, height)
        
        # Initialize the font for the button text
        self.font = pygame.font.SysFont('Arial', 24)
        self.text_surface = self.font.render(self.text, True, (255, 255, 255))
        self.text_rect = self.text_surface.get_rect(center=self.rect.center)

    def draw(self):
        """Draw the button on the screen."""
        if self.hovering:
            pygame.draw.rect(self.screen, self.hover_color, self.rect)
        else:
            pygame.draw.rect(self.screen, self.normal_color, self.rect)
        
        # Draw the text on the button
        self.screen.blit(self.text_surface, self.text_rect)

    def contains(self, point):
        """Check if a point is inside the button."""
        return self.rect.collidepoint(point)

    def update_hover(self, mouse_position):
        """Update the hover status based on mouse position."""
        self.hovering = self.contains(mouse_position)

def draw_button(screen, text, position, width, height, shape="rectangle", hover_color=(255, 255, 255), normal_color=(0, 0, 0)):
    """Create a button and return it."""
    button = Button(screen, text, position, width, height, shape, hover_color, normal_color)
    return button

def draw_circle(screen, center, radius, color):
    """Draw a circle on the screen."""
    pygame.draw.circle(screen, color, center, radius)
