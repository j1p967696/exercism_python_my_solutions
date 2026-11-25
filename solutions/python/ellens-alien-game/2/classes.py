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
    
    def __init__(self, x_coordinate, y_coordinate, health=3):
        """ Initialize an alien with position and health status.

        Parameters:
            x_coordiate (int): Horizontal value of alien position.
            y_coordinate (int): Vertical value of alien position.
            health (int): Initial health status of alien (3 points).

        Returns:
            Alien instance (Alien).
        """
        self.x_coordinate = x_coordinate
        self.y_coordinate = y_coordinate
        self.health = health
        Alien.total_aliens_created += 1

    
    def hit(self):
        """Hit and injure an alien."""
        if self.health > 0:
            self.health -= 1


    def is_alive(self):
        """Check if an alien is still alive.

        Returns:
            True or False (boolean).
        """
        if self.health == 0:
            return False
        return True


    def teleport(self, new_x_coordinate, new_y_coordinate):
        """Move alien to a new position.

        Parameters:
            new_x_coordinate (int): New horizontal position of alien.
            new_y_coordinate (int): New vertical position of alien.
        """
        self.x_coordinate = new_x_coordinate
        self.y_coordinate = new_y_coordinate


    def collision_detection(self, other_object):
        """Check for collision with another object"""
        pass


def new_aliens_collection(alien_start_positions):
    """Create aliens. 

    Parameters:
        alien_start_positions (List[tuples]): Coordinates of alien positions.

    Returns:
        Aliens (Alien): List of alien tuples.
    """
    aliens = []
    for coordinates_tuple in alien_start_positions:
        x_coordinate, y_coordinate = coordinates_tuple
        alien = Alien(x_coordinate, y_coordinate)
        aliens.append(alien)
    return aliens
