from Tkinter import *

fps = 30
dt = int(1000/fps)
t = 0
tmax = 100

b1 = "up"
xold, yold = None, None
x = 0
y = 0

def b1down(event):
    global b1
    b1 = "down"           # you only want to draw when the
    global x
    global y
    x, y = event.x, event.y
    global ball
    ball = Particle()
    ball.chars = ["sand", x, y, 0, 0, 0, 0.04, 300, 3, 1]

def b1up(event):
    global b1, xold, yold
    b1 = "up"
    ball.animate()
    xold = None           # reset the line when you let go of the button
    yold = None

def motion(event):
    if b1 == "down":
        global xold, yold
        if xold is not None and yold is not None:
            event.widget.create_line(xold,yold,event.x,event.y,smooth=TRUE)
                          # here's where you draw it. smooth. neat.
        xold = event.x
        yold = event.y



class Particle:

    """Particles have a number of parameters:
        - material mat
        - location x, y
        - velocity vx, vy
        - acceleration ax, ay
        - temperature T
        - mass m
        - interaction strength s
    """

    def __init__(self):
        self.t = 0
        self.x = x
        self.y = y
        self.dx = 10
        self.dy = 10
        self.vx = 0
        self.vy = 0
        self.ax = 0
        self.ay = 1
        self.mat = "sand"
        self.T = 300
        self.m = 3
        self.s = 0

        self.chars = [self.mat, self.x, self.y, self.vx, self.vy, self.ax, self.ay, self.T, self.m, self.s]

        self.shape = c.create_oval(self.chars[1], self.chars[2], self.chars[1]+self.dx, self.chars[2]+self.dy)


        # self.animate()

    def animate(self):

        global b1
        if self.t < 100:
            if (self.x > 640) or (self.x < 0) or (self.y < 0) or (self.y > 480):
                ball.destroy
            else:
                c.move(self.shape, self.chars[5]*self.t+self.chars[3], self.chars[6]*self.t+self.chars[4])
                print self.t
                self.t = self.t + 1
                root.after(dt, self.animate)

    def destroy(self):
        c.delete(ball)


# window
root = Tk()
root.lift()

# canvas
c = Canvas(root, width = 640, height = 480)
c.pack()
# c.bind("<Motion>", motion)
c.bind("<ButtonPress-1>", b1down)
c.bind("<ButtonRelease-1>", b1up)



# toy = Particle()
# toy.chars = ["water", 150, 300, 10, -24, 0, 1, 300, 3, 1]

# Button(root, text="Go", command=ball.animate).pack()

root.mainloop()
