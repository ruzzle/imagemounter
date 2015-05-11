from __future__ import print_function
from __future__ import unicode_literals

__ALL__ = ['Volume', 'Disk', 'ImageParser']
__version__ = '1.6.0b2'

BLOCK_SIZE = 512
VOLUME_SYSTEM_TYPES = ('detect', 'dos', 'bsd', 'sun', 'mac', 'gpt', 'dbfiller')
FILE_SYSTEM_TYPES = ('ext', 'ufs', 'ntfs', 'luks', 'lvm', 'xfs', 'iso', 'udf', 'fat',
                     'vmfs', 'squashfs', 'jffs2', 'cramfs', 'minix', 'dir', 'unknown')


from imagemounter import util
from imagemounter.parser import ImageParser
from imagemounter.disk import Disk
from imagemounter.volume import Volume
