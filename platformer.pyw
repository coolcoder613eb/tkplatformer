from tkinter import *
from tkinter import ttk
from tkinter.messagebox import *

w = Tk()
w.state('zoomed')
w.minsize(width=600, height=600)
w.title('Coding Game')
w['bg']='#ffffff'
#29 x 14

screen = PhotoImage(file='assets/screen.png')
g = PhotoImage(file='assets/grass1.png')
d = PhotoImage(file='assets/soil1.png')


def read(file):
    with open(file,'r', encoding="utf-8") as f:
        r = f.read()
        s = r.splitlines()
        l = []
        for x in s:
            l.append(x.split(' '))

        for y in range(14):
            for x in range(29):
                if l[y][x] == 'g':
                    tiles.append(c.create_image(cr[x],cr[y],anchor = 'nw',image = g))
                if l[y][x] == 'd':
                    tiles.append(c.create_image(cr[x],cr[y],anchor = 'nw',image = d))



cr=[4, 46, 88, 130, 172, 214, 256, 298, 340, 382, 424, 466, 508, 550, 592, 634, 676, 718, 760, 802, 844, 886, 928, 970, 1012, 1054, 1096, 1138, 1180]

tiles=[]

c = Canvas(w,width = 1218,height = 588,bd = 1,relief = SOLID,bg = 'light sky blue')
bg = c.create_image(3,3,anchor = 'nw',image = screen)



c.grid(column = 0,row = 2,padx = 5,pady = 5)

read('data/1.lvl')

w.mainloop()




