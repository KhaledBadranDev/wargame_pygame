
"""
AUHTHOR: KHALED BADRAN
"""

import pygame


class Tank:

    def __init__(self, x, y):
        """ constructor of Tank class. 
        Args:
            x (int): x-coordinate of start point of the tank.
            y (int): y-coordinate of start point of the tank.
        """
        self.x = x
        self.y = y
        self.img = pygame.image.load("util/images/tank.png")
        self.health = 10
        self.fired_bullets = []
        self.max_bullets = 3


class TankBullet:   
        
    def __init__(self, x, y):
        """ constructor of TankBullet class. 
        Args:
            x (int): x-coordinate of start point of a bullet of the tank.
            y (int): y-coordinate of start point of a bullet of the tank.
        """
        self.x = x
        self.y = y
        self.img = pygame.image.load("util/images/tank_bullet.png")


class Soldier:

    def __init__(self, x, y):
        """ constructor of Soldier class. 
        Args:
            x (int): x-coordinate of start point of a soldier.
            y (int): y-coordinate of start point of a soldier.
        """
        self.x = x
        self.y = y
        self.img = pygame.image.load("util/images/soldier.png")
        self.fired_bullets = []
        self.max_bullets = 1
     

class SoldierBullet:
    
    def __init__(self, x, y):
        """ constructor of SoldierBullet class. 
        Args:
            x (int): x-coordinate of start point of the bullet of a soldier.
            y (int): y-coordinate of start point of the bullet of a soldier.
        """
        self.x = x
        self.y = y
        self.img = pygame.image.load("util/images/soldier_bullet.png")
