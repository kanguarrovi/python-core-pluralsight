# demo_reader/multireader.py

from demo_reader.compressed import bzipped, gzipped

import os

extension_map = {
    '.bz2': bzipped.opener
    '.gz': gzipped.opener
}

class MultiReader:

    def __init__(self, filename):
        extension = os.path.splitext(filename)[1]
        opener = extension_map
        self.filename = filename
        self.f = open(filename, 'rt')

    def close(self):
        self.f.close()

    def read(self):
        return self.f.read()


