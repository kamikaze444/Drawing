import pygame as pg
import tkinter

root = tkinter.Tk()
width = root.winfo_screenwidth()
height = root.winfo_screenheight()

pg.init()

class Main():

    def __init__(self):
        root = tkinter.Tk()
        self.dis_sizes = (root.winfo_screenheight(),root.winfo_screenheight())
        hello
        self.length,self.height = (900,900)
        self.screen = pg.display.set_mode(self.length,self.height)

    def loop(self):
        run = True
        while run:
            for event in pg.event.get():
                if event == pg.QUIT():
                    run = False

        

        pg.quit()