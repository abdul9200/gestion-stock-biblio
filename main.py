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
import FUNCTIONS
from functools import partial
def vp_start_gui():
    global val, w, root
    root = tk.Tk()
    top = Toplevel1(root)
    FUNCTIONS.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(rt, *args, **kwargs):
    global w, w_win, root
    root = rt
    w = tk.Toplevel(root)
    top = Toplevel1(w)
    FUNCTIONS.init(w, top, *args, **kwargs)
    return (w, top)
def destroy_Toplevel1():
    global w
    w.destroy()
    w = None
class Toplevel1:
    def __init__(self, top=None):
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        top.geometry("868x790+0+0")
        top.minsize(868, 790)
        top.maxsize(868,790)
        top.resizable(0, 0)
        top.title("Biblio BADRANE")
        top.configure(background="#0431b5")
        self.Entry1 = tk.Entry(top)
        self.Entry1.place(x=127, y=100, height=36, width=204)
        self.Entry1.configure(background="white")
        self.Entry1.configure(disabledforeground="#a3a3a3")
        self.Entry1.configure(font="TkFixedFont")
        self.Entry1.configure(foreground="#000000")
        self.Entry1.configure(insertbackground="black")
        self.Entry1_1 = tk.Entry(top)
        self.Entry1_1.place(x=127, y=250, height=36, width=204)
        self.Entry1_1.configure(background="white")
        self.Entry1_1.configure(disabledforeground="#a3a3a3")
        self.Entry1_1.configure(font="TkFixedFont")
        self.Entry1_1.configure(foreground="#000000")
        self.Entry1_1.configure(highlightbackground="#d9d9d9")
        self.Entry1_1.configure(highlightcolor="black")
        self.Entry1_1.configure(insertbackground="black")
        self.Entry1_1.configure(selectbackground="blue")
        self.Entry1_1.configure(selectforeground="white")
        self.Entry1_2 = tk.Entry(top)
        self.Entry1_2.place(x=64, y=500, height=136, width=284)
        self.Entry1_2.configure(background="#0431b5")
        self.Entry1_2.configure(disabledforeground="#a3a3a3")
        self.Entry1_2.configure(font="TkFixedFont")
        self.Entry1_2.configure(foreground="#FFFFFF")
        self.Entry1_2.configure(highlightbackground="#d9d9d9")
        self.Entry1_2.configure(highlightcolor="black")
        self.Entry1_2.configure(insertbackground="black")
        self.Entry1_2.configure(selectbackground="blue")
        self.Entry1_2.configure(selectforeground="white")
        self.Entry1_3 = tk.Entry(top)
        self.Entry1_3.place(x=127, y=400, height=36, width=204)
        self.Entry1_3.configure(background="white")
        self.Entry1_3.configure(disabledforeground="#a3a3a3")
        self.Entry1_3.configure(font="TkFixedFont")
        self.Entry1_3.configure(foreground="#000000")
        self.Entry1_3.configure(insertbackground="black")
        self.Button1 = tk.Button(top)
        self.Button1.place(x=623, y=50, height=62, width=138)
        self.Button1.configure(activebackground="#ececec")
        self.Button1.configure(activeforeground="#000000")
        self.Button1.configure(background="#d9d9d9")
        action1 = partial(FUNCTIONS.AjouterElement,self.Entry1,self.Entry1_1,self.Entry1_2,self.Entry1_3)
        self.Button1.configure(command=action1)
        self.Button1.configure(disabledforeground="#a3a3a3")
        self.Button1.configure(foreground="#000000")
        self.Button1.configure(highlightbackground="#d9d9d9")
        self.Button1.configure(highlightcolor="black")
        self.Button1.configure(pady="0")
        self.Button1.configure(text='''Ajouter''')
        self.Button1_1 = tk.Button(top)
        self.Button1_1.place(x=623, y=250, height=62, width=138)
        self.Button1_1.configure(activebackground="#ececec")
        self.Button1_1.configure(activeforeground="#000000")
        self.Button1_1.configure(background="#d9d9d9")
        action2 = partial(FUNCTIONS.Quant, self.Entry1, self.Entry1_1, self.Entry1_2,self.Entry1_3)
        self.Button1_1.configure(command=action2)
        self.Button1_1.configure(disabledforeground="#a3a3a3")
        self.Button1_1.configure(foreground="#000000")
        self.Button1_1.configure(highlightbackground="#d9d9d9")
        self.Button1_1.configure(highlightcolor="black")
        self.Button1_1.configure(pady="0")
        self.Button1_1.configure(text='''Quantité''')
        self.Button1_2 = tk.Button(top)
        self.Button1_2.place(x=623, y=500, height=62, width=138)
        self.Button1_2.configure(activebackground="#ececec")
        self.Button1_2.configure(activeforeground="#000000")
        self.Button1_2.configure(background="#d9d9d9")
        action3 = partial(FUNCTIONS.Vente, self.Entry1, self.Entry1_1, self.Entry1_2,self.Entry1_3)
        self.Button1_2.configure(command=action3)
        self.Button1_2.configure(disabledforeground="#a3a3a3")
        self.Button1_2.configure(foreground="#000000")
        self.Button1_2.configure(highlightbackground="#d9d9d9")
        self.Button1_2.configure(highlightcolor="black")
        self.Button1_2.configure(pady="0")
        self.Button1_2.configure(text='''Vendre''')


if __name__ == '__main__':
    vp_start_gui()