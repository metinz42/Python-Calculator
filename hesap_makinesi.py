from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk

pencere = Tk()
pencere.geometry("270x250+300+100")
pencere.title("Hesap Makinesi")
pencere.resizable(FALSE,FALSE)
pencere.tk_setPalette("#F0F0FF")
ico = Image.open('ico.png')
photo = ImageTk.PhotoImage(ico)
pencere.wm_iconphoto(False,photo)


depo = ""

def hesapla(tus):
    try:
        global depo
        if tus in "0123456789":
            ekran.insert(END,tus)
            depo += tus
        if tus in "+/*-":
            ekran.insert(END,tus)
            depo += tus
        if tus=="=":
            ekran.delete(0,END)
            hesap = eval(depo,{"__builtins__":None},{})
            depo = str(hesap)
            ekran.insert(END,depo)
        if tus=="C":
            ekran.delete(0,END)
            depo = ""
    except Exception :
        ekran.delete(0,END)
        messagebox.showerror("Hata","Hata lütfen tekrar deneyiniz!")
        depo = ""

ekran = Entry(width=44,justify=RIGHT,) # justify metni sağa yaslamak için
ekran.grid(row=0,column=0,columnspan=3,ipady=4) 

liste =["1","2","3","4","5","6","7","8","9","0","+","-","*","/","=","C"]

sira = 1
sutun = 0

for i in liste:
    komut=lambda x=i:hesapla(x)
    Button(text=i,fg="black",font="verdana 8 bold",bg="#F0F0FF",width=10,height=2,relief=GROOVE,command=komut).grid(row=sira,column=sutun)
    sutun += 1
    if sutun>2:
        sutun = 0
        sira +=1

mainloop()



