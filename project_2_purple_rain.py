from tkinter import *
import random

class rain:
    def __init__(self):
        self.x = random.randint(0,xMax) # The x,y locations of rain
        self.y = random.randint(-500,-50)  
        self.z = random.randint(5, 20) # Smaller z means the farther the rain is, vise versa

        self.sizex = 2 + (self.z * 0.075)  # The size of rain x,y
        self.sizey = random.randint(10,14) + (self.z * 0.4)  
        
        self.yspeed = round(random.uniform(2,4), 2) + (self.z * 0.4) #Speed of rain
        self.sizey_copy = (self.yspeed)

        self.drop = background.create_rectangle(self.x, self.y, self.x - self.sizex, self.y - self.sizey, outline="#E6E6FA" ,fill="#8A2BE2")

    def fall(self):
        if (self.y - self.sizey >= bottom): # If the rain reaches the bottom
            self.x = random.randint(0,xMax) # New random location
            self.y = random.randint(-500,-50)
            self.yspeed = self.sizey_copy # Reset speed

        self.yspeed += 0.01 + (self.z * 0.02) # Gravity (self.z * 0.001) is pretter, (self.z * 0.02) is more realistic

        self.y += self.yspeed # Move the rain 
        background.coords(self.drop, self.x, self.y, self.x - self.sizex, self.y - self.sizey)
        
root = Tk()
top = (0)

bottom = (350) # Y-axis
xMax = (630) # X-axis
numRain = (500) # Number of rain

root.geometry("{}x{}".format(xMax,bottom))
drops = []
background = Canvas(root, width=xMax, height=bottom, background="#E6E6FA")
background.pack()

for i in range(0,numRain): # Initialize all the rains
    drops.append(rain())

while True:
    for i in range(0,numRain):
        drops[i].fall()
        root.update()

root.mainloop()