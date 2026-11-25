"""Solution to Ellen's Alien Game exercise."""


class Alien:
    """Create an Alien object with location x_coordinate and y_coordinate.

    Attributes:
        (class) total_aliens_created (int): Total number of Alien instances.
        x_coordinate (int): Position on the x-axis.
        y_coordinate (int): Position on the y-axis.
        health (int): Number of health points.

    Methods:
        hit(): Decrement Alien health by one point.
        is_alive(): Return a boolean for if Alien is alive (if health is > 0).
        teleport(new_x_coordinate, new_y_coordinate): Move Alien object to new coordinates.
        collision_detection(other): Implementation TBD.

    """

    total_aliens_created = 0
    
    def __init__(self, x_coordinate, y_coordinate):
        """Initialize an alien with position and health status.

        Args:
            x_coordinate (int): Horizontal value of alien position.
            y_coordinate (int): Vertical value of alien position.
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = 3
        Alien.total_aliens_created += 1

    
    def hit(self):
        """Hit and injure an alien."""
        if self.health > 0:
            self.health -= 1


    def is_alive(self):
        """Check if an alien is still alive.

        Returns:
            bool: True if the alien is alive, False otherwise.
        """
        return self.health > 0


    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move alien to a new position.

        Args:
            new_x_coordinate (int): New horizontal position of alien.
            new_y_coordinate (int): New vertical position of alien.
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate


    def collision_detection(self, other_object):
        """Check for collision with another object.
        
        Args:
            other_object (object): Another object to check collision against.
        """


def new_aliens_collection(alien_start_positions):
    """Create aliens.

    Args:
        alien_start_positions (list[tuple[int, int]]): Coordinates of alien positions.

    Returns:
        list[Alien]: A list of initializes alien instances.
    """
    aliens = []
    for coordinates_tuple in alien_start_positions:
        x_coordinate, y_coordinate = coordinates_tuple
        alien = Alien(x_coordinate, y_coordinate)
        aliens.append(alien)
    return aliens
