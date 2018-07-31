Hostname
from socket import gethostname; print gethostname()
import os; print os.uname()[1]


Find Platform
from sys import platform; print platform


compiles every .py file in the Python directory.
from compileall import compile_dir; compile_dir(<ptyhon dir>)


Simple Web Server
python -m http.server


Pretty Printing
from pprint import pprint


my_dict = {'name': 'Yasoob', 'age': 'undefined', 'personality': 'awesome'}
pprint(my_dict)


Profiling a script
python -m cProfile my_script.py


CSV to json
python -c "import csv,json;print json.dumps(list(csv.reader(open('csv_file.csv'))))"


List Flattening
a_list = [[1, 2], [3, 4], [5, 6]]
print(list(itertools.chain.from_iterable(a_list)))
# Output: [1, 2, 3, 4, 5, 6]

# or
print(list(itertools.chain(*a_list)))
# Output: [1, 2, 3, 4, 5, 6]


One-Line Constructors
class A(object):
    def __init__(self, a, b, c, d, e, f):
        self.__dict__.update({k: v for k, v in locals().items() if k != 'self'})


Want to know how many bytes a terabyte is?
import pprint;pprint.pprint(zip(('Byte', 'KByte', 'MByte', 'GByte', 'TByte'), (1 << 10*i for i in xrange(5))))


And what's the largest number that can be represented by 8 Byte?
print '\n'.join("%i Byte = %i Bit = largest number: %i" % (j, j*8, 256**j-1) for j in (1 << i for i in xrange(8)))


Set of all subsets
f = lambda x: [[y for j, y in enumerate(set(x)) if (i >> j) & 1] for i in range(2**len(set(x)))]
shorter
f = lambda l: reduce(lambda z, x: z + [y + [x] for y in z], l, [[]])


Decode a base64 encoded file
import base64, sys; base64.decode(open(sys.argv[1], "rb"), open(sys.argv[2], "wb"))


Editing a list of files in place
What this does is replace the substring "at" by "op" on all lines of all files (in place) under the path specified (here, the current path).
import sys,os,re,fileinput;a=[i[2] for i in os.walk('.') if i[2]] [0];[sys.stdout.write(re.sub('at','op',j)) for j in fileinput.input(a,inplace=1)]


echo unicode character:
python -c "print unichr(234)"


Compress CSS file
python -c 'import re,sys;print re.sub("\s*([{};,:])\s*", "\\1", re.sub("/\*.*?\*/", "", re.sub("\s+", " ", sys.stdin.read())))'


Decode string written in Hex
python -c "print ''.join(chr(int(''.join(i), 16)) for i in zip(*[iter('474e552773204e6f7420556e6978')]*2))"


Retrieve content text from HTTP data
python -c "import sys; print sys.stdin.read().replace('\r','').split('\n\n',2)[1]";


Prints file extension
print '~/python/one-liners.py'.split('.')[-1]