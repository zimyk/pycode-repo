# -*- coding: utf-8 -*-
"""
Created on Mon May 20 21:35:07 2019

@author: Zigma
"""


class Restaurant():
    """ A simple model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """ Iniitailizes restaurrant name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """ Describes the restaurant name and cuisine type"""
        print("The restaurant is " + self.restaurant_name.title() + ".")
        print("Known for their " + self.cuisine_type.title() + " Cuisine")

    def open_restaurant(self):
        """ Describes the state of the restaurant"""
        print(self.restaurant_name.title() + " is open")


class IceCreamStand(Restaurant):
    """Represents aspects of a restaurant specific to icecream"""
    def __init__(self, restaurant_name, cuisine_type):
        """initializes attributes from the parent class"""

        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []

    def display_flavor(self, flavors):
        """ Displays flavors of ice cream"""
        print("We offer the fpollowing flavors:")
        for flavor in flavors:
            print("- " + flavor.title())


ice_cream_flavors = ['vanila', 'strawberry', 'banana']
ice_cream = IceCreamStand('Cold Stone', 'Vanila Icecreanm')
ice_cream.display_flavor(ice_cream_flavors)
