import MySQLdb
import os
#import test1_support
mydb=MySQLdb.connect(host="localhost",user="root",password="root",port=3306)
mycursor=mydb.cursor()
mycursor.execute("use `yarn register`")
L1,L2,L3,L4=[],[],[],[]
def funclist(L1,L2,L3,L4,L5):
    mycursor.execute("select buyer from buyer_master")
    L1=tuple([i[0] for i in mycursor.fetchall()])
    mycursor.execute("select yarn_count from yarn_count")
    L2=tuple([i[0] for i in mycursor.fetchall()])
    mycursor.execute("select yarn_shades from yarn_shades")
    L3=tuple([i[0] for i in mycursor.fetchall()])
    mycursor.execute("select shade_num from yarn_cardnum_shdnum_tbl")
    L4=tuple([i[0] for i in mycursor.fetchall()])
    mycursor.execute("select yarn_supplier from yarn_supplier")
    L5=tuple([i[0] for i in mycursor.fetchall()])    
    print("Imported drop-down items")
    return L1,L2,L3,L4,L5
"""
def cd():
    #L4,cd_num,combobox4

    mycursor.execute("select card_num from yarn_cardnum_shdnum_tbl")
    Lt=tuple([i[0] for i in mycursor.fetchall()])
    try:
        i=L4.index(test1_support.combobox4.get())
        test1_support.Entry6.set(Lt[i])
    except:
        print("NF")
"""
    
'''
self.cust1=test1_support.Custom(self.Frame1)
        self.cust1.enable_bindings()
        self.cust1.grid(row = 0, column = 0, sticky = "nswe")
'''
'''
import MySQLdb
import os
mydb=MySQLdb.connect(host="localhost",user="root",password="root",port=3306)
mycursor=mydb.cursor()
mycursor.execute("use `yarn register`")

import modt
L1,L2,L3,L4=[1,],[2,],[3,],[4,]
L1,L2,L3,L4=modt.funclist(L1,L2,L3,L4)
'''
'''
import modt
L1,L2,L3,L4=[1,],[2,],[3,],[4,]
L1,L2,L3,L4=modt.funclist(L1,L2,L3,L4)

def rfsh():
    print("re")
'''
#self.TCombobox1.bind("<Key-Return>",lambda x:self.Entry1.focus_set())
