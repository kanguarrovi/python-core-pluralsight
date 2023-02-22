
class Trace:

    def __init__(self):
        self.enabled = True

    def __call__(self, f):
        def wrap(*args, **kwargs):
            if self.enabled:
                print(f'Calling {f}')
            return f(*args, **kwargs)
        return wrap

tracer = Trace()

@tracer
def rotate_list(l):
    return l[1:] + [l[0]]

l = [0, 1, 2]
l = rotate_list(l)

class IslandMaker:

    def __init__(self, suffix):
        self.suffix = suffix

    @tracer
    def make_island(self, name):
        return name + self.suffix

im = IslandMaker('Island')
im.make_island('Python')

