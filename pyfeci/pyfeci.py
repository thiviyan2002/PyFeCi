import tkinter as tk
import random
from tkinter import messagebox as tkMessageBox
from tkinter import *
#from PIL import Image, ImageTk
nom="user"
user_win=0
userresult="vous avez gagner un point"
egalité=0
computer_win=0
computerresult="ordi a gagner un point"
running=True
def click():
    global user_win
    global egalité
    global computer_win
    choix=entry.get()
    ordi = random.randint(1, 3)
    if choix == "q":
        tkMessageBox.askyesno("Exit","êtes vous sur de vouloir quitter ?")
        window.destroy()

    if choix == "p":
        chx.config(text="vous avez choisi pierre")

    elif choix == "f":
        chx.config(text="vous avez choisi feuille")

    elif choix=="c":
        chx.config(text="vous avez choisi ciseau")

    else:
        chx.config(text="mauvais choix")

    ordi = random.randint(1, 3)
    if ordi == 1:
        choixPC = "p"
        chxo.config(text="Ordi a choisi pierre")

    elif ordi == 2:
        choixPC = "f"
        chxo.config(text="Ordi a choisi feuille")

    else:
        choixPC = "c"
        chxo.config(text="Ordi a choisi ciseau")


    if choix == choixPC:
        rslt.config(text="Parti nulle")

        egalité = egalité + 1
        score.config(text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}")
    elif choix == "p" and choixPC == "f":
        rslt.config(text=computerresult)

        computer_win = computer_win + 1
        score.config(text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}")
    elif choix == "f" and choixPC == "p":
        rslt.config(text=userresult)

        user_win = user_win + 1
        score.config(text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}")
    elif choix == "p" and choixPC == "c":
        user_win = user_win + 1
        score.config(text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}")
    elif choix == "c" and choixPC == "p":
        rslt.config(text=computerresult)

        computer_win = computer_win + 1
        score.config(text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}")
    elif choix == "f" and choixPC == "c":
        rslt.config(text=computerresult)

        computer_win = computer_win + 1
        score.config(text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}")
    elif choix == "c" and choixPC == "f":
        rslt.config(text=userresult)

        user_win = user_win + 1
        score.config(text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}")

    vc="Vainqueur"
    if user_win == 3:
        #print("vous avez gagner")
        tkMessageBox.showinfo(vc, "vous avez gagner")
        window.destroy()
    elif computer_win == 3:
        #print("ordi a gagner")
        tkMessageBox.showinfo(vc, "ordi a gagner")
        window.destroy()

#def fenetre
window=tk.Tk()
window.title("PyFeCi")
window.geometry("400x400")
window.minsize(400,250)
window.iconbitmap(r"pyfeci.ico")


img=PhotoImage(file="font3.png")
lbl_bk=tk.Label(window,image=img)
lbl_bk.image=img
lbl_bk.place(relx=0.5,rely=0.5,anchor="center")

#def label
hello = tk.Label(window, text=f"Hello {nom}",
    bg="#736357",
    fg="#C69C6D",
    font=("Arial",20),
    width=20,
    height=2
)

hello.pack()

qustn = tk.Label(window, text=f"{nom} Quel est votre choix: (p)pierre/(f)feuille/(c)ciseau ou (q)quitter:",
    font=("Arial",10),fg="#00FF00",bg="#006837"
)
qustn.pack(pady=(10,10))
#def entry
entry=tk.Entry(window)
entry.pack(pady=(0,10))


#def button
button=tk.Button(window,text="Cliquez ici",
    width=10,
    height=1,
    bg="#006837",
    fg="#00FF00",
    command=click
                 )
button.pack(pady=(0,10))
score = tk.Label(window, text=f"{nom}:{user_win}/egaliter:{egalité}/ordi:{computer_win}",
    font=("Arial",10),fg="#F15A24",bg="#999999"
)
score.pack()
chx=tk.Label(window, text="",
    font=("Arial",10),bg="#00FF00"
)
chx.pack()
chxo=tk.Label(window, text="",
    font=("Arial",10),bg="#00FF00"
)
chxo.pack()
rslt=tk.Label(window, text="",
    font=("Arial",10),bg="#00FF00"
)
rslt.pack()
window.mainloop()