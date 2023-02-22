
#def hypervolume(*args):
#    print(args)
#    print(type(args))

def hypervolume(*lengths):
    i = iter(lengths)
    v = next(i)
    for length in i:
        v *= length
    return v


def hypervolume2(length, *lengths):
    v = length
    for item in lengths:
        v *= item
    return v


if __name__ == '__main__':
    print(hypervolume(3,4))
    print(hypervolume(3,4,5))
    print(hypervolume(2,4,6,8))
    print(hypervolume(1))



