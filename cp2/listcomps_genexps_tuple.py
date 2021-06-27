import collections
import sys
from collections import namedtuple

# list comprehensions and genexps:
symbols = "@#$%^"
list1 = [ord(i) for i in symbols]
list2 = list(filter(lambda c: c > 127, map(ord, symbols)))

colors = ["black", "white"]
sizes = ["S", "M", "L"]

# Cartesian Products in listcomps
listcomps = [(c, s) for c in colors for s in sizes]

# Cartesian Products in genexps 
generator = ((c, s) for c in colors for s in sizes)

print(sys.getsizeof(listcomps))
print(sys.getsizeof(generator))


# tuple:
# grap items using *：
a, b, *rest = range(5)
print(a, b, rest)

a, *rest, b = range(5)
print(a, b, rest)

# namedtuple：
City = namedtuple('City', "name country population coordinates")
tokyo = City('Tokyo', 
            country='JP',
            population="36.933", 
            coordinates=(35, 139))
print(tokyo.coordinates)
print(tokyo[1])

delhi_data = ('Delhi', 'India', 21.9, (28, 77))

print(City._fields)
delhi = City._make(delhi_data)
tokyo_dict = tokyo._asdict()
print(tokyo_dict)