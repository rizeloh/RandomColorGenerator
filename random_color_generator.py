import random

def generate_random_color():
    """
    Generate a random color in HEX format.

    Returns:
    str: A randomly generated color code in HEX format.
    """
    # Generate random values for R, G, and B components
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    
    # Format the RGB values as a HEX color code
    hex_color = f'#{r:02x}{g:02x}{b:02x}'
    return hex_color

if __name__ == "__main__":
    # Generate a random color and print it
    random_color = generate_random_color()
    print(f"Generated HEX color code: {random_color}")
