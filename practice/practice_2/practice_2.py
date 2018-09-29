'''
Task:
- Complete the Tank class, there is no need to alter the Gun class provided.
'''

class Gun:
    """
        Represents a Gun object.
    """
    ammo: int
    ammo_capacity: int

    def __init__(self, ammo: int, ammo_capacity: int):
        """
        Intialize instance variables.
        Note: ammo_capacity <= ammo
        """
        assert ammo_capacity <= ammo
        self.ammo = ammo
        self.ammo_capacity = ammo_capacity;

    def __str__(self):
        """
        Returns a string in the format of "ammo_capacity/ammo"
        """
        return str(self.ammo_capacity) + '/' + str(self.ammo)

class Tank(Gun):
    """
        Instance of a fighter
    """
    health: int
    armor: int
    gun: 'Gun'

    def __init__(self, health: int, armor: int, gun: 'Gun'):
        """
        Implement this method by initializing the instance variables.
        Expect to create a new Gun object, ensuring ammo_capacity <= ammo
        """
        pass

    def __str__(self):
        """
        Returns a string with a message representing the tank.
        "Tank: Health (100) - Armor (50) - Gun (40/50)"
        """
        pass

if __name__ == "__main__":
    """
    Initialize a tank object and print its string representation.
    """
    #t1 = Tank()
    #print(t1)
    pass
