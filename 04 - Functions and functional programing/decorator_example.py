def escape_unicode(f):
    def wrap(*args, **kwargs):
        x = f(*args, **kwargs)
        return ascii(x)
    return wrap

def northern_city():
    return "TromsØ")

print(northern_city())

@escape_unicode
def northern_city():
    return "TromsØ")

print(northern_city())


