"""Main entry point for the example app."""

import utils

class Greeter:
    """Greets the user."""

    def __init__(self, name):
        """Initialize with a name."""
        self.name = name

    def greet(self):
        """Print a greeting."""
        print(f"Hello, {self.name}!")

def main():
    """Run the greeter."""
    g = Greeter("World")
    g.greet()

if __name__ == "__main__":
    main()
