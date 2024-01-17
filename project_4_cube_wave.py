from tkinter import *
import numpy as np
from math import sin, sqrt

class cube:
    root = Tk()
    LENGTH = 600
    HEIGHT = 600

    p = 0
    h = 0

    colorR = "#%02x%02x%02x" % (230,218,165)
    colorL = "#%02x%02x%02x" % (53,74,123)
    colorT = "#%02x%02x%02x" % (119,170,175)

    isDelay = True

    value = np.array([[0,1,2,3,4,3,2,1,0],
                      [1,2,3,4,0,4,3,2,1],
                      [2,3,4,0,1,0,4,3,2],
                      [3,4,0,1,2,1,0,4,3],
                      [4,0,1,2,3,2,1,0,4],
                      [3,4,0,1,2,1,0,4,3],
                      [2,3,4,0,1,0,1,3,2],
                      [1,2,3,4,0,4,3,2,1],
                      [0,1,2,3,4,3,2,1,0]])


    def __init__(self):
        cube.root.geometry("{}x{}".format(cube.LENGTH,cube.HEIGHT))
        cube.root.configure(bg="black")
        self.bg = Canvas(cube.root, width=cube.LENGTH, height=cube.HEIGHT, background="{}".format("#%02x%02x%02x" % (249,248,249)))
        self.bg.pack(side=BOTTOM)

        self.projection()

        while True:
            self.box_move()


    def projection(self):

        h = 25

        cube.preboxes = np.empty([9,9,7,3])
        for col in range (0,9):
            for row in range (0,9):
                cube.preboxes[col, row, 0] = np.array([0+3*row, 0, 0+3*col])
                cube.preboxes[col, row, 1] = np.array([0+3*row, 0, 3+3*col])
                cube.preboxes[col, row, 2] = np.array([3+3*row, 0, 0+3*col])
                cube.preboxes[col, row, 3] = np.array([0+3*row, h, 0+3*col])
                cube.preboxes[col, row, 4] = np.array([0+3*row, h, 3+3*col])
                cube.preboxes[col, row, 5] = np.array([3+3*row, h, 0+3*col])
                cube.preboxes[col, row, 6] = np.array([3+3*row, h, 3+3*col])

        M = np.array([[sqrt(3), 0, -sqrt(3)],
                    [1, 2, 1],
                    [sqrt(2), -sqrt(2), sqrt(2)]])

        cof = 1 / sqrt(6)

        for col in range (0,9):
            for row in range (0,9):
                cube.preboxes[col, row, 0] = cof * (M @ cube.preboxes[col, row, 0])
                cube.preboxes[col, row, 1] = cof * (M @ cube.preboxes[col, row, 1])
                cube.preboxes[col, row, 2] = cof * (M @ cube.preboxes[col, row, 2])
                cube.preboxes[col, row, 3] = cof * (M @ cube.preboxes[col, row, 3])
                cube.preboxes[col, row, 4] = cof * (M @ cube.preboxes[col, row, 4])
                cube.preboxes[col, row, 5] = cof * (M @ cube.preboxes[col, row, 5])
                cube.preboxes[col, row, 6] = cof * (M @ cube.preboxes[col, row, 6])

        asf = np.array([[1, 0, 0],
                    [0, 1, 0]])
        asf = asf.T
        ao = np.array([30, 10])

        cube.preboxes2 = np.empty([9,9,7,2])


        for col in range (0,9):
            for row in range (0,9):
                cube.preboxes2[col, row, 0] = cube.preboxes[col, row, 0] @ asf + ao #a
                cube.preboxes2[col, row, 1] = cube.preboxes[col, row, 1] @ asf + ao #b
                cube.preboxes2[col, row, 2] = cube.preboxes[col, row, 2] @ asf + ao #c
                cube.preboxes2[col, row, 3] = cube.preboxes[col, row, 3] @ asf + ao #d
                cube.preboxes2[col, row, 4] = cube.preboxes[col, row, 4] @ asf + ao #e
                cube.preboxes2[col, row, 5] = cube.preboxes[col, row, 5] @ asf + ao #f
                cube.preboxes2[col, row, 6] = cube.preboxes[col, row, 6] @ asf + ao #g

        del cube.preboxes

        cube.boxes = np.empty([9,9,3,8])
        

        for col in range (0,9):
            for row in range (0,9):
                cube.boxes[col, row, 0] = [int(cube.preboxes2[col, row, 4, 0] * 10) , 600 - int(cube.preboxes2[col, row, 4, 1]* 10) , int(cube.preboxes2[col, row, 3, 0] * 10) , 600 - int(cube.preboxes2[col, row, 3, 1] * 10) , int(cube.preboxes2[col, row, 0, 0] * 10) , 600 - int(cube.preboxes2[col, row, 0, 1] * 10) , int(cube.preboxes2[col, row, 1, 0] * 10) , 600 - int(cube.preboxes2[col, row, 1, 1] * 10) ]
                cube.boxes[col, row, 1] = [int(cube.preboxes2[col, row, 4, 0] * 10) , 600 - int(cube.preboxes2[col, row, 4, 1]* 10) , int(cube.preboxes2[col, row, 6, 0] * 10) , 600 - int(cube.preboxes2[col, row, 6, 1] * 10) , int(cube.preboxes2[col, row, 5, 0] * 10) , 600 - int(cube.preboxes2[col, row, 5, 1] * 10) , int(cube.preboxes2[col, row, 3, 0] * 10) , 600 - int(cube.preboxes2[col, row, 3, 1] * 10) ]           
                cube.boxes[col, row, 2] = [int(cube.preboxes2[col, row, 0, 0] * 10) , 600 - int(cube.preboxes2[col, row, 0, 1]* 10) , int(cube.preboxes2[col, row, 2, 0] * 10) , 600 - int(cube.preboxes2[col, row, 2, 1] * 10) , int(cube.preboxes2[col, row, 5, 0] * 10) , 600 - int(cube.preboxes2[col, row, 5, 1] * 10) , int(cube.preboxes2[col, row, 3, 0] * 10) , 600 - int(cube.preboxes2[col, row, 3, 1] * 10) ]           

        del cube.preboxes2
        np.set_printoptions(threshold=np.inf)

        cube.create_box = np.empty([9,9,3])

        for col in range (8,-1,-1):
            for row in range (8,-1,-1):
                cube.create_box[col, row, 0] = self.bg.create_polygon(list(cube.boxes[col, row, 0]), fill="{}".format(cube.colorL))
                cube.create_box[col, row, 1] = self.bg.create_polygon(list(cube.boxes[col, row, 1]), fill="{}".format(cube.colorT))
                cube.create_box[col, row, 2] = self.bg.create_polygon(list(cube.boxes[col, row, 2]), fill="{}".format(cube.colorR))
        cube.root.update()



    def box_move(self):
        cube.value = cube.value + 0.01

        nboxes = np.empty([9,9,3,8])
        c = np.empty([9,9])

        for col in range (0,9):
            for row in range (0,9):
                c[col,row] = int(sin(cube.value[col,row]) * 10)

        
        nboxes = np.empty([9,9,3,8])

        for col in range (0,9):
            for row in range (0,9):
                nboxes[col, row, 0] = [cube.boxes[col, row, 0, 0], cube.boxes[col, row, 0, 1] + c[col,row], cube.boxes[col, row, 0, 2], cube.boxes[col, row, 0, 3] + c[col,row], cube.boxes[col, row, 0, 4], cube.boxes[col, row, 0, 5] - c[col,row], cube.boxes[col, row, 0, 6], cube.boxes[col, row, 0, 7] - c[col,row]]
                nboxes[col, row, 1] = [cube.boxes[col, row, 1, 0], cube.boxes[col, row, 1, 1] + c[col,row], cube.boxes[col, row, 1, 2], cube.boxes[col, row, 1, 3] + c[col,row], cube.boxes[col, row, 1, 4], cube.boxes[col, row, 1, 5] + c[col,row], cube.boxes[col, row, 1, 6], cube.boxes[col, row, 1, 7] + c[col,row]]
                nboxes[col, row, 2] = [cube.boxes[col, row, 2, 0], cube.boxes[col, row, 2, 1] - c[col,row], cube.boxes[col, row, 2, 2], cube.boxes[col, row, 2, 3] - c[col,row], cube.boxes[col, row, 2, 4], cube.boxes[col, row, 2, 5] + c[col,row], cube.boxes[col, row, 2, 6], cube.boxes[col, row, 2, 7] + c[col,row]]

        self.bg.delete("all")


        for col in range (8,-1,-1):
            for row in range (8,-1,-1):
                cube.create_box[col, row, 0] = self.bg.create_polygon(list(nboxes[col, row, 0]), fill="{}".format(cube.colorL))
                cube.create_box[col, row, 1] = self.bg.create_polygon(list(nboxes[col, row, 1]), fill="{}".format(cube.colorT))
                cube.create_box[col, row, 2] = self.bg.create_polygon(list(nboxes[col, row, 2]), fill="{}".format(cube.colorR))

        cube.root.update()


main = cube()
cube.root.mainloop()

