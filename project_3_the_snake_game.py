from tkinter import *
from tkinter import messagebox
from time import sleep
from random import randint

class snake:
    def __init__(self,background):

        # Generate the box
        self.grids = [[0 for x in range(gridDimension)] for y in range(gridDimension)]
        for x in range(gridDimension): 
            for y in range (gridDimension):
                self.grids[x][y] = background.create_rectangle(x*boxSize, y*boxSize,(x+1)*boxSize, (y+1)*boxSize, outline="white")

        # Generate a snake from middle
        self.snakeLen = 7
        self.body = []
        
        for i in range (0,self.snakeLen): 
            self.body.append([gridDimension//2, (gridDimension//2)+i] )

        print (self.body[0][0])
        for item in range (len(self.body)):
            if (item == 0):
                background.itemconfig(self.grids[(self.body[item][0])][(self.body[item][1])], fill = 'red')
            else:
                background.itemconfig(self.grids[(self.body[item][0])][(self.body[item][1])], fill = 'white')

        # Initialize key press event environment
        background.bind("<Left>",self.moveLeft)
        background.bind("<Right>",self.moveRight)
        background.focus_set()

        # Initialize apple
        self.appleX = randint(0, gridDimension-1)
        self.appleY = randint(0, gridDimension-1)
        self.genApple()

        self.last = [0,0] # The last location of snake, so it is easy to append the snake when apple is eaten
        self.direction = 0 # The direction, 0-up 1-down 2-left 3-right
        self.moveValid = True # 
        while self.moveValid:
            self.moveCheck()
            if (self.moveValid == False):
                break
            self.move()        

    def moveUp(self,event):
        self.moveValid = True
        background.unbind('<Up>')
        background.unbind('<Down>')
        background.bind("<Left>",self.moveLeft)
        background.bind("<Right>",self.moveRight)
        self.direction = 0
        while self.moveValid:
            self.moveCheck()
            if (self.moveValid == False):
                break
            self.move()

    def moveDown(self,event):
        self.moveValid = True
        background.unbind('<Up>')
        background.unbind('<Down>')
        background.bind("<Left>",self.moveLeft)
        background.bind("<Right>",self.moveRight)
        self.direction = 1
        while self.moveValid:
            self.moveCheck()
            if (self.moveValid == False):
                break
            self.move()

    def moveLeft(self,event):
        self.moveValid = True
        background.unbind('<Left>')
        background.unbind('<Right>')
        background.bind("<Up>",self.moveUp)
        background.bind("<Down>",self.moveDown)
        self.direction = 2
        while self.moveValid:
            self.moveCheck()
            if (self.moveValid == False):
                break
            self.move()

    def moveRight(self,event):
        self.moveValid = True
        background.unbind('<Left>') 
        background.unbind('<Right>')
        background.bind("<Up>",self.moveUp)
        background.bind("<Down>",self.moveDown)
        self.direction = 3
        while self.moveValid:
            self.moveCheck()
            if (self.moveValid == False):
                break
            self.move()

    def move(self):
        #Four directions
        if (self.direction == 0):
            background.itemconfig(self.grids[(self.body[-1][0])][(self.body[-1][1])], fill = 'black') # Uncolor the last one
            self.last[0] = self.body[self.snakeLen-1][0]
            self.last[1] = self.body[self.snakeLen-1][1]
            for i in range (self.snakeLen-1, 0, -1): 
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]
            self.body[0][1] -= 1 
            self.snakeUpdate()

        elif (self.direction == 1):
            background.itemconfig(self.grids[(self.body[-1][0])][(self.body[-1][1])], fill = 'black') # Uncolor the last one
            self.last[0] = self.body[self.snakeLen-1][0]
            self.last[1] = self.body[self.snakeLen-1][1]
            for i in range (self.snakeLen-1, 0, -1):
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]
            self.body[0][1] += 1 
            self.snakeUpdate()
        
        elif (self.direction == 2):
            background.itemconfig(self.grids[(self.body[-1][0])][(self.body[-1][1])], fill = 'black') # Uncolor the last one
            self.last[0] = self.body[self.snakeLen-1][0]
            self.last[1] = self.body[self.snakeLen-1][1]
            for i in range (self.snakeLen-1, 0, -1): 
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]
            self.body[0][0] -= 1 
            self.snakeUpdate()

        elif (self.direction == 3):
            background.itemconfig(self.grids[(self.body[-1][0])][(self.body[-1][1])], fill = 'black') # Uncolor the last one
            self.last[0] = self.body[self.snakeLen-1][0]
            self.last[1] = self.body[self.snakeLen-1][1]
            for i in range (self.snakeLen-1, 0, -1): 
                self.body[i][0] = self.body[i-1][0]
                self.body[i][1] = self.body[i-1][1]
            self.body[0][0] += 1 
            self.snakeUpdate()

    def snakeUpdate(self):
        for item in range (0,self.snakeLen):
            if (item == 0):
                background.itemconfig(self.grids[(self.body[item][0])][(self.body[item][1])], fill = 'red')
            else:
                background.itemconfig(self.grids[(self.body[item][0])][(self.body[item][1])], fill = 'white')
        sleep(0.05)

        root.update()

    def moveCheck(self):
        self.appleEatenCheck()
        self.gameOverCheck()
        if (self.direction == 0 and (self.body[0][1])-1 < 0):
            self.moveValid = False
        elif (self.direction == 1 and (self.body[0][1])+1 > gridDimension-1):
            self.moveValid = False
        elif (self.direction == 2 and (self.body[0][0])-1 < 0):
            self.moveValid = False
        elif (self.direction == 3 and (self.body[0][0])+1 > gridDimension-1):
            self.moveValid = False
             
    def genApple(self):
        overlap = True
        
        while (overlap):
            self.appleX = randint(0, gridDimension-1)
            self.appleY = randint(0, gridDimension-1)

            for i in range (0,self.snakeLen):
                if ((self.body[i][0] == self.appleX) and (self.body[i][1] == self.appleY)):
                    overlap = True
                else:
                    overlap = False

        background.itemconfig(self.grids[(self.appleX)][(self.appleY)], fill = '#90ee90')

    def appleEatenCheck(self):
        if ((self.body[0][0] == self.appleX) and (self.body[0][1] == self.appleY)):
            self.snakeLen += 1
            self.body.append([self.last[0],self.last[1]])
            self.genApple()

    def gameOverCheck(self):
        for i in range (1,self.snakeLen):
            if ((self.body[0][0] == self.body[i][0]) and (self.body[0][1] == self.body[i][1])):
                messagebox.showinfo("Game Over","Try again next time!")
                self.move() # Move once so the function will trigger multiple times
                root.destroy()
                

root = Tk()

dimension = (600)

origin = (0)
boxSize = (20)
gridDimension = (dimension//boxSize) 

root.geometry("{}x{}".format(dimension,dimension))
background = Canvas(root, width=dimension, height=dimension, background="black")
background.pack()

game = snake(background)

root.mainloop()