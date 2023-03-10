""" Demostrate raiding a refrigerator """
from contextlib import closing

class RefrigeratorRaider:
    """ Raid a refrigerator"""

    def open(self):
        print("Open frige door.")

    def take(self, food):
        print(f"Finding {food}...")
        if food == "deep fried pizza":
            raise RuntimeError("Health warning!")
        print(f"Taking {food}")

    def close(self):
        print("Close frige door.")

def raid(food):
    with closing(RefrigeratorRaider()) as r:
        r = RefrigeratorRaider()
        r.open()
        r.take(food)
