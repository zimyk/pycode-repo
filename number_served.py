# -*- coding: utf-8 -*-
"""
Created on Mon May  6 22:54:54 2019

@author: Zigma
"""


class Restaurant():
    """ A simple model of a restaurant"""
    def __init__(self, restaurant_name, cuisine_type):
        """ Iniitailizes restaurrant name and cuisine"""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        """ Describes the restaurant name and cuisine type"""
        print(self.restaurant_name.title() + ' has served ', end='')
        print(str(self.number_served) + ' customers.')
        print(self.restaurant_name + ' is knowm for amazing ', end='')
        print(self.cuisine_type.title() + ' Cuisine')

    def open_restaurant(self):
        """ Describes the state of the restaurant"""
        print(self.restaurant_name.title() + " is open")

    def set_number_served(self, new_number):
        self.number_served = new_number

    def increment_number_served(self, increment_number):
        if increment_number >= self.number_served:
            self.number_served += increment_number
        else:
            print("We had low sales today")


def main():
    restaurant = Restaurant('njideka', 'local')
    restaurant.set_number_served(25)
    restaurant.increment_number_served(76)
    restaurant.describe_restaurant()


if __name__ == '__main__':
    main()
