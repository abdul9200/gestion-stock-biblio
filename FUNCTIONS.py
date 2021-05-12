from tkinter import END
try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk
try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True
def init(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top


class Livre :
    def __init__(self,name,etat,quantity=1):
        self.name=name
        self.quantity=int(quantity)
        self.etat=etat
    def Ajouter(self):
        fichierDonnees = "biblio.db"
        conn=sqlite3.connect(fichierDonnees)
        cur=conn.cursor()
        cur.execute( """CREATE TABLE IF NOT EXISTS Stock ([LivreID] INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
        [Titre] NVARCHAR(160) NOT NULL,
        [quantité] INTEGER NOT NULL,
        [etat] TEXT NOT NULL);""")
        cur.execute("SELECT quantité FROM Stock WHERE Titre=? AND etat=?", (self.name,self.etat))
        if(len(cur.fetchall())==0):
            cur.execute("INSERT INTO Stock (Titre,quantité,etat) VALUES (?,?,?)",(self.name,self.quantity,self.etat))
        else :
            cur.execute("SELECT * FROM Stock WHERE Titre=? AND etat=?", (self.name,self.etat))
            a=cur.fetchone()[2]
            cur.execute("UPDATE Stock Set quantité=? WHERE Titre=? etat=?",(a+self.quantity,self.name,self.etat))
        conn.commit()
        cur.close()
        conn.close()
    def Quantity(self):
        fichierDonnees = "biblio.db"
        conn = sqlite3.connect(fichierDonnees)
        cur = conn.cursor()
        cur.execute("SELECT quantité FROM Stock WHERE Titre=? AND etat=?",(self.name,self.etat))
        resultat=cur.fetchall()[0][0]
        conn.commit()
        cur.close()
        conn.close()
        return resultat
    def Vendre(self):
        fichierDonnees = "biblio.db"
        conn = sqlite3.connect(fichierDonnees)
        cur = conn.cursor()
        cur.execute("SELECT quantité FROM Stock WHERE Titre=? AND etat=?", (self.name, self.etat))
        if (len(cur.fetchall()[0]) == 0):
            resultat='Repture de Stock'
        else :
            cur.execute("SELECT quantité FROM Stock WHERE Titre=? AND etat=?", (self.name, self.etat))
            if cur.fetchall()[0][0] < self.quantity :
                resultat=f"""Indisponible!quantité disponible:{cur.fetchall()[0][0] }"""
            else :
                cur.execute("SELECT * FROM Stock WHERE Titre=? AND etat=?", (self.name, self.etat))
                a = cur.fetchone()[2]
                cur.execute("UPDATE Stock SET quantité=? WHERE Titre=? AND etat=?",(a-self.quantity,self.name,self.etat))
                resultat = f"""Disponible !Encore {a-self.quantity} dans le stock"""
        conn.commit()
        cur.close()
        conn.close()
        return resultat
def AjouterElement(Entry1,Entry1_1,Entry1_2,Entry1_3):
    Entry1_2.delete(0,END)
    text1 =Entry1.get()
    text2 = Entry1_1.get()
    text3 = Entry1_3.get()
    a = Livre(text1, text3,text2)
    try:
        a.Ajouter()
    except:
        Entry1_2.insert(0, 'Ce livre n\'a pas été saisi')
    else:
        Entry1_2.insert(0, f'Ce livre est bien ajouté \n au stock d\'un quantité de {text2}')
    Entry1.delete(0,END)
    Entry1_1.delete(0, END)
    Entry1_3.delete(0, END)
def Quant(Entry1,Entry1_1,Entry1_2,Entry1_3):
    Entry1_2.delete(0, END)
    text1 = Entry1.get()
    text3 = Entry1_3.get()
    a = Livre(text1,text3)
    try:
        result=a.Quantity()
    except:
        Entry1_2.insert(0, 'Ce livre n\'existe pas \n dans le stock')
    else:
        Entry1_2.insert(0, f' quantité existante : {result}')
    Entry1.delete(0,END)
    Entry1_1.delete(0, END)
    Entry1_3.delete(0, END)
def Vente(Entry1,Entry1_1,Entry1_2,Entry1_3):
    Entry1_2.delete(0,END)
    text1 = Entry1.get()
    text2 = Entry1_1.get()
    text3 = Entry1_3.get()
    a = Livre(text1,text3,text2)
    try:
        Entry1_2.insert(0,a.Vendre())
    except:
        Entry1_2.insert(0,"Error404")
    Entry1.delete(0, END)
    Entry1_1.delete(0, END)
    Entry1_3.delete(0, END)
def destroy_window():
    global top_level
    top_level.destroy()
    top_level = None
if __name__ == '__main__':
    import main
    main.vp_start_gui()



