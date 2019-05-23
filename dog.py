class Dog():
	""" A simple attempt to model a dog"""
	
	def __init__(self, name, age):
		""" Initializes name and age"""
		self.name = name
		self.age = age
	def sit(self):
		""" Simulates a dog sitting in response to a command"""
		print(self.name.title() + " is now sitting.")
	
	def roll_over(self):
		""" Simulate a dog that rolled over"""
		print(self.name.title() + " rolled over!")
def main():		
	my_dog = Dog('mayoe', 5)
	
	print("My dog's name is " + my_dog.name.title() + ".")
	print("My dog is " + str(my_dog.age) + " years old.")
	my_dog.sit()
	my_dog.roll_over()
	
if __name__ == '__main__':
	main()
		
