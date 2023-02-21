import a_PlantClass as pc

primrose = pc.Plant("Green")  # creating an instance

sunflower = pc.Flower("Yellow", 12)  # creating an instance

print(primrose.get_color())

print(sunflower.get_color())
print(sunflower.get_petals())


# cant have a sub class access another supers classes attributes
# print(primrose.get_petals())
