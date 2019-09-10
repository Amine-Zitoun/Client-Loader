#!/usr/bin/env python
# coding: utf-8

# In[1]:


from tkinter import *
import sqlite3 as lite


# In[3]:



root = Tk()
root.geometry('860x750')
root.title('Enregister Une Malade')


con = lite.connect("db.db")
curr = con.cursor()


def submit():
    entry_list = [entry_1,entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8]

    print(entry_1.get(),
                                                             entry_2.get(),
                                                             entry_3.get(),
                                                             entry_4.get(),
         entry_5.get(),
         entry_6.get())



    try:
        curr.execute(' INSERT INTO DB(Nom,Pernom,NDossier,Doc,CIN,DG,REG) VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(entry_1.get(),
                                                                        entry_2.get(),
                                                                        entry_3.get(),
                                                                        entry_4.get(),
                                                                        entry_5.get(),
                                                                        entry_6.get(),
                                                                entry_7.get()))
    except Exception as e:
        curr.execute("CREATE TABLE DB( Nom TEXT NOT NULL,Pernom TEXT NOT NULL,NDossier INT NOT NULL,Doc TEXT NOT NULL,CIN INT NOT NULL, DG TEXT NOT NULL,REG TEXT NOT NULL,TEL INT NOT NULL)")
        curr.execute(' INSERT INTO DB(Nom,Pernom,NDossier,Doc,CIN,DG,REG) VALUES ("{}","{}","{}","{}","{}","{}","{}")'.format(entry_1.get(),
                                                                        entry_2.get(),
                                                                        entry_3.get(),
                                                                        entry_4.get(),
                                                                        entry_5.get(),
                                                                        entry_6.get(),
                                                                entry_7.get()))
    con.commit()
    for i in entry_list:
        i.delete(0,'end')


mycolor = '#%02x%02x%02x' % (66,544,232)
label_0 = Label(root,text="Enregistrement",width=20,font=("Times New Roman",28,'italic'),fg='blue')
label_0.place(x=232,y=53)


label_19 = Label(root,text="HOP REG GABES",width=20,font=("impact",15,'italic'),fg='black')
label_19.place(x=18,y=53)
label_20 = Label(root,text="SERVICE PSYCHIATRIE",width=20,font=("impact",15,'italic'),fg='black')
label_20.place(x=18,y=80)

label_1 = Label(root, text="Nom",width=20,font=('bold',15),fg='black')
label_1.place(x=1,y=130)

entry_1 = Entry(root,font=(30))
entry_1.place(x=182,y=130)



label2 = Label(root, text="PreNom",width=20,font=('bold',15),fg='black')
label2.place(x=1,y=200)


entry_2 = Entry(root,font=(30))
entry_2.place(x=182,y=200)

label_3 = Label(root, text="N° Doss",width=20,font=('bold',15),fg='black')
label_3.place(x=1,y=270)

entry_3 = Entry(root,font=(30))
entry_3.place(x=182,y=270)


label_4 = Label(root, text="Docteur",width=20,font=('bold',15),fg='red')
label_4.place(x=380,y=130)


entry_4 = Entry(root,font=(30))
entry_4.place(x=580,y=130)

label_5 = Label(root, text="CIN",width=20,font=('bold',15),fg='black')
label_5.place(x=1,y=350)

entry_5 = Entry(root,font=(30))
entry_5.place(x=182,y=350)


label_6 = Label(root, text="Diagnostic",width=20,font=('bolder',15),fg='red')
label_6.place(x=380,y=200)

entry_6 = Entry(root, width=30,font=(30))
entry_6.place(x=580,y=200)



label_7 = Label(root, text="Region",width=20,font=('bolder',15),fg='black')
label_7.place(x=1,y=430)

entry_7 = Entry(root, width=30,font=(30))
entry_7.place(x=182,y=430)

label_8 = Label(root, text="TEL",width=20,font=('bolder',15),fg='black')
label_8.place(x=1,y=510)

entry_8 = Entry(root, font=(30), width=30)
entry_8.place(x=182,y=510)

Button(root,text="OK",width=10,bg='brown',fg='white',height=2 ,font=('bolder',12),command=submit).place(x=350,y=650)
mainloop()


# In[6]:


Xconn=lite.connect("db.db")
Xc=Xconn.cursor()
sql = "SELECT * FROM db"
Xc.execute(sql)
print (Xc.fetchall()) #THIS SHOWS NO RECORDS


# In[ ]:
