from tkinter import *
import customtkinter
from PIL import ImageTk, Image

with open('sensor.txt', 'r') as f:
    ## print(f.name)
    movements = f.read()

def getFile():
    con = 0
    mov = ''
    for i in range(len(movements)):
        if (movements[i] == '\n'):
            con = 0
            #print(mov)
            for j in range(6):
                print(mov[j])
            mov = ''
        if ((con < 6) and (movements[i] != ' ')):
            mov += movements[i]
        con += 1


    # MouseMove(mov[0], mov[0], mov[0])


def MouseMove(arm, p, s):
    ##theRAT.place(x=307, y=231)

    medX = 0
    medY = 0
    armAUX = 0
    pAUX = 0

    if arm == 0:
        medX = 0
        medY = -42

    elif arm == 1:
        medX = 42
        medY = 0

    elif arm == 2:
        medX = 0
        medY = 42

    elif arm == 3:
        medX = -42
        medY = 0

    print(medX)

    # theRAT.place(x=(medX * p), y=(medY * p))

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

playRAT = customtkinter.CTkButton(frame, text="play", image=RAT, command=getFile())
playRAT.pack(padx=(550, 10), pady=(10, 10))

## command=MouseMove(1, 3, 1)





root.mainloop()
