from tkinter import Button, Label
import random
import MSsettings
import ctypes
import sys

class Cell:
    all = []
    cellCount = MSsettings.CELL_COUNT
    cellCountLabelObject = None
    def __init__(self,x, y, isMine=False):
        self.isMine = isMine
        self.isOpened = False
        self.isMineCandidate = False
        self.cellBtnObject = None
        self.x = x
        self.y = y
        #Append the object to the Cell.all list
        Cell.all.append(self)

    def createBtnObject(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
        )
        btn.bind('<Button-1>', self.leftClickActions)
        btn.bind('<Button-3>', self.rightClickActions)
        self.cellBtnObject = btn

    @staticmethod
    def createCellCountLabel(location):
        lbl = Label(
            location,
            bg='black',
            fg='white',
            text=f'Cells Left:{Cell.cellCount}',
            width=12,
            height=4,
            font=('', 30)
        )
        Cell.cellCountLabelObject = lbl

    def leftClickActions(self, event):
        if self.isMine:
            self.showMine()
        else:
            if self.surroundedCellsMinesLenght == 0:
                for cellObject in self.surroundedCells:
                    cellObject.showCell()
            self.showCell()
        self.cellBtnObject.unbind('<Button-1>')
        self.cellBtnObject.unbind('<Button-3>')
        if Cell.cellCount == MSsettings.MINES_COUNT:
            ctypes.windll.user32.MessageBoxW(0, 'Contratulations! You won!', 'End of the Game', 0)

    def getCellByAxis(self, x,y):
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property
    def surroundedCells(self):
        cells = [
            self.getCellByAxis(self.x - 1, self.y - 1),
            self.getCellByAxis(self.x - 1, self.y),
            self.getCellByAxis(self.x - 1, self.y + 1),
            self.getCellByAxis(self.x, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y - 1),
            self.getCellByAxis(self.x + 1, self.y),
            self.getCellByAxis(self.x + 1, self.y + 1),
            self.getCellByAxis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    @property
    def surroundedCellsMinesLenght(self):
        counter = 0
        for cell in self.surroundedCells:
            if cell.isMine:
                counter += 1

        return counter

    def showCell(self):
        if not self.isOpened:
            Cell.cellCount -= 1
            self.cellBtnObject.configure(text=self.surroundedCellsMinesLenght)
            if Cell.cellCountLabelObject:
                Cell.cellCountLabelObject.configure(
                    text=f'Cells Left:{Cell.cellCount}',

            )
            self.cellBtnObject.configure(
                bg='SystemButtonFace'
            )
        self.isOpened = True

    def showMine(self):
        self.cellBtnObject.configure(bg='red')
        ctypes.windll.user32.MessageBoxW(0, 'You exploded', 'Game Over', 0)
        sys.exit()

    def rightClickActions(self, event):
        if not self.isMineCandidate:
            self.cellBtnObject.configure(
                bg='orange'
            )
            self.isMineCandidate = True
        else:
            self.cellBtnObject.configure(
                bg='SystemButtonFace'
            )
            self.isMineCandidate = False

    @staticmethod
    def randomizeMines():
        pickedCells = random.sample(
            Cell.all, MSsettings.MINES_COUNT,
        )
        for pickedCells in pickedCells:
            pickedCells.isMine = True

    def __repr__(self):
        return f'Cell({self.x}, {self.y})'