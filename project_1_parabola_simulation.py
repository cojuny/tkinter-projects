from tkinter import *
from time import sleep
from random import sample

def display_tk(linePoints,H):

    root = Tk()
    root.title("Parabola Simulation")

    b = Canvas(root, width=H, height=H)
    b.pack()

    ran = []
    ran = sample(range(H),H)

    for i in (ran):
        b.create_line(linePoints[i][0][0],linePoints[i][0][1],linePoints[i][1][0],linePoints[i][1][1])
        sleep(0.05)
        root.update()


    root.mainloop()


def solver():
    L = (0)
    H = (1000)

    # The combination of lines
    lineList = []
    x = H
    for y in range (0,H):
        lineList.append([x,y])
        x -= 1


    # Set to tuple
    for i in range (H):
        lineList[i] = tuple(lineList[i])
    lineList = tuple(lineList)


    # Locate four points of each line, linePoints[line][points][axis]
    linePoints = []
    for i in range (H):
        points = []
        points.append([lineList[i][0],L])
        points.append([L,lineList[i][1]])

        linePoints.append(points)

    display_tk(linePoints,H)

solver()