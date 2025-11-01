#Write a Python program to create a dog class with one class variable and two instance variables, and display the details of dogs of two different breeds.

class Dog:
    species = "golden retriever"
    def __init__(self, AvgSize, skin_color):
        self.AvgSize = AvgSize
        self.skin_color = skin_color
dog1 = Dog("Large", "Golden")
dog2 = Dog("Medium", "Light Golden")
print("Dog Breed 1:")
print("Species:", dog1.species)
print("Average Size:", dog1.AvgSize)
print("Skin Color:", dog1.skin_color)
print("\nDog Breed 2:")
print("Species:", dog2.species)
print("Average Size:", dog2.AvgSize)
print("Skin color:", dog2.skin_color)
#Done! helped write it too. Not just AI!.