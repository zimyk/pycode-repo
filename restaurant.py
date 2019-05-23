class Restaurant():
	""" A simple model of a restaurant"""
	
	def __init__(self, restaurant_name, cuisine_type):
		""" Iniitailizes restaurrant name and cuisine"""
		self.restaurant_name = restaurant_name
		self.cuisine_type = cuisine_type
		
	def describe_restaurant(self):
		""" Describes the restaurant name and cuisine type"""
		print("Our restaurant is " + self.restaurant_name.title() + ".")
		print("We are known for our " + self.cuisine_type.title())
	def open_restaurant(self):
		""" Describes the state of the restaurant"""
		print(self.restaurant_name.title() + " is open")
		
def main():
	restaurant = Restaurant('Njideka', 'intercontinental')
	print(restaurant.restaurant_name.title() + " is simply the best!")
	print("We offer " + restaurant.cuisine_type.title() + "Cuisine.")
	
	restaurant.describe_restaurant()
	restaurant.open_restaurant()	
if __name__ == '__main__':
	main()
