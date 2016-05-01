# -*- coding=utf-8 -*-
from pyarabic.unshape import unshaping_text
from pyarabic.araby import strip_tashkeel
from word import letter as key
input_text = unicode("1,بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ",'utf-8')
#input_text = "خَلِيفَةً"
stripped_text =  strip_tashkeel(input_text)
space_count = stripped_text.count(' ')
stripped_text = stripped_text.replace(' ','',space_count)
stripped_text = stripped_text.rstrip()
letter =  unshaping_text(stripped_text)

for i in letter:
    print i
uni_key = {}
for i in key.keys():
    uni_key[unicode(i,'utf-8')] = key[i]

sum_value = 0
for i in letter:
    try:
        sum_value = sum_value +uni_key[i]
    except:
        print "skip"
        print str(i)

print sum_value
# import pdb;pdb.set_trace()
# print list(letter)
# print key.keys()
# print sum_value
