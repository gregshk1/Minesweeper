from tkinter import *
import MSsettings
import MSutils
from MScell import Cell

root = Tk()
#Override the settings of the window
root.configure(bg='black')
root.geometry(f'{MSsettings.WIDTH}x{MSsettings.HEIGHT}')
root.title('Minesweeper Game')
root.resizable(False, False)

topFrame = Frame(
    root,
    bg='black',
    width=MSsettings.WIDTH,
    height=MSutils.height_prct(25)
)
topFrame.place(x=0, y=0)

gameTitle = Label(
    topFrame,
    bg='Black',
    fg='White',
    text='Minesweeper Game',
    font=('', 48)
)

gameTitle.place(
    x=MSutils.width_prct(25), y=0
)

leftFrame = Frame(
    root,
    bg='black',
    width=MSutils.width_prct(25),
    height=MSutils.height_prct(75)
)
leftFrame.place(x=0,y=MSutils.height_prct(25))

centerFrame = Frame(
    root,
    bg='black', #Change later
    width=MSutils.width_prct(75),
    height=MSutils.height_prct(75),
)
centerFrame.place(
    x=MSutils.width_prct(25),
    y=MSutils.height_prct(25)
)

for x in range(MSsettings.GRID_SIZE):
    for y in range(MSsettings.GRID_SIZE):
        c = Cell(x, y)
        c.createBtnObject(centerFrame)
        c.cellBtnObject.grid(
            column=x, row=y
        )

Cell.createCellCountLabel(leftFrame)
Cell.cellCountLabelObject.place(
    x=0, y=0
)

Cell.randomizeMines()


#Run The window
root.mainloop()
