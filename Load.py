#!/usr/bin/env python
# coding: utf-8

# In[3]:


from tkinter import *
import sqlite3 as lite


# In[35]:


from tkinter import ttk



con = lite.connect("db.db")
curr = con.cursor()
root = Tk()
root.geometry('1450x750')
root.title('LOAD')
table = Frame(root)
table.pack(side="top", fill="both", expand=True)
table.place(x=150,y=380)




widgets={}




def select():
    curItem = listbox.focus()
    print (listbox.item(curItem))
    print( len(listbox.item(curItem)['values']))
    Name = listbox.item(curItem)['values'][0]
    pname = listbox.item(curItem)['values'][1]
    sql = "DELETE FROM db WHERE Nom = {}".format(Name)
    print(sql)
    curr.execute("DELETE FROM db WHERE Nom = '{}' AND Pernom= '{}'".format(Name,pname))

    sql = "SELECT * FROM db"
    curr.execute(sql)
    print (curr.fetchall())
    con.commit()
    listbox.delete(curItem)





def load():
    entry_list = [entry_2,entry_3,entry_4,entry_5,entry_6,entry_7,entry_8]

    pre = entry_2.get()
    nd = entry_3.get()
    doc = entry_4.get()
    cin = entry_5.get()
    reg = entry_6.get()
    nom = entry_7.get()
    dg = entry_8.get()
    if (pre != '' and nd == '' and doc == '' and cin == '' and reg == ''):
        #listbox.delete(1, END)
        for i in listbox.get_children():
            listbox.delete(i)
        curr.execute( "SELECT * FROM DB WHERE Pernom='{}' ORDER BY Nom ".format(pre))


        for index,row in enumerate(curr.fetchall()):
            listbox.insert("", "end", values=(row[0], row[1], row[2],row[6],row[4],row[5],row[3]))
            #listbox.insert(END, str(row[0])+ ' '*20 + str(row[1])+' '*20 +   str(row[2])+' '*20 +   str(row[3])+' '*20 +   str(row[4])+' '*20 +   str(row[5]))
    if (pre == '' and nd != '' and doc == '' and cin == '' and reg == ''):
        #listbox.delete(1, END)
        for i in listbox.get_children():
            listbox.delete(i)
        curr.execute( "SELECT * FROM DB WHERE NDossier='{}' ORDER BY Nom ".format(nd))

        for index,row in enumerate(curr.fetchall()):
            listbox.insert("", "end", values=(row[0], row[1], row[2],row[6],row[4],row[5],row[3]))
        #    print(row)
        #    listbox.insert(END, str(row[0])+ ' '*20 + str(row[1])+' '*20 +   str(row[2])+' '*20 +   str(row[3])+' '*20 +   str(row[4])+' '*20 +   str(row[5]))
    if (pre != '' and nd == '' and doc!= '' and cin == '' and reg == ''):
        #listbox.delete(1, END)
        for i in listbox.get_children():
            listbox.delete(i)
        curr.execute( "SELECT * FROM DB WHERE Doc='{}' ORDER BY Nom".format(doc))

        for index,row in enumerate(curr.fetchall()):
            listbox.insert("", "end", values=(row[0], row[1], row[2],row[6],row[4],row[5],row[3]))
        #    print(row)
        #    listbox.insert(END, str(row[0])+ ' '*20 + str(row[1])+' '*20 +   str(row[2])+' '*20 +   str(row[3])+' '*20 +   str(row[4])+' '*20 +   str(row[5]))
    if (pre == '' and nd == '' and doc == '' and cin != '' and reg == ''):
        for i in listbox.get_children():
            listbox.delete(i)
        curr.execute( "SELECT * FROM DB WHERE CIN='{}' ORDER BY Nom ".format(cin))

        for index,row in enumerate(curr.fetchall()):
            print(row)
            listbox.insert("", "end", values=(row[0], row[1], row[2],row[6],row[4],row[5],row[3]))
    if (pre =='' and nd == '' and doc == '' and cin == '' and reg != ''):
        for i in listbox.get_children():
            listbox.delete(i)
        curr.execute( "SELECT * FROM DB WHERE REG='{}' ORDER BY Nom ".format(reg))

        for index,row in enumerate(curr.fetchall()):
            print(row)
            listbox.insert("", "end", values=(row[0], row[1], row[2],row[6],row[4],row[5],row[3]))
    if (pre =='' and nd == '' and doc == '' and cin == '' and reg == '' and nom!='' and dg == ''):
        for i in listbox.get_children():
            listbox.delete(i)
        curr.execute( "SELECT * FROM DB WHERE NOM='{}' ORDER BY Nom ".format(nom))

        for index,row in enumerate(curr.fetchall()):
            print(row)
            listbox.insert("", "end", values=(row[0], row[1], row[2],row[6],row[4],row[5],row[3]))
    if (pre =='' and nd == '' and doc == '' and cin == '' and reg == '' and nom=='' and dg != ''):
        for i in listbox.get_children():
            listbox.delete(i)
        curr.execute( "SELECT * FROM DB WHERE DG='{}' ORDER BY Nom ".format(dg))

        for index,row in enumerate(curr.fetchall()):
            print(row)
            listbox.insert("", "end", values=(row[0], row[1], row[2],row[6],row[4],row[5],row[3]))

        #    print(row)
        #    listbox.insert(END, str(row[0])+ ' '*20 + str(row[1])+' '*20 +   str(row[2])+' '*20 +   str(row[3])+' '*20 +   str(row[4])+' '*20 +   str(row[5]))
    #for i in listbox.get_children():
    #    listbox.delete(i)

    for i in entry_list:
        i.delete(0,'end')



scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)





label_0 = Label(root,text="LOAD",width=20,font=("Arial",28,'bold'),fg='black')
label_0.place(x=450,y=53)

label2 = Label(root, text="Prenom",width=20,font=('bold',15),fg='black')
label2.place(x=470,y=160)


entry_2 = Entry(root,font=('bold',15))
entry_2.place(x=650,y=160)



label7 = Label(root, text="Nom",width=20,font=('bold',15),fg='black')
label7.place(x=50,y=160)


entry_7 = Entry(root,font=('bold',15))
entry_7.place(x=200,y=160)


label6 = Label(root, text="Region",width=20,font=('bold',15),fg='black')
label6.place(x=50,y=340)


entry_6 = Entry(root,font=('bold',15))
entry_6.place(x=200,y=340)



label_4 = Label(root, text="Docteur",width=20,font=('bold',15),fg='black')
label_4.place(x=870,y=160)

entry_4 = Entry(root,font=('bold',15))
entry_4.place(x=1050,y=160)




label_5 = Label(root, text="CIN",width=20,font=('bold',15),fg='black')
label_5.place(x=50,y=250)

entry_5 = Entry(root,font=('bold',15))
entry_5.place(x=200,y=250)



label_3 = Label(root, text="N°Doss",width=20,font=('bold',15),fg='black')
label_3.place(x=470,y=250)

entry_3 = Entry(root,font=('bold',15))
entry_3.place(x=650,y=250)


label_8 = Label(root, text="Diagnostic",width=20,font=('bold',15),fg='black')
label_8.place(x=870,y=250)

entry_8 = Entry(root,font=('bold',15))
entry_8.place(x=1050,y=250)




style = ttk.Style()
style.configure("mystyle.Treeview", highlightthickness=5, bd=0, font=('Calibri', 15),justify=LEFT) # Modify the font of the body
style.configure("mystyle.Treeview.Heading", font=('Calibri', 20,'bold'),anchor="e") # Modify the font of the headings
#style.layout("mystyle.Treeview", [('mystyle.Treeview.treearea', {'sticky': 'nswe'})])

cols = ('Nom', 'Prenom', 'CIN','Region',"N° Dossier","Diagnostic","Docteur")
listbox = ttk.Treeview(root, columns=cols, show='headings',style="mystyle.Treeview", yscrollcommand=scrollbar.set)
for col in cols:
    listbox.heading(col, text=col ,anchor=W)
listbox.place(x=20,y=420)
#listbox.insert(END, "Nom"+ ' '*20 + "Prenom"+' '*20 +   "N°Dossier"+' '*20 +   "Doc"+' '*20 +   "CIN"+' '*20 +   "Region" )




Button(root,text="OK",width=10,bg='brown',fg='white',height=2 ,font=('bolder',12),command=load).place(x=580,y=680)
Button(root,text="Delete",width=10,bg='brown',fg='white',height=2 ,font=('bolder',12),command=select).place(x=700,y=680)
mainloop()


# In[ ]:
