# -*- coding: utf-8 -*-
"""
Created on Sat May  4 11:12:01 2019

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


def main():
    my_rest = Restaurant('Inanie', 'chinese')
    print(my_rest.restaurant_name.title() + " Is the best in town!")
    print("Their " + my_rest.cuisine_type.title() + " is unrivaled")
    my_rest.describe_restaurant()

    their_rest = Restaurant('njideka', 'local')
    print("\n" + their_rest.restaurant_name.title() + "; best local recipe")
    print("Their " + their_rest.cuisine_type.title() + "cuisine; unmatched")
    their_rest.describe_restaurant()

    her_rest = Restaurant('chivaley', 'french')
    print("\n" + her_rest.restaurant_name.title() + " is very outstanding")
    print("They make amazing " + her_rest.cuisine_type.title() + " cuisine")
    her_rest.describe_restaurant()


if __name__ == '__main__':
    main()
