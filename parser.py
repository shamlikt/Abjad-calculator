# -*- coding=utf-8 -*-

from pyarabic.unshape import unshaping_text
from pyarabic.araby import strip_tashkeel
import database

input_text = unicode("1,بِسْمِ اللَّهِ الرَّحْمَنِ الرَّحِيمِ",'utf-8')
def strip(input_text):
     return  strip_tashkeel(input_text)

def unshape(stripped_text):
    stripped_text = unshaping_text(stripped_text)
    return stripped_text.replace('\n','',stripped_text.count('\n'))

def format_text(stripped_text):
    space_count = stripped_text.count(' ')
    stripped_text = stripped_text.replace(' ','',space_count)
    return stripped_text.replace('\n','',stripped_text.count('\n'))

def parse(key,letter):
    uni_key = {}
    uni_key.update(key)
    sum_value = 0
    skip_letter = []
    for i in letter:
        try:
            sum_value = sum_value +uni_key[i]
        except:
            skip_letter.append(i)
    return sum_value,skip_letter


db,cu = database.connect_db()
database.insert_initial(db,cu)
key = database.fetch_data('one',cu)
stripped_text =  strip(input_text)
format_string = format_text(stripped_text)
letter = unshape(format_string)
print parse(key,letter)
