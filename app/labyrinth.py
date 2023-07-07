from tkinter import *
import customtkinter
from PIL import ImageTk, Image
import re
import time



def getFile(event=None):
    with open('movents.txt', 'r') as f:
        movements = f.read()

    con = 0
    mov = ''
    movi = [4]
    for i in range(len(movements)):
        if (movements[i] == '\n'):
            movi = re.findall('\d+', mov)
            con = 0


            # print(movi[0] + movi[1] + movi[2])
            MouseMove(movi[0], movi[1], movi[2])
            root.update()
            time.sleep(0.2)


            # for j in range(6):
            #    print('-' + mov[j] + '-')

            mov = ''
        if ((con < 6) and (movements[i] != (' ' or '\n' or '\t'))):
            mov += movements[i]
        con += 1

    # Chame a função MouseMove com os valores obtidos
    # MouseMove(int(mov[0]), mov[1], mov[2])
    # MouseMove(4, 2, 1)



def MouseMove(arm, p, s):
    medX = 0
    medY = 0

    if arm == '0':
        medX = 0
        medY = -42
    elif arm == '1':
        medX = 42
        medY = 0
    elif arm == '2':
        medX = 0
        medY = 42
    elif arm == '3':
        medX = -42
        medY = 0

    theRAT.place(x=(232 - (medX * int(p))), y=(231 - (medY * int(p))))
    # print(f'{medX} : {medY} == arm{arm} p{p}')
    # print(arm + p + s)
    # xR = (medX * p)
    # yR = (medY * p)

    # print(xR + " - " +yR)
    print(f'{arm} : {p} : {s}')


customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('dark-blue')      ## SET COLOR

## ROOT ELEMENT CREATED
root = customtkinter.CTk()
root.geometry('800x500')
root.resizable(False, False)
root.title('labyrinth')

## THE IMAGES ARE IMPORTED
imgLAB = Image.open("labrinth.png")
RimgLAB = imgLAB.resize((500, 500))
LAB = ImageTk.PhotoImage(RimgLAB)

imgRAT = Image.open("rat.png")
RimgRAT = imgRAT.resize((38, 38))
RAT = ImageTk.PhotoImage(RimgRAT)



## DECLARES THE MAIN FRAME
frame = customtkinter.CTkFrame(master=root)
frame.pack(fill='both', expand=True)


## THE LAB AND RAT IMAGES
theLAB = customtkinter.CTkLabel(frame, text="", image=LAB)
theLAB.place(x=0, y=0)

theRAT = customtkinter.CTkLabel(frame, text="", image=RAT)
theRAT.place(x=232, y=231)

playRAT = customtkinter.CTkButton(frame, text="play", image=RAT, command=getFile)
playRAT.pack(padx=(550, 10), pady=(10, 10))

## command=MouseMove(1, 3, 1)





root.mainloop()
