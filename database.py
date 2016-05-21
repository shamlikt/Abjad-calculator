# -*- coding=utf-8 -*-
import sqlite3
from collections import OrderedDict

def connect_db():
    db = sqlite3.connect('data')
    cu = db.cursor()
    try:
        cu.execute('''CREATE TABLE abjid(id INTIGER PRIMARY KEY,letter TEXT,
        value INTIGER, label TEXT)''')
    except:
        # cu.execute(''' DROP TABLE abjid ''')
        # cu.execute('''CREATE TABLE abjid(id INTIGER PRIMARY KEY,letter TEXT,
        # value INTIGER, label TEXT)''')
        pass
    return db,cu
    
def insert_initial(db,cu):
    letter = OrderedDict()
    letter.update([(
    'ا',1),(
    'ب',2),(
    'ة',5),(
    'ت',400),(
    'ث',500),(
    'ج',3),(
    'ح',8),(
    'خ',600),(
    'د',4),(
        'ذ',700),(
        'ر',200),(
        'ز',7),(
        'س',60),(
        'ش',300),(
        'ص',90),(
        'ض',800),(
        'ط',9),(
        'ظ',900),(
        'ع',70),(
        'غ',100),(
        'ؽ',1),(
        'ف',80),(
        'ق',100),(
        'ك',20),(
        'ل',30),(
        'م',40),(
        'ن',50),(
        'ه',5),(
        'و',6),(
        'ى',10),(
        'ي',10),(
        'ء',1),(
        'أ',1),(
        'إ',1),(
        'آ',1),(
        'ؤ',1)])

    for i in letter:
        cu.execute('''INSERT INTO abjid(letter,value,label) values(?,?,?)''',(unicode(i,'utf-8'),letter[i],'one'))
    db.commit()

def fetch_data(label,cu):    
    data = cu.execute("SELECT letter,value FROM abjid WHERE label=?",(label,))
    return data

def insert_data(letter,value,label,cu,db):
    cu.execute('''INSERT INTO abjid(letter,value,label) values(?,?,?)''',(unicode(letter,'utf-8'),value,label))
    db.commit()
def update_data(letter_list, label):
    db,cu = connect_db()
    for letter,value in letter_list:
        print letter+"  "+value+"  "+label
        cu.execute('''UPDATE abjid SET value = ? WHERE letter = ? AND label = ?''',
        (value, letter, label))
    db.commit()

#db,cu = connect_db()
#insert_initial(db,cu)
# for i in fetch_data('one',cu):
#     print i
