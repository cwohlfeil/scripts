'''
Explicitly calling close closes the file handle, but only if the read was successful.
If there is any error just after f = open(...), f.close() will not be called
(depending on the Python interpreter, the file handle may still be returned, but that’s another story).
To make sure that the file gets closed whether an exception occurs or not, pack it into a with statement.

The first argument of open is the filename. The second one (the mode) determines how the file gets opened.

If you want to read the file, pass in r
If you want to read and write the file, pass in r+
If you want to overwrite the file, pass in w
If you want to append to the file, pass in a
If its a binary file, pass in b and the mode (rb to read binary)

Unfortunately, open does not allow explicit encoding specification in Python 2.x.
However, the function io.open is available in both Python 2.x and 3.x (where it is an alias of open),
and does the right thing. You can pass in the encoding with the encoding keyword.
If you don’t pass in any encoding, a system – and Python – specific default will be picked. Y
ou may be tempted to rely on these defaults, but the defaults are often wrong,
or the default encoding cannot actually express all characters in the file
(this will happen often on Python 2.x and/or Windows).
'''

import io

with open('photo.jpg', 'rb') as inf:
    jpgdata = inf.read()

if jpgdata.startswith(b'\xff\xd8'):
    text = u'This is a JPEG file (%d bytes long)\n'
else:
    text = u'This is a random file (%d bytes long)\n'

with io.open('summary.txt', 'w', encoding='utf-8') as outf:
    outf.write(text % len(jpgdata))