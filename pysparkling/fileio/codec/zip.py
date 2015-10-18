from __future__ import absolute_import

import zipfile
import logging
from io import BytesIO

from .codec import Codec

log = logging.getLogger(__name__)


class Zip(Codec):
    def __init__(self):
        pass

    def compress(self, stream):
        compressed = BytesIO()
        with zipfile.ZipFile(file=compressed, mode='w') as f:
            f.writestr('data', stream.read())
        return BytesIO(compressed.getvalue())

    def decompress(self, stream):
        uncompressed = BytesIO()

        with zipfile.ZipFile(file=stream, mode='r') as f:
            for f_name in f.namelist():
                uncompressed.write(f.read(f_name))

        uncompressed.seek(0)
        return uncompressed
