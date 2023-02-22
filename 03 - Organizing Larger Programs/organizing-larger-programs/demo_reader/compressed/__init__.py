from demo_reader.compressed.bzipped import opener as bz2_open
from demo_reader.compressed.gzipped import opener as gzip_opener

__all__ = ['bz2_opener', 'gzip_opener']
