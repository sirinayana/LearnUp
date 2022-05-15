import math

a = 32 / (math.sin((-35 * math.pi) / 4) * (math.cos((35 * math.pi) / 4)))
b = 24 / (math.sin(math.radians(127)) ** 2 + 1 + math.sin(math.radians(217)) ** 2)
c = math.sqrt(48) - math.sqrt(192) * math.sin(19 / 12 * math.pi) ** 2
d = (7 * math.sin(math.radians(11))) / math.cos(math.radians(79))

for c in (a, b, c, d):
    print(round(c, 5))
