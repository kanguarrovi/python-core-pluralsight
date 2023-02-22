# print("executing multi-reader-program/__main__.py")

from demo_reader.multireader import MultiReader

import sys

filename = sys.argv[1]
r = MultiReader(filename)
print(r.read())
r.close()

