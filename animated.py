from Tkinter import *

fps = 30
dt = int(1000/fps)
t = 0
x = 0
y = 300
dx = 25
dy = 25
vx = 10
vy = -24
ax = 0
ay = 1

def animate():
    global t
    t = t + 1
    c.move(ball, ax*t+vx, ay*t+vy)
    root.after(dt, animate)

root = Tk()
c = Canvas(root, width = 640, height = 480)
c.pack()

def createball():
    ball = c.create_oval(x, y, x+dx, y+dy)
    return ball

# animate()
Button(root, text="Go", command=animate).pack()
root.mainloop()
