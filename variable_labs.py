import math
percent = 1/3
coconut = 1450
macaw = 900
macaw_carry = macaw*percent
total_macaws = coconut/macaw_carry
print("it takes " + str(math.ceil(total_macaws)) + " macaws to carry a coconut")