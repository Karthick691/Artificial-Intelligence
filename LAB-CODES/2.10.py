
# Planet(Name, PositionFromSun, Type, NumberOfMoons)

planets = [
    ("mercury", 1, "rocky", 0),
    ("venus", 2, "rocky", 0),
    ("earth", 3, "rocky", 1),
    ("mars", 4, "rocky", 2),
    ("jupiter", 5, "gas_giant", 95),
    ("saturn", 6, "gas_giant", 146),
    ("uranus", 7, "ice_giant", 28),
    ("neptune", 8, "ice_giant", 16)
]

def gas_giant(p):
    return [x[0] for x in planets if x[2] == "gas_giant"]

def has_moons(p):
    return next((x[3] > 0 for x in planets if x[0] == p), False)

def closer_than(p1, p2):
    a = next(x[1] for x in planets if x[0] == p1)
    b = next(x[1] for x in planets if x[0] == p2)
    return a < b

def rocky_planets():
    return [x[0] for x in planets if x[2] == "rocky"]

print("Gas giants:", gas_giant(None))
print("Earth has moons:", has_moons("earth"))
print("Earth closer than Mars:", closer_than("earth", "mars"))
print("Rocky planets:", rocky_planets())
