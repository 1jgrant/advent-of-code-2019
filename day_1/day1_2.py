import math


module_masses = []
with open('day1_input.txt', 'r', encoding='utf8') as text:
    lines = text.read().splitlines()
    module_masses = [int(mass) for mass in lines]


def calculate_total_fuel(fuel_mass: int) -> int:
    if fuel_mass < 1:
        return 0
    extra_fuel = max(math.floor(fuel_mass / 3) - 2, 0)
    return extra_fuel + calculate_total_fuel(extra_fuel)


fuels = list(map(calculate_total_fuel, module_masses))
total = sum(fuels)
print(total)
