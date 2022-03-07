from tkinter import *
from tkinter.ttk import *
import pyAesCrypt
import os
import getpass

if getattr(sys, 'frozen', False):
    os.chdir(sys._MEIPASS)

def crypt1(password):
    dir = "C:/Users/"+getpass.getuser()+"/Desktop/VK_message"
    pas = password
    def crypt(file, pas):
        password = pas
        bufferSize = 512 * 1024
        pyAesCrypt.encryptFile(str(file), str(file) + ".crp", password, bufferSize)
        os.remove(file)
    def walk(dir, pas):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                crypt(path, pas)
            else:
                walk(path, pas)
    walk(str(dir), str(pas))
def decrypt1(password):
    dir = "C:/Users/" + getpass.getuser() + "/Desktop/VK_message"
    pas = password
    def decrypt(file, pas):
        password = pas
        bufferSize = 512 * 1024
        pyAesCrypt.decryptFile(str(file), str(os.path.splitext(file)[0]), password, bufferSize)
        os.remove(file)
    def walk(dir, pas):
        for name in os.listdir(dir):
            path = os.path.join(dir, name)
            if os.path.isfile(path):
                try:
                    decrypt(path, pas)
                except:
                    pass
            else:
                walk(path, pas)
    walk(str(dir), str(pas))


w = Tk()
w.title("VK message")

photofr=Frame(w)
fr1=Frame(w)
fr2=Frame(w)
fr3=Frame(w)
fr33=Frame(w)
fr4=Frame(w)
fr5=Frame(w)
photofr.grid(row=0)
fr1.grid(row=1)
fr2.grid(row=2)
fr3.grid(row=3)
fr33.grid(row=3)
fr4.grid(row=4)
fr5.grid(row=5)
####

add_img = PhotoImage(file="VKmessage.gif")
CheckMark = PhotoImage(file="CheckMark.gif")
def Photo():
    label = Label(fr1, image=add_img)
    label.pack(side=TOP)
####

def string():
    var = IntVar()
    rad0 = Radiobutton(fr1, text="Зашифровать", variable=var, value=0, command=callpassword1)
    rad1 = Radiobutton(fr1, text="Раcшифровать", variable=var, value=1, command=callpassword2)
    rad0.pack(side=LEFT)
    rad1.pack(side=RIGHT)
#####
def label():
    la = Label(fr2, text="Пароль для шифрования")
    la.pack()
#####
def password1():
    password = Entry(fr3, text="Пароль", width=13, font=10)
    btn1 = Button(fr3, text="Сделать!")
    btn1.bind("<Button-1>", lambda event: crypt1(password.get()))
    password.grid(column=0, row=0)
    btn1.grid(column=1, row=0)
#####
def password2():
    password = Entry(fr33, text="Пароль", width=13, font=10)
    btn1 = Button(fr33, text="Сделать!")
    btn1.bind("<Button-1>", lambda event: decrypt1(password.get()))
    password.grid(column=0, row=0)
    btn1.grid(column=1, row=0)

#####
def papka():

    lab1 = Label(fr4, text="Создать папку на рабочем столе")
    lab1.pack(side=LEFT)
    btn1 = Button(fr4, image=CheckMark)
    btn1.pack(side=LEFT)
    btn1.bind("<Button-1>", lambda event: createdir())
def callpassword1():
    fr33.grid_forget()
    fr3.grid(row=3)
def callpassword2():
    fr3.grid_forget()
    fr33.grid(row=3)
def createdir():
    os.mkdir("C:/Users/"+getpass.getuser()+"/Desktop/VK_message")
Photo()
string()
label()
password1()
password2()
papka()
fr33.grid_forget()
w.mainloop()
