import math


module_masses = []
with open('day1_input.txt', 'r', encoding='utf8') as text:
    lines = text.read().splitlines()
    module_masses = [int(mass) for mass in lines]

def fuel_from_mass(mass: int) -> int:
    return math.floor(mass / 3) - 2

fuels = list(map(fuel_from_mass, module_masses))
total = sum(fuels)
print(total)
