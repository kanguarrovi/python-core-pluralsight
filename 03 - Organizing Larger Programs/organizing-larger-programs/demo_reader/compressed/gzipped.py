from .. import util

import gzip

opener = gzip.open

if __name__ == '__main__':
    util.write.main(opener)

