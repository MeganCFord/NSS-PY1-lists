

planet_list = ["Mercury", "Mars"]
print(planet_list)

# Use append() to add Jupiter and Saturn at the end of the list.
planet_list.append("Jupiter")
planet_list.append("Saturn")
print(planet_list)

# Use the extend() method to add another list of the last two planets in our solar system to the end of the list.
planet_list.extend(["Uranus", "Neptune"])
print(planet_list)

# Use insert() to add Earth, and Venus in the correct order.
planet_list.insert(1, "Earth")
planet_list.insert(1, "Venus")
print(planet_list)

# Use append() again to add Pluto to the end of the list.
planet_list.append("Pluto")
print(planet_list)

# Now that all the planets are in the list, slice the list in order to get the rocky planets into a new list called rocky_planets. slice([start], stop[, step])
rocky_planets = planet_list[0:4]
rocky_planets.extend(planet_list[-1:])
print(rocky_planets)

# Being good amateur astronomers, we know that Pluto is now a dwarf planet, so use the del operation to remove it from the end of planet_list.
del planet_list[8]
print(planet_list)

# Create another list containing tuples. Each tuple will hold the name of a spacecraft that we have launched, and the names of the planet(s) that it has visited, or landed on. (e.g. ('Cassini', 'Jupiter')).
spacecraft = [
    ("Messenger", ["Mercury"]),
    ("Mariner 10", ["Mercury", "Venus"]),
    ("Mariner 1", ["Venus"]),
    ("Mariner 2", ["Venus"]),
    ("Mariner 5", ["Venus"]),
    ("Pioneer", ["Venus"]),
    ("Galileo", ["Venus", "Earth", "Jupiter"]),
    ("Magellan", ["Venus"]),
    ("Cassini", ["Venus", "Earth", "Jupiter", "Saturn"]),
    ("Venus Express", ["Venus"]),
    ("Messenger", ["Venus", "Earth"]),
    ("IKAROS", ["Venus"]),
    ("NEAR", ["Earth"]),
    ("Stardust", ["Earth"]),
    ("Rosetta", ["Earth"]),
    ("Deep Impact", ["Earth"]),
    ("Juno", ["Earth", "Jupiter"]),
    ("Mariner 3", ["Mars"]),
    ("Mariner 4", ["Mars"]),
    ("Mariner 6", ["Mars"]),
    ("Mariner 7", ["Mars"]),
    ("Mariner 9", ["Mars"]),
    ("Viking 1", ["Mars"]),
    ("Viking 2", ["Mars"]),
    ("Pathfinder", ["Mars"]),
    ("Sojourner", ["Mars"]),
    ("Odyssey", ["Mars"]),
    ("Opportunity", ["Mars"]),
    ("Phoenix", ["Mars"]),
    ("Dawn", ["Mars"]),
    ("Pioneer 10", ["Jupiter"]),
    ("Pioneer 11", ["Jupiter", "Saturn"]),
    ("Voyager 1", ["Jupiter", "Saturn"]),
    ("Voyager 2", ["Jupiter", "Saturn", "Uranus", "Neptune"]),
    ("Ulysses", ["Jupiter"]),
    ("New Horizons", ["Jupiter", "Pluto"])
]


# Iterate over your list of planets, and inside that loop, iterate over the list of tuples. Print, for each planet, which sattelites have visited.
def find_visitors():
    visitors = {}
    for planet in planet_list:
        visitors[planet] = [probe[0] for probe in spacecraft if planet in probe[1]]
    print(visitors)


find_visitors()
