# -*- coding=utf-8 -*-
from letter2 import letter
a=file('word.py','w')
a.write("# -*- coding=utf-8 -*-\n")
a.write("letter = {\n")
for i in letter:
    a.write("'{}':{},\n".format(i,letter.index(i)))
a.write("}\n")
a.close()

from word import letter
print letter
print type(letter)
for i in a.keys():
    print i
    
