from .. import util

import bz2

opener = bz2.open

if __name__ == '__main__':
    util.write.main(opener)
