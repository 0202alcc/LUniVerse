# THEMES.PY - Dynamic Theme Manager

# Define the axis of symmetry for color inversion (e.g., 255 for RGB)
AXIS_OF_SYMMETRY = 255

# Example light theme (add your own feature colors here)
LIGHT_THEME = {
    "background": (255, 255, 255),
    "text": (0, 0, 0),
    "primary": (100, 150, 200),
    "secondary": (180, 100, 50),
}

def invert_color(color: tuple, axis: int = AXIS_OF_SYMMETRY) -> tuple:
    """
    Inverts an RGB color based on the specified axis of symmetry.

    Args:
        color (tuple): RGB color as (R, G, B).
        axis (int): Axis of symmetry for inversion. Defaults to 255.

    Returns:
        tuple: Inverted RGB color.
    """
    return tuple(axis - c for c in color)

def compute_dark_theme(light_theme: dict, axis: int = AXIS_OF_SYMMETRY) -> dict:
    """
    Computes the dark theme dynamically by inverting the light theme colors.

    Args:
        light_theme (dict): Dictionary of light theme colors.
        axis (int): Axis of symmetry for inversion. Defaults to 255.

    Returns:
        dict: Dark theme colors.
    """
    return {key: invert_color(value, axis) for key, value in light_theme.items()}

def toggle_theme(is_dark_mode: bool, light_theme: dict, axis: int = AXIS_OF_SYMMETRY) -> dict:
    """
    Toggles between light and dark themes.

    Args:
        is_dark_mode (bool): Whether dark mode is enabled.
        light_theme (dict): Dictionary of light theme colors.
        axis (int): Axis of symmetry for inversion. Defaults to 255.

    Returns:
        dict: Active theme colors.
    """
    return compute_dark_theme(light_theme, axis) if is_dark_mode else light_theme

# Usage Example
if __name__ == "__main__":
    # Simulate a toggle between light and dark mode
    is_dark_mode = False
    active_theme = toggle_theme(is_dark_mode, LIGHT_THEME)
    print("Active Theme:", active_theme)

    # Switch to dark mode
    is_dark_mode = True
    active_theme = toggle_theme(is_dark_mode, LIGHT_THEME)
    print("Active Theme:", active_theme)

# -----------------------------------------------------------------------------
# NOTE: Future Implementation of Method 2 (Precomputing Both Themes)
# -----------------------------------------------------------------------------
# If performance becomes a bottleneck or theme toggling needs to be instantaneous:
#
# 1. Precompute the dark theme using `compute_dark_theme()` during initialization:
#       DARK_THEME = compute_dark_theme(LIGHT_THEME)
#
# 2. Store both themes explicitly in memory:
#       THEMES = {"light": LIGHT_THEME, "dark": DARK_THEME}
#
# 3. Modify `toggle_theme()` to return the precomputed theme instead of recalculating:
#       def toggle_theme(is_dark_mode: bool) -> dict:
#           return THEMES["dark"] if is_dark_mode else THEMES["light"]
#
# This approach trades storage space for faster theme switching and is suitable for:
# - High-frequency toggling scenarios (e.g., animations).
# - Applications with a large number of theme colors.
#
# -----------------------------------------------------------------------------
