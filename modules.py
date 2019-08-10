import coverters  # imports all the module
from coverters import lbs_to_kg  # imports specific module
from coverters import find_max

print(coverters.kg_to_lbs(56))
print(lbs_to_kg(130))

numbers = [1, 60, 20, 84, 105]

maximum = find_max(numbers)

print(maximum)
